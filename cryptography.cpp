//Caeser cipher


#include <iostream>
#include <string>
using namespace std;

int main(){

	//data
	string message;
	int shift;

	//input
	cout << "enter shift: ";
	cin >> shift;
	cout << "enter message: ";
	cin >> message;

	//process and output
	for(int i; i < message.length(); i++){
		cout << char(((int(message[i]) + shift) % 127)) << endl;
	}

	return 0;
}

// int() converts it to ascii code, then char() converts it back to english