
#include <iostream>

#include "libA/libA.h"

int main() {
    std::cout << "App: " << std::endl;
    hello_libA(1, "called from App");
    return 0;
}