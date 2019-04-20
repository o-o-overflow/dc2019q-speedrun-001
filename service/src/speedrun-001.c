#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/* 

   Compilation:
   gcc -o speedrun-001 -no-pie -static -fno-stack-protector speedrun-001.c

 */

void say_hello()
{
   printf("Hello brave new challenger\n");
}

void what_do_they_say()
{
   char buf[1024];
   printf("Any last words?\n");
   read(0, buf, 2000);
   printf("This will be the last thing that you say: %s\n", buf);
}

void say_goodbye()
{
   printf("Alas, you had no luck today.\n");
}

int main(int argc, char** argv)
{
   setvbuf(stdout, NULL, _IONBF, 0);

   say_hello();
   what_do_they_say();
   say_goodbye();
}
