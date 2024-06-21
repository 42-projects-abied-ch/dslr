cmake_minimum_required(VERSION 3.22.1)
project(dslr VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CSS_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(SOURCES
    src/main.cpp
    src/Frog.cpp
)

set(HEADERS
    include/Frog.hpp
)

# Define the root directory
set(ROOT_DIR "${CMAKE_SOURCE_DIR}")

include_directories(include)

add_executable(dslr ${SOURCES} ${HEADERS})

# Pass the root directory to the code
target_compile_definitions(dslr PRIVATE ROOT_DIR="${ROOT_DIR}")
