#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
    do {
        n = get_int("Number of starting llamas: ");
    }
    while (n < 9);
    // TODO: Prompt for end size
    int e;
    do {
        e = get_int("Number of starting llamas: ");
    }
    while (e < n);
    // TODO: Calculate number of years until we reach threshold
    // Calculate gain
    int g = n/3;


    // TODO: Print number of years
}
