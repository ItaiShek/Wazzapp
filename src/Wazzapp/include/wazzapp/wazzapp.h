#pragma once

namespace wazzapp
{
    void show_message(const char* title, const char* message);
    void print_help();
    std::string convert_all(int argc, char *argv[]);
    bool is_console();
}