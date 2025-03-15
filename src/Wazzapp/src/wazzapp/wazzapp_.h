#pragma once

#include <filesystem>


struct converted_info
{
    int converted{};
    int total{};
};

namespace wazzapp
{
    bool is_dir(const std::filesystem::path &path);
    bool is_file(const std::filesystem::path &path);
    bool is_jpeg(const char *path_ch);
    converted_info convert_files(int argc, char *argv[]);
    converted_info convert_dir(const std::filesystem::path &path);
    int convert_single_file(const std::filesystem::path &path);
}