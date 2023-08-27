#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string n = get_string("Name: \n");
    printf("hello, %s\n", n);
}