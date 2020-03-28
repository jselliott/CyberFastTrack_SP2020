#include <stdio.h> 
#include <stdlib.h> 
#include<time.h> 
  
// Driver program 
int main(void) 
{ 

	char str[80];

	int T = time(0);

    srand(T); 
  
    int num1 = rand();
    uint num2 = (num1 - 3) * 3;
  
    if(num2 & 1 != 0)
    {
    	num2 = num2 - 1;
    }

    int num3 = (int) num2 /2 + 7;

    sprintf(str,"%d %d %d %d",T,num1,num2,num3);

    puts(str);
  
    return 0; 
} 