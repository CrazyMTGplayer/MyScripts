#include <iostream>
#include <string>

using namespace std;

string revrecurse(string);

int main(){

    string input;
    getline(cin, input);
    cout << revrecurse(input) <<endl;

}//main()

string revrecurse (string input){
    if ((input.length() == 0) || (input.length() == 1))
        return input;
    else
        return revrecurse(input.substr(1, input.length())) + input.at(0);
}//revrecurse
