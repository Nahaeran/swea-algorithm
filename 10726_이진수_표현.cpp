#include<iostream>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
    cin >> T;
    
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N, M;
        cin >> N >> M;
        int correct = (1 << N) - 1;
        
        if (correct == (M & correct)){
            cout << "#" << test_case << " ON" << endl;
        } else {
             cout << "#" << test_case << " OFF" << endl;
        }
    }
	return 0;
}