
#include <iostream>

#include "libB/libB.h"

int main() {
    std::cout << "App: " << std::endl;
    hello_libB(1, "called from App");
    return 0;
}