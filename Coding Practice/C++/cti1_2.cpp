#include <iostream>
#include <cstdio>
using namespace std;

char* reverse(char*);

int main(){
	char i[256];
	scanf ("%s", i);
	cout << reverse(i) <<endl;
	return 0;
}//main()

char* reverse(char* input){
	int size;
	char tmp;
	for (size = 0; input[size] != '\0';size++);
	int swaps = size / 2;

	for (int i = 0; i < swaps; i++){
		tmp = input[i];
		input[i] = input[size - 1 - i];
		input[size - 1 - i] = tmp;
	}

	return input;
}//reverse()
