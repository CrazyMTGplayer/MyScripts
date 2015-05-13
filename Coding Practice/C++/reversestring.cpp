#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    string input;
    getline(cin, input);
    cout << "Input string " + input + " reversed is ";
    reverse(input.begin(), input.end());
    cout << input << endl;
    return 0;
}//main()
