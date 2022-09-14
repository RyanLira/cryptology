//vigenère cipher
//Ryan Lira 9/12/2022
//identify an elements index in an array 
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

//SEARCH ALGORITHM
int searchAlgorithmIGuess(char n){
	int o = 0;
	int alphabet[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

	while(n != alphabet[o]){
		o++;
	}
	return o;
}

//SECRET OBJECT (SHHH!!!)
class Secret{
	public:
		string word;
		int alphabet[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

		void encrypt(int n){
			for(int i = 0; i < word.length(); i++){
				word[i] = char(alphabet[(searchAlgorithmIGuess(word[i]) + n) % 26]);
			}
		}


		void decrypt(int n){
			for(int i = 0; i < word.length(); i++){
				word[i] = char(alphabet[(searchAlgorithmIGuess(word[i]) - n) % 26]);
			}
		}
};


// MAIN FUNCTION
int main(){
//variables
	Secret message;
	int shift;
	char q;

//input
	cout << "enter word: ";
	cin >> message.word;
	cout << "enter shift: ";
	cin >> shift;
	cout << "Encrypt or Decrypt? (e/d): ";
	cin >> q;

//Process
	if(q == 'e'){
		message.encrypt(shift);
	}
	else if(q == 'd'){
		message.decrypt(shift);
	}
	else{
		cout << "No try again." << endl;
	}

//output
	
	cout << message.word << endl;


	return 0;

}






