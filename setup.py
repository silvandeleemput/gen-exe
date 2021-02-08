from os import path
from setuptools import setup, find_packages


VERSION = "0.2.1"

this_directory = path.abspath(path.dirname(__file__))

with open(
    path.join(this_directory, "README.md"), mode="r", encoding="utf-8"
) as fh:
    long_description = fh.read()

with open(
    path.join(this_directory, "requirements.txt"), mode="r", encoding="utf-8"
) as fh:
    requirements = [e.strip() for e in fh.readlines() if e.strip() != ""]

setup(
    name="gen-exe",
    version=VERSION,
    author="S.C. van de Leemput",
    author_email="silvandeleemput@gmail.com",
    install_requires=requirements,
    include_package_data=True,
    license="LICENSE",
    entry_points={
        "console_scripts": [
            "gen-exe=genexe.generate_exe:cli",
            "add-ico-to-exe=genexe.winicon:cli",
        ]
    },
    packages=find_packages(),
    description="A small utility which allows you to generate Windows executables "
    "that can run custom commands on your Windows system.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
    ],
)
