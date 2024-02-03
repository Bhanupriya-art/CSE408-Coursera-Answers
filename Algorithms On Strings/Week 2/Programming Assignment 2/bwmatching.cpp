#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using std::cin;
using std::istringstream;
using std::map;
using std::string;
using std::vector;
using std::cout;
using std::endl;

// Preprocess the Burrows-Wheeler Transform bwt of some text
// and compute as a result:
//   * starts - for each character C in bwt, starts[C] is the first position 
//       of this character in the sorted array of 
//       all characters of the text.
//   * occ_count_before - for each character C in bwt and each position P in bwt,
//       occ_count_before[C][P] is the number of occurrences of character C in bwt
//       from position 0 to position P inclusive.

// Note: Make occ_count_before[C][P] exclusive P.
// It will make the code cleaner and easier to implement.

void PreprocessBWT(const string& bwt, 
                   map<char, int>& starts, 
                   map<char, vector<int> >& occ_count_before) {
  // Implement this function yourself
  for (int i = 0; i < bwt.size(); i++) {
    starts[bwt[i]]++;
    occ_count_before[bwt[i]][i + 1]++;
    for (auto& it : occ_count_before) {
      if (i < bwt.size()) {
        it.second[i + 1] += it.second[i];
      }
    }
  }

  int cf = 0;
  for (auto& it : starts) {
    if (it.second == 0) {
      it.second = -1;
    } else {
      int temp = it.second;
      it.second = cf;
      cf += temp;
    }
  }
}

// Compute the number of occurrences of string pattern in the text
// given only Burrows-Wheeler Transform bwt of the text and additional
// information we get from the preprocessing stage - starts and occ_count_before.
int CountOccurrences(const string& pattern, 
                     const string& bwt, 
                     const map<char, int>& starts, 
                     const map<char, vector<int> >& occ_count_before) {
  // Implement this function yourself
  string pattern_cp = pattern;
  int top = 0;
  int bottom = bwt.size() - 1;
  while (top <= bottom) {
    if (!pattern_cp.empty()) {
      char symbol = pattern_cp.back();
      pattern_cp.pop_back();
      if (occ_count_before.find(symbol)->second[bottom + 1] > occ_count_before.find(symbol)->second[top]) {
        top = starts.find(symbol)->second + occ_count_before.find(symbol)->second[top];
        bottom = starts.find(symbol)->second + occ_count_before.find(symbol)->second[bottom + 1] - 1;
      } else {
        return 0;
      }
    } else {
      return bottom - top + 1;
    }
  }

  return 0;
}
     

int main() {
  string bwt;
  cin >> bwt;
  int pattern_count;
  cin >> pattern_count;
  // Start of each character in the sorted list of characters of bwt,
  // see the description in the comment about function PreprocessBWT
  map<char, int> starts = {{'$', 0}, {'A', 0}, {'C', 0}, {'G', 0}, {'T', 0}};
  // Occurrence counts for each character and each position in bwt,
  // see the description in the comment about function PreprocessBWT
  map<char, vector<int> > occ_count_before = {{'$', vector<int>(bwt.size() + 1)}, {'A', vector<int>(bwt.size() + 1)}, {'C', vector<int>(bwt.size() + 1)}, {'G', vector<int>(bwt.size() + 1)}, {'T', vector<int>(bwt.size() + 1)}};;
  // Preprocess the BWT once to get starts and occ_count_before.
  // For each pattern, we will then use these precomputed values and
  // spend only O(|pattern|) to find all occurrences of the pattern
  // in the text instead of O(|pattern| + |text|).
  PreprocessBWT(bwt, starts, occ_count_before);

  for (int pi = 0; pi < pattern_count; ++pi) {
    string pattern;
    cin >> pattern;
    int occ_count = CountOccurrences(pattern, bwt, starts, occ_count_before);
    printf("%d ", occ_count);
  }
  printf("\n");
  return 0;
}
