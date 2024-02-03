#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using std::cin;
using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::string;
using std::vector;

void print_int_v(vector<int>& v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout << endl;
}

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
