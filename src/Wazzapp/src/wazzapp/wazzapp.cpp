#include <iostream>
#include <sstream>
#include <Windows.h>

#define STBI_ONLY_JPEG
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

#include "wazzapp.h"
#include "wazzapp_.h"

namespace wazzapp
{
    void show_message(const char *title, const char *message)
    {
        if(is_console())
        {
            return;
        }
        ::MessageBox(nullptr, message, title, MB_OK | MB_ICONINFORMATION);
    }

    void print_help()
    {
        std::cout << "Wazzap - Fix WhatsApp JPEG images for Photoshop\n\n";
        std::cout << "Usage:\n";
        std::cout << "\tWazzapp im1.jpg [im2.jpeg ...]\n";
        std::cout << "\tWazzapp directory";
    }

    std::string convert_all(int argc, char *argv[])
    {
        converted_info ci{};
        if (argc == 1 && is_dir(argv[0]))
        {
            ci = convert_dir(argv[0]);
        }
        else
        {
            ci = convert_files(argc, argv);
        }


        std::ostringstream oss;
        oss << "Converted " << ci.converted << "/" << ci.total << " files";
        auto message = oss.str();
        std::cout << message << std::endl;
        return message;
    }

    bool is_dir(const std::filesystem::path &path)
    {
        return std::filesystem::exists(path) && std::filesystem::is_directory(path);
    }

    bool is_file(const std::filesystem::path &path)
    {
        return std::filesystem::exists(path) && std::filesystem::is_regular_file(path);
    }

    int convert_single_file(const std::filesystem::path &path)
    {
        auto path_str = path.string();
        auto path_ch = path_str.c_str();

        if (is_jpeg(path_ch) == false)
        {
            return 0;
        }

        int width, height, channels;
        auto img = stbi_load(path_ch, &width, &height, &channels, 0);
        if (img == nullptr)
        {
            return 0;
        }

        auto success = stbi_write_jpg(path_ch, width, height, channels, img, 100);

        stbi_image_free(img);

        return success;
    }

    converted_info convert_dir(const std::filesystem::path &path)
    {
        converted_info ci{};
        for (const auto &entry : std::filesystem::recursive_directory_iterator(path))
        {
            if (is_file(entry.path()))
            {
                ci.total++;
                ci.converted += convert_single_file(entry.path());
            }
        }

        return ci;
    }

    converted_info convert_files(int argc, char *argv[])
    {
        converted_info ci{};
        for (std::size_t i{}; i < argc; i++)
        {
            if (is_file(argv[i]))
            {
                ci.total++;
                ci.converted += convert_single_file(argv[i]);
            }
        }

        return ci;
    }

    bool is_jpeg(const char *path_ch)
    {
        int width, height, channels;
        return stbi_info(path_ch, &width, &height, &channels);
    }

    bool is_console()
    {
        DWORD processList[1];
        return GetConsoleProcessList(processList, 1) > 1;
        // return GetConsoleWindow() != nullptr;
    }
}