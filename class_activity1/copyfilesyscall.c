#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int src, dest;
    char buffer[1024];
    ssize_t bytesRead;

    src = open("result.txt", O_RDONLY);
    dest = open("copyresult.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

    if (src < 0 || dest < 0) {
        perror("File open error");
        return 1;
    }

    while ((bytesRead = read(src, buffer, sizeof(buffer))) > 0) {
        write(dest, buffer, bytesRead);
    }

    close(src);
    close(dest);

    return 0;
}
