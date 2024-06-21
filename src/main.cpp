#include <iostream>

#include "Frog.hpp"

int main() {
    std::string filePath = std::string(ROOT_DIR) + "/datasets/dataset_test.csv";
    DataFrame   df = DataFrame(filePath);
    cout << df["First Name"].count();
}