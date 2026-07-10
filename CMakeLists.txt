cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "-g3 -O0 -Wall -Wextra -Wshadow -Werror")

add_library(timezone SHARED timezone.cc)
target_link_options(timezone PUBLIC -static-libstdc++ -static-libgcc)
