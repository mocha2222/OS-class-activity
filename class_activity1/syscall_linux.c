#include <unistd.h>

int main() {
    const char *message = "Hello, System Call!\n";
    write(1, message, 19); // fd 1 = stdout
    return 0;
}
