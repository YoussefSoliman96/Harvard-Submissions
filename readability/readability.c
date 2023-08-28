#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
int letter_count (string text);

//take user input
string text = get_string("The sentence is: ");












int letter_count (char *text);
int letters = 0;
for (int i = 0; i < strlen(text); i++ )
{
    if (isalpha(text[i]))
    {
        letters++;
    }
    return letters;
}
printf("%c letters", letters);
}


