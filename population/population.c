#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int s;
    do {
        s = get_int("Number of starting llamas: ");
    }
    while (s < 9);
    // TODO: Prompt for end size
    int e;
    do {
        e = get_int("Number of starting llamas: ");
    }
    while (e < s);
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
