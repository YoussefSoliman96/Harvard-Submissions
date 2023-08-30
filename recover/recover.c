#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check if argument count > 2
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE...\n");
        return 1;
    }
    // Open memory card
    FILE *input_file = fopen (argv[1], "r");
    // Check if input file is valid
    if (input_file == NULL)
    {
        printf("Couldn't open file");
        return 2;
    }

    // Check if file is JPEG
    unsigned char buffer[512];
    // Number of images
    int image_count = 0;
    // Pointer for recovered images
    FILE *output_file = NULL;
    // File name
    char *file_name = malloc (8 * sizeof(char));
    // Read data from the memory card
    while (fread (buffer, sizeof(char), 512, input_file ))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
                    // Write new file name
                    sprintf(file_name, "%03i.jpg", image_count);
                    // Open a new file with the new file name and write the data to it
                    output_file = fopen(file_name, "w");
                    image_count++;
        }
        if (output_file != NULL)
        {
            fwrite (buffer, sizeof(char), 512, output_file);
        }
    }
    free(file_name);
    fclose(input_file);
    fclose(output_file);
    return 0;

}
