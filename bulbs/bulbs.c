#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int main(void)
{
    // TODO
    string text = get_string("Text: ");

    for (int i = 0, l = strlen(text); i < l; i++)
    {
        int binary[] = {0,0,0,0,0,0,0,0};
        // Convert to ASCII
        int decimal = text [i];
        // Convert ASCII to Binary
        for (int j = 0; decimal > 0; j++)
        {
            binary [j] = decimal % 2;
            decimal = decimal / 2;
        }
        //Reverse the Binary output
        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
           print_bulb(binary[k]);
        }
        printf("\n");
    }
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

