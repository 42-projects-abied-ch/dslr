#include "Frog.hpp"

#include <iostream>

int main() {
    std::string filePath = std::string(ROOT_DIR) + "/datasets/dataset_test.csv";
    DataFrame df = DataFrame(filePath);
    Column col = df["Hogwarts House"];
    for (const auto& row : col) {
        cout << "'" << row << "'" << std::endl;
    }
}