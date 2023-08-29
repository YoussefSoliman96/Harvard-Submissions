#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            float Red = image[i][j].rgbtRed;
            float Blue = image[i][j].rgbtBlue;
            float Green = image[i][j].rgbtGreen;
            // grayscale pixels are made by taking the average color of all color bits in that pixel
            int average = round (Red + Blue + Green / 3);
            image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
        for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            float ORed = image[i][j].rgbtRed;
            float OBlue = image[i][j].rgbtBlue;
            float OGreen = image[i][j].rgbtGreen;

            float SRed = image[i][j].rgbtRed;
            float SBlue = image[i][j].rgbtBlue;
            float SGreen = image[i][j].rgbtGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
