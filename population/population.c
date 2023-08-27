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
    // Calculate gain, we gain n/3 llamas and lose n/4, so current count should be n = n + n/3 - n/4
    int g = n/3;


    // TODO: Print number of years
}
