#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using std::cin;
using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::string;
using std::vector;

// Build suffix array of the string text and
// return a vector result of the same length as the text
// such that the value result[i] is the index (0-based)
// in text where the i-th lexicographically smallest
// suffix of text starts.
vector<int> BuildSuffixArray(const string& text) {
  vector<int> result(text.size());
  // Implement this function yourself
  vector<pair<string, int> > suffix(text.size());
  for (int i = 0; i < text.size(); i++) {
    suffix[i] = make_pair(text.substr(i), i);
  }
  sort(suffix.begin(), suffix.end());
  for (int i = 0; i < suffix.size(); i++) {
    result[i] = suffix[i].second;
  }
  return result;
}

int main() {
  string text;
  cin >> text;
  vector<int> suffix_array = BuildSuffixArray(text);
  for (int i = 0; i < suffix_array.size(); ++i) {
    cout << suffix_array[i] << ' ';
  }
  cout << endl;
  return 0;
}
