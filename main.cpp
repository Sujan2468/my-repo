/* program to find factorial of a number. */
#include<iostream>
using namespace std;
int factorial(int num)
{
if(num==1||num==0)
return 1;
return num*factorial(num-1);
}
int main()
{
int num;
cout<<"Enter a number : ";
cin>>num;
int fact=factorial(num);
cout<<"Factorial of "<<num<<" is "<<fact<<"."<<endl;
return 0;
}
