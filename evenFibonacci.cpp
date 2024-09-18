#include <iostream>
#include <vector>
using namespace std;

class fibonacci { // Create class
    public: // Access specifier
        int evenFib(int max); // Method declaration
};

int fibonacci::evenFib(int max) { // Method definition outside of class
    int term1 = 1;
    int term2 = 2;
    int fibSum = term1 + term2; 
    int total = 0;
    vector<int> fibSeq = {term1, term2, fibSum};

    while (fibSum < max) {
        fibSum = term1 + term2;
        fibSeq.push_back(fibSum);
        term1 = term2;
        term2 = fibSum;
    }
    for (int i : fibSeq) {
        if (i % 2 == 0) {
            total = total + i;
        }
    }
    return total;
    
}

int main() {
    fibonacci myObj; // Create object of fibonacci class
    cout << myObj.evenFib(4000000); // Calling method with maximum number
}