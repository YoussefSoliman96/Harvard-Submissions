#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int word_to_bits(string text);
int main(void)
{
    // TODO
    string text = get_string("Text: ");
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}


int word_to_bits(string text);
int l = strlen(text);
for (i = 0; i < l; i++)
{
    int decimal = message [i];
}