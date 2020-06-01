#include <stdio.h>
#include <string.h>

int main(){

	int t;
	scanf("%d",&t);

	char alice[t];
	char bob[t];
	scanf("%s", alice);

	/*
	A = 65
	T = 84
	G = 71
	C = 67
	0 = 48 
	1 = 49
	2 = 50
	3 = 51
	*/
	
	bob[0] = 65;

	for(int i = 1; i<t; i++){
		if(alice[i] != 51){
		if(bob[i-1] == 65){
			//A
			if(alice[i] == 48){
				bob[i] = 67;
			}
			else if(alice[i] == 49){
				bob[i] = 71;
			}
			else{
				bob[i] = 84;
			}

		}
		else if(bob[i-1] == 84){
			//T
			if(alice[i] == 48){
				bob[i] = 65;
			}
			else if(alice[i] == 49){
				bob[i] = 67;
			}
			else{
				bob[i] = 71;
			}
		}
		else if(bob[i-1] == 71){
			//G
			if(alice[i] == 48){
				bob[i] = 84;
			}
			else if(alice[i] == 49){
				bob[i] = 65;
			}
			else{
				bob[i] = 67;
			}
		}
		else{
			//C
			if(alice[i] == 48){
				bob[i] = 71;
			}
			else if(alice[i] == 49){
				bob[i] = 84;
			}
			else{
				bob[i] = 65;
			}

		}

	}
}
	
	for(int x = 0; x<t; x++){
		printf("%c",bob[x]);
	}


	return 0;


}
