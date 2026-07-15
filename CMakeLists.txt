cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES CXX)

add_library(in SHARED in.cc)
target_link_options(in PRIVATE
    -static-libstdc++
    "-Wl,--version-script=${CMAKE_CURRENT_SOURCE_DIR}/in.map"
)
set_property(TARGET in APPEND PROPERTY LINK_DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/in.map"
)
