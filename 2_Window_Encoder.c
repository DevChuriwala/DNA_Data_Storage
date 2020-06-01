//input binary in array i
//create array n of same length
#include <stdio.h>
#include <string.h>

int main(){

int t;
scanf("%d",&t);
char i[t];
char n[t];
scanf("%s", i);

int k=0;
for ( int j=0;j<x;)
{
if(i[j]=='0'&&i[j+1]=='0')
	{
		n[k]='A';
	}
if(i[j]=='0'&&i[j+1]=='1')
	{
		n[k]='T';
	}
if(i[j]=='1'&&i[j+1]=='0')
	{
		n[k]='G';
	}
if(i[j]=='1'&&i[j+1]=='1')
	{
		n[k]='C';
	}
k++;
j+=2;
}

for(int x = 0; x<z; x++){
		printf("%c",n[x]);
	}
}
