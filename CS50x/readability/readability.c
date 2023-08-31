#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int letter_count(string text);
int word_count(string text);
int sentence_count(string text);

int main(void)
{
    // take user input
    string text = get_string("The sentence is: ");
    int letters = letter_count(text);
    int words = word_count(text);
    int sentences = sentence_count(text);

    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
    int index = round((0.0588 * L) - (0.296 * S) - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
    return 0;
}

int letter_count(string text)
{
    int l = strlen(text);
    int count = 0;
    for (int i = 0; i < l; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int word_count(string text)
{
    int l = strlen(text);
    int count = 1;
    for (int i = 0; i < l; i++)
    {
        if (isblank(text[i]))
        {
            count++;
        }
    }
    return count;
}

int sentence_count(string text)
{
    int l = strlen(text);
    int count = 0;
    for (int i = 0; i < l; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}