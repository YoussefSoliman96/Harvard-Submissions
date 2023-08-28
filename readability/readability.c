#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int letter_count (string text);
int word_count (string text);
int sentence_count (string text);

int main(void)
{


//take user input
string text = get_string("The sentence is: ");
int letters = letter_count(text);
printf("%i letters\n", letters);

int words = word_count(text);
printf("%i words\n", words);

int sentences = sentence_count(text);
printf("%i sentences\n", sentences);










return 0;
}

int letter_count (string text)
{
int l = strlen(text);
int count = 0;
for (int i = 0; i < l; i++ )
{
    if (isalpha(text[i]))
    {
        count++;
    }

}
return count;
}

int word_count (string text)
{
    int l = strlen(text);
    int count = 0;
    for (int i = 0; i < l; i++){
        if(isblank(text[i]))
        {
            count++;
        }
    }
    return count;
}

int sentence_count (string text)
{
    int l = strlen(text);
    int count = 0;
    for (int i = 0; i < l; i++){
        if((text[i] == '.'))
        {
            count++;
        }
    }
    return count;
}