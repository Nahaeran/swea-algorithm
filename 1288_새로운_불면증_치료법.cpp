#include <iostream>
#include <string>
using namespace std;

int main() {
    int tc;
    cin >> tc;
    int total = (1 << 10) - 1; 

    for (int i = 1; i <= tc; i++) {
        int N;
        cin >> N;

        int visited = 0, count = 0;
        while (true) {
            string strNum = to_string(N * (++count));  
            for (char c : strNum) {
                int num = c - '0';
                visited |= (1 << num);  
            }
            if (visited == total) 
                break;
        }

        cout << "#" << i << " " << N * count << endl;
    }

    return 0;
}
