#include <windows.h>
#include <shlwapi.h>
#include <stdlib.h>
#include <iostream>
#include <string>


void replace_all(std::string& str, const std::string& from, const std::string& to) {
    if (from.empty())
        return;
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
}


int main(int argc, char** argv)
{
    char ownPth[MAX_PATH] = "";
    char targetPth[MAX_PATH] = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";

    std::string module_path(".\\");

    HMODULE hModule = GetModuleHandle(NULL);
    if (hModule != NULL)
    {
        // Get exe filename
        GetModuleFileNameA(hModule, ownPth, (sizeof(ownPth)));
        // Strip filename, but leave path
        char* p = strrchr(ownPth, '\\');
        if (p) p[0] = 0;

        module_path = std::string((char*) ownPth);
    }

    std::string command(targetPth);
    // Substitute EXE_DIR macros to the full module_path at its current location
    replace_all(command, "{EXE_DIR}", module_path);
    // Pass all additional arguments to argv, but skip the first
    for (int i = 1; i < argc; i++)
        command = command + " " + std::string(argv[i]);

    return system(command.c_str());
}
