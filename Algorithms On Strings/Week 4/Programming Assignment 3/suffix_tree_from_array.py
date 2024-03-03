# python3
import sys
class SuffixArray:
    """SuffixArray(string) -> build suffix array for string.
    Attributes:
        string        input string
        charset       character set expected in string
                      ("$" is reserved for internal calculation)
    """

    def __init__( self, string ):
        self.string = string
        self.charset = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}

    def _sort_char( self ):
        """Sort string by counting sort."""
        n = len(self.string)
        m = len(self.charset)
        order = [None] * n
        count = [0] * m
        for i in self.string:
            count[self.charset[i]] += 1
        for i in range(1, m):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            char = self.string[i]
            count[self.charset[char]] -= 1
            order[count[self.charset[char]]] = i
        return order

    def _calc_char_class( self, order ):
        """Calculate the equivalence class."""
        _class = [None] * len(self.string)
        _class[order[0]] = 0
        for i in range(1, len(self.string)):
            if self.string[order[i]] != self.string[order[i - 1]]:
                _class[order[i]] = _class[order[i - 1]] + 1
            else:
                _class[order[i]] = _class[order[i - 1]]
        return _class

    def _sort_doubled( self, L, order, _class ):
        """Sort doubled suffix by counting sort."""
        n = len(self.string)
        count = [0] * n
        new_order = [None] * n
        for i in range(n):
            count[_class[i]] = count[_class[i]] + 1
        for i in range(1, n):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            start = (order[i] - L + n) % n
            c = _class[start]
            count[c] -= 1
            new_order[count[c]] = start
        return new_order

    def _update_class( self, L, order, _class ):
        """Update the equivalence class."""
        n = len(self.string)
        new_class = [None] * n
        new_class[order[0]] = 0
        for i in range(1, n):
            current = order[i]
            previous = order[i - 1]
            mid_current = (current + L) % n
            mid_previous = (previous + L) % n
            if _class[current] != _class[previous] or _class[mid_current] != _class[mid_previous]:
                new_class[current] = new_class[previous] + 1
            else:
                new_class[current] = new_class[previous]
        return new_class

    def build( self ):
        """Build suffix array."""
        n = len(self.string)
        order = self._sort_char()
        _class = self._calc_char_class(order)
        L = 1
        while L < n:
            order = self._sort_doubled(L, order, _class)
            _class = self._update_class(L, order, _class)
            L *= 2
        return order


class LongestCommonPrefix:
    """LongestCommonPrefix(string, sa)
       -> build longest common prefix (lcp) array
    Attributes:
        sa          suffix array
        string      input string
    """

    def __init__( self, string, sa ):
        self.sa = sa
        self.string = string

    def build( self ):
        """Build lcp array."""
        n = len(self.string)
        results = [None] * (n - 1)
        order = self.sa
        lcp = 0
        pos_order = self._invert_sa()
        suffix = order[0]
        for i in range(n):
            order_index = pos_order[suffix]
            if order_index == n - 1:
                lcp = 0
                suffix = (suffix + 1) % n
                continue
            next_suffix = order[order_index + 1]
            lcp = self._calc_lcp(suffix, next_suffix, lcp - 1)
            results[order_index] = lcp
            suffix = (suffix + 1) % n
        return results

    def _invert_sa( self ):
        "Invert suffix array."
        n = len(self.sa)
        results = [None] * n
        for i in range(n):
            results[self.sa[i]] = i
        return results

    def _calc_lcp( self, i, j, prev ):
        "Return lcp of current iteration."""
        string = self.string
        n = len(string)
        lcp = max(0, prev)
        while (i + lcp < n) and (j + lcp < n):
            if string[i + lcp] == string[j + lcp]:
                lcp += 1
            else:
                break
        return lcp


class SuffixTreeNode:
    """SuffixTreeNode(node_id, parent, depth, start, end)
       -> node in suffix tree
    Attributes:
        node_id       ID of node (root ID = 0)
        parent        parent node
        depth         length of text from root
        start         start index of substring in string
        end           end index of substring in string
        children      dictionary of tuples
                      tuple = (first char in child node, child node)
    """

    def __init__( self, node_id, parent, depth, start, end ):
        self.node_id = node_id
        self.parent = parent
        self.depth = depth
        self.start = start
        self.end = end
        self.children = {}


class SuffixTree:
    """SuffixTree(sa, lcp, string) -> build suffix tree
    Attributes:
        sa            suffix array
        lcp           longest common prefix (lcp) array
        string        input string
        nodes         number of nodes
        charset       character set expected in string
                      ("$" is reserved for internal calculation)
    """

    def __init__( self, sa, lcp, string ):
        self.sa = sa
        self.lcp = lcp
        self.string = string
        self.nodes = 0
        self.charset = {0: '$', 1: 'A', 2: 'C', 3: 'G', 4: 'T'}

    def build( self ):
        """Build suffix tree."""
        self.root = SuffixTreeNode(0, None, 0, -1, -1)
        self.nodes += 1
        node = self.root
        lcp_prev = 0
        n = len(self.string)
        for i in range(n):
            suffix = self.sa[i]
            while node.depth > lcp_prev:
                node = node.parent
            if node.depth == lcp_prev:
                node = self._new_leaf(node, suffix)
            else:
                start = self.sa[i - 1] + node.depth
                offset = lcp_prev - node.depth
                mid_node = self._break_edge(node, start, offset)
                node = self._new_leaf(mid_node, suffix)
            if i < n - 1:
                lcp_prev = self.lcp[i]

    def _new_leaf( self, node, suffix ):
        """Add new leaf node."""
        depth = len(self.string) - suffix
        start = suffix + node.depth
        end = len(self.string)
        leaf = SuffixTreeNode(self.nodes, node, depth, start, end)
        node.children[self.string[start]] = leaf
        self.nodes += 1
        return leaf

    def _break_edge( self, node, start, offset ):
        """Break edge A-C into A-B-C and return B."""
        depth = node.depth + offset
        end = start + offset
        start_char = self.string[start]
        mid_char = self.string[end]
        mid_node = SuffixTreeNode(self.nodes, node, depth, start, end)
        mid_node.children[mid_char] = node.children[start_char]
        node.children[start_char].parent = mid_node
        node.children[start_char].start += offset
        node.children[start_char] = mid_node
        self.nodes += 1
        return mid_node

    def print_edges( self ):
        """Print all edges in suffix tree."""
        char_num = len(self.charset)
        node = self.root
        stack = [(node, 0)]  # Use a stack instead of recursion
        while len(stack) > 0:
            node, child_char = stack.pop()
            char = self.charset[child_char]
            if char not in node.children:
                if child_char < char_num - 1:
                    stack.append((node, child_char + 1))
                continue
            child = node.children[char]
            print(child.start, child.end)
            if child_char < char_num - 1:
                stack.append((node, child_char + 1))
            if child.children:
                stack.append((child, 0))


if __name__ == '__main__':

    string = input()
    # Build suffix array first
    sa = SuffixArray(string)
    sa = sa.build()
    # Then build longest common prefix array
    lcp = LongestCommonPrefix(string, sa)
    lcp = lcp.build()
    text = sys.stdin.readline().strip()
    print(string)
    # Finally build suffix tree
    suffix_tree = SuffixTree(sa, lcp, string)
    suffix_tree.build()
    suffix_tree.print_edges()
