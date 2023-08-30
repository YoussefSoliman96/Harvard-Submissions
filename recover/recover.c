#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check if argument count > 2
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE...\n");
        return 1;
    }
    // Open memory card
    FILE *f = fopen (argv[1], "r");
    // Check if input file is valid
    if (f == NULL)
    {
        printf("Couldn't open file");
        return 2;
    }

    // Check if file is JPEG
    unsigner char buffer[512];
    // Number of images
    int image_count = 0;
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
                sprintf(filename, "%03i.jpg", 2)
                // Open a new file with the new file name and write the data to it
                FILE *img = fopen(filename, "w");
                fwrite (data, size, number, outputr)
            }
            }
        }
    }
    // Read data from the memory card
    fread (data, size, number, inptr);

}