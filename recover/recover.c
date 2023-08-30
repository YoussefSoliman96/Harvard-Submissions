#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if argument count > 2
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE...\n");
    }
    // Open memory card
    FILE *f = fopen (card.raw, "r");

    // Read data from the memory card
    fread (data, size, number, inptr);

    // Check if file is JPEG
    int buffer[];
    if (buffer[0] == 0xff)
    {
        if (buffer[1] == 0xd8)
        {
            if (buffer[2] == 0xff)
            {
            if ((buffer[3] && 0xf0) == 0xe0)
            {
                printf("file is JPEG");
                // Make a new JPEG file
                sprintf(filename, "%03i.jpg", 2);
                // Open a new file with the new file name and write the data to it
                FILE *img = fopen(filename, "w");
                fwrite (data, size, number, outputr)
            }
            }
        }
    }

return 1;

}