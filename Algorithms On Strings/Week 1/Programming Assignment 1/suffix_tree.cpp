#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <utility>

using std::cin;
using std::cout;
using std::endl;
using std::map;
using std::string;
using std::vector;
using std::pair;
using std::make_pair;

struct Node {
  pair<int, int> range;
  vector<Node> next;
};

// Build a suffix tree of the string text and return a vector
// with all of the labels of its edges (the corresponding 
// substrings of the text) in any order.
vector<string> ComputeSuffixTreeEdges(const string& text) {
  vector<string> result;
  // Implement this function yourself
  Node trie;
  for (int i = text.size() - 1; i >= 0; i--) {
    bool found = false;
    Node curr = trie;
    int j = i;
    bool cont_to_next_level = true;
    while (cont_to_next_level) {
      if (curr.next.empty()) {
        break;
      }
      for (int k = 0; k < curr.next.size(); k++) {
        if (text[j] == text[curr.next[k].range.first]) {
          found = true;
          int l = curr.next[k].range.first;
          int r = curr.next[k].range.second;
          while(text[j] == text[l]) {
            if (l == r) {
              cont_to_next_level = true;
              curr = curr.next[k];
              j++;
              break;
            }
            j++;
            l++;
            cont_to_next_level = false;
          }
          if (!cont_to_next_level) {
            curr = curr.next[k];
            curr.range.second = l - 1;
            Node new_node;
            new_node.range = make_pair(j, text.size() - 1);
            curr.next.push_back(new_node);
          }
          break;
        }
      }
    }
    if (!found) {
      Node new_node;
      new_node.range = make_pair(i, text.size() - 1);
      trie.next.push_back(new_node);
    }
  }
  return result;
}

int main() {
  string text;
  cin >> text;
  vector<string> edges = ComputeSuffixTreeEdges(text);
  for (int i = 0; i < edges.size(); ++i) {
    cout << edges[i] << endl;
  }
  return 0;
}
