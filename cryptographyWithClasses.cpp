//Caeser cipher
//Ryan Lira 9/12/2022
#include <iostream>
#include <string>
using namespace std;





class secret{
	public:
		string mes;

		void encrypt(int n){
			for(int i; i < mes.length(); i++){
				mes[i] = char((int(mes[i]) + n) % 127);
			}
		}

		void decrypt(int n){
			for(int i; i < mes.length(); i++){
				mes[i] = char((int(mes[i]) - n) % 127);
			}
		};
};


int main(){

	secret message;
	int key;

	cout << "enter message: ";
	cin >> message.mes;
	cout << "enter shift number: ";
	cin >> key;
	cout << endl;

	message.encrypt(key);
	cout << message.mes << endl;
	cout << endl;

	return 0;
}

// int() converts it to ascii code, then char() converts it back to english






