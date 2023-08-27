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
        e = get_int("Number of ending llamas: ");
    }
    while (e < n);
    // TODO: Calculate number of years until we reach threshold
    // Calculate gain and loss, we gain n/3 llamas and lose n/4, so current count should be n = n + n/3 - n/4
    // Year count is the number of iterations i

    int y = 0;

    do {
        n = n + (n/3) - (n/4);
        y++;
    }
    while (n < e);

    // TODO: Print number of years

    printf("years: %i /n", y);
}
