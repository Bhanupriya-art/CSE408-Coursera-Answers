#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int char_to_idx(char x) {
  switch (x) {
    case '$':
      return 0;
    case 'A':
      return 1;
    case 'C':
      return 2;
    case 'G':
      return 3;
    case 'T':
      return 4;
  }
}

void counting_sort_char(const string& text, vector<int>& order) {
  vector<int> c_f(5, 0);
  for (int i = 0; i < text.size(); i++) {
    c_f[char_to_idx(text[i])]++;
  }
  for (int i = 1; i < c_f.size(); i++) {
    c_f[i] += c_f[i - 1];
  }
  for (int i = text.size() - 1; i >= 0; i--) {
    order[--c_f[char_to_idx(text[i])]] = i;
  }
}

void compute_class(const string& text, vector<int>& order, vector<int>& sort_class) {
  int count = 0;
  sort_class[order[0]] = count;
  for (int i = 1; i < order.size(); i++) {
    if (text[order[i]] == text[order[i - 1]])
      sort_class[order[i]] = count;
    else
      sort_class[order[i]] = ++count;
  }
}

vector<int> sort_double(const string& text, int l, vector<int>& order, vector<int>& sort_class) {
  vector<int> new_order(text.size());
  vector<int> c_f(text.size(), 0);

  for (int i = 0; i < order.size(); i++) {
    c_f[sort_class[i]]++;
  }
  for (int i = 1; i < c_f.size(); i++) {
    c_f[i] += c_f[i - 1];
  }
  for (int i = order.size() - 1; i >= 0; i--) {
    int start = (order[i] - l + order.size()) % order.size();
    new_order[--c_f[sort_class[start]]] = start;
  }
  order.clear();
  return new_order;
}

vector<int> update_class(vector<int>& order, vector<int>& sort_class, int l) {
  vector<int> new_sort_class(order.size());
  int count = 0;
  new_sort_class[order[0]] = count;
  for (int i = 1; i < order.size(); i++) {
    int cur = order[i];
    int cur_mid = (order[i] + l) % order.size();
    int prev = order[i - 1];
    int prev_mid = (order[i - 1] + l) % order.size();
    if (sort_class[cur]!= sort_class[prev] || sort_class[cur_mid] != sort_class[prev_mid]) {
      new_sort_class[order[i]] = ++count;
    } else {
      new_sort_class[order[i]] = count;
    }
  }
  sort_class.clear();
  return new_sort_class;
}

// Build suffix array of the string text and
// return a vector result of the same length as the text
// such that the value result[i] is the index (0-based)
// in text where the i-th lexicographically smallest
// suffix of text starts.
vector<int> BuildSuffixArray(const string& text) {
  vector<int> result;
  // Implement this function yourself
  vector<int> order(text.size());
  counting_sort_char(text, order);

  vector<int> sort_class(text.size());
  compute_class(text, order, sort_class);

  for (int l = 1; l <= text.size(); l *= 2) {
    order = sort_double(text, l, order, sort_class);
    sort_class = update_class(order, sort_class, l);
  }

  return order;
}

string BWT_fast(const string& text, vector<int>& suffix_array) {
  string result = "";
  for (int i = 0; i < suffix_array.size(); i++) {
    result += text[(suffix_array[i] - 1 + text.size()) % text.size()];
  }
  return result;
}

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


vector<int> FindOccurrences(const string& pattern, 
                            const string& text, 
                            const vector<int>& suffix_array, 
                            const string& bwt, 
                            const map<char, int>& starts, 
                            const map<char, vector<int> >& occ_count_before) {
  vector<int> result;

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
        return result;
      }
    } else {
      for (int i = top; i <= bottom; i++) {
        result.push_back(suffix_array[i]);
      }
      return result;
    }
  }

  return result;
}

int main() {
  char buffer[100001];
  scanf("%s", buffer);
  string text = buffer;
  text += '$';
  vector<int> suffix_array = BuildSuffixArray(text);

  string bwt = BWT_fast(text, suffix_array);

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

  int pattern_count;
  scanf("%d", &pattern_count);
  vector<bool> occurs(text.length(), false);
  for (int pattern_index = 0; pattern_index < pattern_count; ++pattern_index) {
    scanf("%s", buffer);
    string pattern = buffer;
    vector<int> occurrences = FindOccurrences(pattern, text, suffix_array, bwt, starts, occ_count_before);
    for (int j = 0; j < occurrences.size(); ++j) {
      occurs[occurrences[j]] = true;
    }
  }
  for (int i = 0; i < occurs.size(); ++i) {
    if (occurs[i]) {
      printf("%d ", i);
    }
  }
  printf("\n");
  return 0;
}
