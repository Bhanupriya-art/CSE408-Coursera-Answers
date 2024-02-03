#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

string BWT(const string& text) {
  string result = "";

  // write your code here
  vector<string> m(text.size());
  for (int i = 0; i < m.size(); i++) {
  	m[i] = text.substr(i) + text.substr(0, i);
  }

  sort(m.begin(), m.end());

  for (int i = 0; i < m.size(); i++) {
  	result += m[i][m.size() - 1];
  }

  return result;
}

int main() {
  string text;
  cin >> text;
  cout << BWT(text) << endl;
  return 0;
}