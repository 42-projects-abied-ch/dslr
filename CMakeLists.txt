cmake_minimum_required(VERSION 3.22.1)
project(describe VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CSS_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(SOURCES
    src/main.cpp
    src/DataFrame.cpp
    src/Column.cpp
    src/Row.cpp
)

set(HEADERS
    include/DataFrame.hpp
    include/Column.hpp
    include/Row.hpp
)

set(ROOT_DIR "${CMAKE_SOURCE_DIR}")

include_directories(include)
add_subdirectory(matplotplusplus)

add_executable(describe ${SOURCES} ${HEADERS})
target_link_libraries(describe PUBLIC matplot)

target_compile_definitions(describe PRIVATE ROOT_DIR="${ROOT_DIR}")