#include <iostream>
#include <Windows.h>

#include "wazzapp.h"

int main(int argc, char *argv[])
{
    if (wazzapp::is_console() == false)
    {
        ::ShowWindow(::GetConsoleWindow(), SW_HIDE);
    }
    if (argc < 2)
    {
        wazzapp::show_message("Wazzap - Fix WhatsApp JPEG images for Photoshop", "Add at least one JPEG file as an argument");
        wazzapp::print_help();
        return 0;
    }

    auto message = wazzapp::convert_all(argc - 1, argv + 1);
    wazzapp::show_message("Wazzap - Finished", message.c_str());

    return 0;
}