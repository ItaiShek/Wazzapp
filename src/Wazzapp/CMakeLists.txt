cmake_minimum_required(VERSION 3.31.5)

project(Wazzapp
        VERSION 1.0.1
        DESCRIPTION "Fix WhatsApp jpeg images for Photoshop"
        HOMEPAGE_URL "https://github.com/ItaiShek/Wazzapp"
        LANGUAGES C CXX)

# source
add_library(wazzapp_lib STATIC "src/wazzapp/wazzapp.cpp")
target_include_directories(wazzapp_lib PUBLIC "include/wazzapp/")
target_include_directories(wazzapp_lib PRIVATE "extern/stb/")
target_include_directories(wazzapp_lib PRIVATE "src/wazzapp/")
target_compile_features(wazzapp_lib PUBLIC cxx_std_17)

if(WIN32)
    add_executable(Wazzapp "src/main/main.cpp" app.rc)
else()
    add_executable(Wazzapp "src/main/main.cpp")
endif()


target_link_libraries(Wazzapp PUBLIC wazzapp_lib)