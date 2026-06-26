#include <stdio.h>
#include <stdbool.h>

int main() {
    int age = 25; //integer variables
    printf("You are %d are years old", age);
    
    float gpa = 2.5; //Float variables
    printf("Your gpa is %.1f", gpa);

    double pi = 3.14159265358979; //higher precision compared to float, Format Specifier %lf

    char tier = 'S'; //single letter strings, format specifier %c
    char name[] = "Name"; //array of characters or a string, format specifier %s

    bool isOnline = true;

    if(isOnline){
        printf("You are online");
    }
    else{
        printf("You are offline");
    }

    //width precision flags
    float price = 19.99;
    printf("%+7.2f\n", price); //+ -> flag, 7 - width, .2 -> decimal points.


    return 0;
}