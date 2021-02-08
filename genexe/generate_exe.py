from typing import Optional
from pathlib import Path
import click
from genexe.winicon import add_icon_to_exe


SCRIPT_DIR = Path(__file__).parent.absolute().resolve()
RESOURCES_DIR = SCRIPT_DIR / "res"
EXE_TEMPLATE_FILE = RESOURCES_DIR / "template"
MAX_CMD_LENGTH = 259
REPLACE_SIGNATURE = (b"X" * MAX_CMD_LENGTH) + b"1"


def generate_exe(
    target: Path,
    command: str,
    icon_file: Optional[Path] = None,
    show_console: bool = True,
):
    target = target.absolute().resolve()
    if target == EXE_TEMPLATE_FILE:
        raise RuntimeError(
            "Cannot overwrite the source EXE_TEMPLATE_FILE file! Pick a different target executable name."
        )
    with open(EXE_TEMPLATE_FILE, "rb") as f:
        data = f.read()
    if len(command) > MAX_CMD_LENGTH:
        print(
            "Warning encode string was longer than MAX_CMD_LENGTH characters and will be truncated..."
        )
        command = command[:MAX_CMD_LENGTH]
    else:
        command = command + "\0" * (MAX_CMD_LENGTH - len(command))
    assert len(command) == MAX_CMD_LENGTH
    msg = command + ("1" if show_console else "0")
    byte_encoded_string = msg.encode("ascii")
    data = data.replace(REPLACE_SIGNATURE, byte_encoded_string)
    print(f"Encode show_console : {show_console}")
    print(f"Adding following command to exe : `{command.strip()}`")
    print(f"Writing exe to: {target}")
    with open(target, "wb") as f:
        f.write(data)
    if icon_file is not None:
        icon_file = Path(icon_file).absolute().resolve()
        print(f"Adding icon to exe: {icon_file}")
        add_icon_to_exe(target_exe_file=target, source_icon_file=icon_file)
    print("Done.")


class ClickPath(click.Path):
    """A Click path argument that returns a pathlib.Path object instead of a str"""

    def convert(self, value, param, ctx):
        return Path(super().convert(value, param, ctx))


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument(
    "target", type=ClickPath(exists=False, file_okay=True, dir_okay=False)
)
@click.argument("command", type=str)
@click.option(
    "-i",
    "--icon-file",
    "icon_file",
    type=ClickPath(exists=True, file_okay=True, dir_okay=False),
    default=None,
    help="Optional icon file to embed in the executable. Default is to use no icon-file",
)
@click.option(
    "-hc",
    "--hide-console",
    "show_console",
    is_flag=True,
    default=True,
    help="Hide the executable console window. Default show the console window",
)
def cli(
    target: Path, command: str, icon_file: Optional[Path], show_console: bool
):
    """
    Generate an executable which will run the provided command on your Windows system.

    The command argument supports the `{EXE_DIR}` macro, which expands the path where the
    executable is executed from.

    Optionally you can provide an icon file for the executable.
    """

    generate_exe(
        target=target,
        command=command,
        icon_file=icon_file,
        show_console=show_console,
    )


if __name__ == "__main__":
    cli()
