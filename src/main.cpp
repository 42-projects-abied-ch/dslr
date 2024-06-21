#include <iostream>

#include "Frog.hpp"

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <path_to_dataset>" << std::endl;
        return 1;
    }
    DataFrame df = DataFrame(string(ROOT_DIR) + "/" + argv[1]);
    cout << df["First Name"].count();
}