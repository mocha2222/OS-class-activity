#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid;

    pid = fork();   // create child process

    if (pid < 0) {
        perror("fork failed");
        return 1;
    }

    if (pid == 0) {
        // Child process
        execlp("ls", "ls", NULL);
        perror("exec failed");
    } else {
        // Parent process
        wait(NULL); // wait for child to finish
        printf("Child process finished.\n");
    }

    return 0;
}
