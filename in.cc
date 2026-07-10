#include <sstream>

extern "C" void c_int_in(char* str, int* result) {
    std::istringstream ss(str);
    ss >> *result;
}
