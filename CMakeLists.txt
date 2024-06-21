cmake_minimum_required(VERSION 3.22.1)
project(dslr VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CSS_STANDARD_REQUIRED True)

set(SOURCES
    src/main.cpp
    src/example.cpp
)

set(HEADERS
    include/utils.h
)

include_directories(include)

add_executable(dslr ${SOURCES} ${HEADERS})