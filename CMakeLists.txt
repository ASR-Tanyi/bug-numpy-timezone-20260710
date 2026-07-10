cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES CXX)

add_library(in SHARED in.cc)
target_link_options(in PUBLIC -static-libstdc++)
