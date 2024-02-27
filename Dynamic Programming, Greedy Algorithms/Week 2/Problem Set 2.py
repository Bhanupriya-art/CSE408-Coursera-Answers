#!/usr/bin/env python
# coding: utf-8

# ## Problem 1 : Longest Stable Subsequence
# 
# Consider a list of numbers $[a_0, a_1, \cdots, a_{n-1}]$. Our goal is to find the the longest stable subsequence: $[a_{i_1}, a_{i_2}, \cdots, a_{i_k} ]$ which is a sub-list of the original list that selects elements at indices $i_1, i_2, \ldots, i_k$ from the original list such that 
#   1. $i_1 < i_2 < \cdots < i_k$; 
#   2. $a_{i_{j+1}} - 1 \leq a_{i_{j}} \leq a_{i_{j+1}} + 1 $. We can also write this as $|a_{i_{j+1}} - a_{i_j}| \leq 1$. I.e, each element of the subsequence must be within $\pm 1$ or equal to the previous element.
#   3. The length of the subsequence $k$ is maximized.
# 
# ### Example 
# 
# Consider the list `[1, 4, 2, -2, 0, -1, 2, 3]`.  There are many "stable subsequences":
#  - `[1, 0, -1]`
#  - `[1, 2, 2, 3]`
#  - `[4, 3]`
# 
# The longest stable subsequence is `[1, 2, 2, 3]` of length 4. Note that each element of the subsequence is at most $1$ away from the previous element.
# 
# The goal of this problem is to formulate a dynamic programming solution to find the length of the longest stable subsequence and the subsequence itself.

# ### A: Write a Recurrence With Base Case
# $$\newcommand\lss{\textsf{LSSLength}}$$
# Let $n$ be the length of the original array $[a_0, \ldots, a_{n-1}]$. Define $$\lss(\color{red}{i}, a_j)$$ to be the length of the longest stable subsequence for the subarray from $[a_{\color{red}{i}}, \ldots, a_{n-1}]$ (note that $a_{\color{red}{i}}$ is included) with the additional constraint that the  first element in the subsequence chosen (let us call it $a_{i_1}$) must satisfy $$| a_{i_1} - a_j |  \leq 1$$.
# 
# 
# __Notes__
#   0. $0 \leq i \leq n$. $i = n$ denotes the empty subarray.
#   1. $a_j$ represents a previous choice we have made before encountering the current subproblem. It is made an argument of the recurrence to ensure that the subsequent choice made from $[a_i, \ldots, a_{n-1}]$ satisfies $|a - a_j| \leq 1$.
#   2. We will use the special value $a_j = \textsf{None}$ to denote that no such element $a_j$ has been chosen.
# 
# Fill out the missing portion of the recurrence and base cases. We will not grade your answer below. Instead please use it as a guide to complete the code for the recurrence and pass the test cases provided.
# 
# 
# $\lss(i, a_j) = \begin{cases}
# ?? & i = n & \text{# Base Case when subarray is empty} \\
# \lss(i+1, a_j) & i < n\ \text{and}\ a_j \not= \text{None}\ \text{and}\ |a_i - a_j| > 1 & \text{# We cannot choose a[i], skip it and move right along}\\
# \max(??? + 1, ??? ) & i < n\ \text{and}\ \left( a_j = \text{None}\ \text{or}\ |a_i - a_j| \leq 1 \right) & \text{# Choose maximum of two options: take a[i]  or skip a[i]}\\
# \end{cases}$
# 
# 

# YOUR ANSWER HERE

# In[1]:


def lssLength(a, i, j):
    aj = a[j] if 0 <= j < len(a) else None 
    # Base Case when subarray is empty
    if i == len(a):
        return 0
    # We cannot choose a[i], skip it and move right along
    # Choose maximum of two options: take a[i] or skip a[i]
    if j == -1 or (aj is not None and abs(a[i] - aj) <= 1):
        return max(1 + lssLength(a, i+1, i), lssLength(a, i+1, j))
    else:
        return lssLength(a, i+1, j)


# In[2]:


print('--Test1--')
n1 = lssLength([1, 4, 2, -2, 0, -1, 2, 3],0, -1)
print(n1)
assert n1== 4, f'Test 1 failed: expected answer 4, your code: {n1}'
print('passed')

print('--Test2--')
n2 = lssLength([1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6], 0, -1)
print(n2)
assert n2 == 8, f'Test 2 failed: expected answer 8, your code: {n2}'

print('--Test3--')
n3 = lssLength([0,2, 4, 6, 8, 10, 12],0, -1)
print(n3)
assert n3 == 1, f'Test 3 failed: expected answer 1, your code: {n3}'


print('--Test 4--')
n4 = lssLength([4,8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2, -3, -1], 0, -1)
print(n4)
assert n4 == 14, f'Test 4 failed: expected answer 14, your code: {n4}'

print('All Tests Passed (8 points)')


# ## Part 2: Memoize the Recurrence 
# 
# Construct a memo table as a dictionary that maps from `(i,j)` where `0 <= i <= n` and `-1 <= j < i` to the value $\lss(a, i, a_j)$ where $a_j = a[j]$ if $j \geq 0$ else $a_j = \text{None}$.
# 
# Your code should run in worst case time $\Theta(n^2)$.

# In[3]:


def memoizeLSS(a):
    T = {} # Initialize the memo table to an empty dictionary
    # Populate the entries for the base case
    n = len(a)
    for j in range(-1, n):
        T[(n, j)] = 0  # i = n and j
    # Fill out the table
    for i in range(n-1, -1, -1):  # Iterate backward for i
        for j in range(i-1, -2, -1):  # Iterate backward for j
            aj = a[j] if j >= 0 else None
            if j == -1 or (aj is not None and abs(a[i] - aj) <= 1):
                T[(i, j)] = max(1 + T[(i+1, i)], T[(i+1, j)])
            else:
                T[(i, j)] = T[(i+1, j)]
    return T


# In[4]:


def lssLength(a, i, j):
    assert False, 'Redefining lssLength: You should not be calling this function from your memoization code'

def checkMemoTableHasEntries(a, T):
    for i in range(len(a)+1):
        for j in range(i):
            assert (i, j) in T, f'entry for {(i,j)} not in memo table'
            
def checkMemoTableBaseCase(a, T):
    n = len(a)
    for j in range(-1, n):
        assert T[(n, j)] == 0, f'entry for {(n,j)} is not zero as expected'
        
print('-- Test 1 -- ')
a1 = [1, 4, 2, -2, 0, -1, 2, 3]
print(a1)
T1 = memoizeLSS(a1)
checkMemoTableHasEntries(a1, T1)
checkMemoTableBaseCase(a1, T1)
assert T1[(0, -1)] == 4, f'Test 1: Expected answer is 4. your code returns {T1[(0, -1)]}'
print('Passed')


print('--Test2--')
a2 = [1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6]
print(a2)
T2 = memoizeLSS(a2)
checkMemoTableHasEntries(a2, T2)
checkMemoTableBaseCase(a2, T2)
assert T2[(0, -1)] == 8, f'Test 2: Expected answer is 8. Your code returns {T2[(0, -1)]}'

print('--Test3--')
a3 = [0,2, 4, 6, 8, 10, 12]
print(a3)
T3 = memoizeLSS(a3)
checkMemoTableHasEntries(a3, T3)
checkMemoTableBaseCase(a3, T3)
assert T3[(0, -1)] == 1, f'Test 3: Expected answer is  1. Your code returns {T3[(0, -1)]}'


print('--Test4--')
a4 = [4,8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2, -3, -1]
print(a4)
T4 = memoizeLSS(a4)
checkMemoTableHasEntries(a4, T4)
checkMemoTableBaseCase(a4, T4)
assert T4[(0, -1)] == 14, f'Text 4: Expected answer is 14. Your code returns {T4[(0,-1)]}'

print('All tests passed (7 points)')


# ## Part 3: Modify Memoized Code to Recover Solution
# 
# Write a function `computeLSS(a)` that modifies the memo table to allow you to recover the longest stable subsequence as well as its length. `computeLSS` should return  the longest stable subsequence of the input `a` as a list.
# 

# In[5]:


def memoizeLSS(a):
    T = {} # Initialize the memo table to an empty dictionary
    n = len(a)
    
    # Populate the entries for the base case
    for j in range(-1, n):
        T[(n, j)] = (0, [])  # i = n and j
    
    # Fill out the table
    for i in range(n-1, -1, -1):  # Iterate backward for i
        for j in range(-1, n):  # Iterate over all possible values of j
            aj = a[j] if j >= 0 else None
            if j == -1 or (aj is not None and abs(a[i] - aj) <= 1):
                length, sequence = max((1 + T[(i+1, i)][0], [a[i]] + T[(i+1, i)][1]), T[(i+1, j)], key=lambda x: x[0])
            else:
                length, sequence = T[(i+1, j)]
            T[(i, j)] = (length, sequence)
    
    return T

def computeLSS(a):
    # Call memoizeLSS to obtain the memo table
    T = memoizeLSS(a)
    # Initialize variables to track the maximum length and its ending index
    max_length = 0
    max_sequence = []
    n = len(a)
    # Find the maximum length and its ending index from the memo table
    for j in range(-1, n):
        length, sequence = T[(0, j)]
        if length > max_length:
            max_length = length
            max_sequence = sequence
    return max_sequence

## BEGIN TESTS 
def checkSubsequence(a, b):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    for j in range(m-1):
        assert abs(b[j] - b[j+1]) <= 1
    while (i < n and j < m):
        if a[i] == b[j]: 
            j = j + 1
        i = i + 1
    if j < m:
        return False
    return True 


# In[6]:


## BEGIN TESTS 
def checkSubsequence(a, b):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    for j in range(m-1):
        assert abs(b[j] - b[j+1]) <= 1
    while (i < n and j < m):
        if a[i] == b[j]: 
            j = j + 1
        i = i + 1
    if j < m:
        return False
    return True 

print('--Test 1 --')
a1 = [1, 4, 2, -2, 0, -1, 2, 3]
print(a1)
sub1 = computeLSS(a1)
print(f'sub1 = {sub1}')
assert len(sub1) == 4, f'Subsequence does not have length 4'
assert checkSubsequence(a1, sub1), f'Your solution is not a subsequence of the original sequence'

print('--Test2--')
a2 = [1, 2, 3, 4, 0, 1, -1, -2, -3, -4, 5, -5, -6]
print(a2)
sub2 = computeLSS(a2)
print(f'sub2 = {sub2}')
assert len(sub2) == 8
assert checkSubsequence(a2, sub2)

print('--Test3--')
a3 = [0,2, 4, 6, 8, 10, 12]
print(a3)
sub3 = computeLSS(a3)
print(f'sub3 = {sub3}')
assert len(sub3) == 1
assert checkSubsequence(a3, sub3)



print('--Test4--')
a4 = [4,8, 7, 5, 3, 2, 5, 6, 7, 1, 3, -1, 0, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1, 2, 4, 5, 0, 2, -3, -9, -4, -2, -3, -1]
print(a4)
sub4 = computeLSS(a4)
print(f'sub4 = {sub4}')
assert len(sub4) == 14
assert checkSubsequence(a4, sub4)

print('All test passed (10 points)')
## END TESTS


# ## Problem 2

# We are given a set of _natural numbers_ $S:\ \{ n_1, \ldots, n_k \}$ and a target _natural number_ $N$.
# 
# 
# Our goal is to choose a subset of numbers $T:\ \{ n_{i_1}, \ldots, n_{i_j} \} \subseteq S$ such that:
# 
#  1. $\sum_{l=1}^j n_{i_l}  \leq N$, the sum of chosen numbers is less than or equal to $N$, 
#  2. The difference $N - \sum_{l=1}^j n_{i_l} $ is made as small as possible.
# 
# For example, $S = \{ 1, 2, 3, 4, 5, 10 \}$ and $N = 20$ then 
#   - Choosing $T = \{1, 2, 3, 4, 5\}$, we have   $1 + 2 + 3 + 4 + 5 = 15 \leq 20$, achieving a difference of $5$.  
#   - However, if we chose $T = \{ 2,3,5,10\}$  we obtain a sum of $2 + 3 + 5 + 10 = 20$ achieving the smallest possible difference of $0$.
#   - Choosing $T = \{ 2, 3, 4, 5, 10\}$ is disallowed because $2 + 3 + 4+ 5+ 10 = 24 > 20$.
# 
# 
# Therefore the problem is as follows:
# 
#   * Inputs: list  $S: [n_1, \ldots, n_k]$ (assume that no element repeats in $S$), and number $N$.
#   * Output: a list $T$ of elements from $S$ such that sum of elements of $T$ is  $\leq N$ and $N - \sum_{e \in T} e$ is the smallest possible.
# 
# The subsequent parts to this problem ask you to derive a dynamic programming solution to this problem.
# 
# __Note:__ Because $S$ and $T$ are viewed as sets, each element in the set may occur exactly once.
# 
# ### Part (A) Write a recursive function
# 
# $$\newcommand\targetSum{\textsf{targetSum}}$$
# Write down a recurrence: $\targetSum( \{ S[i], \ldots, S[k] \}, \hat{T} )$ that expresses the best possible solution to the sub problem where 
#   - we choose a subset of $S$ with elements from from $S[i]$  to $S[k]$ inclusive. 
#   - If $i > k$, we take that to be the empty set and 
#   - $\hat{T}$ is the current target.
#   
#  Complete the missing portions of the definitions below.
# 
# $$\targetSum(\left\{ S[i], \ldots, S[k] \right\}, \hat{T}) = \begin{cases}
#   ??? & \hat{T} < 0 \\
#   ??? & i > k\ \text{and}\ \hat{T} \geq 0 \\
#   \min( ???, ???) & \mbox{otherwise}\\
# \end{cases} $$
# 

# YOUR ANSWER HERE

# In[65]:


def targetSum(S, i, tgt):
    if tgt < 0:
        return float('inf')
    elif i > len(S) - 1:
        return abs(tgt)
    else:
        include_current = targetSum(S, i + 1, tgt - S[i])
        exclude_current = targetSum(S, i + 1, tgt)
        return min(include_current, exclude_current)


# In[66]:


def tgtSum(tgt, S):
    return targetSum(S, 0, tgt)

t1 = tgtSum(15, [1, 2, 3, 4, 5, 10]) # Should be zero
assert t1 == 0, 'Test 1 failed'

t2 = tgtSum(26, [1, 2, 3, 4, 5, 10]) # should be 1
assert t2 == 1, 'Test 2 failed'

t3 = (tgtSum(23, [1, 2, 3, 4, 5, 10])) # should be 0
assert t3 == 0, 'Test 3 failed'


t4 = (tgtSum(18, [1, 2, 3, 4, 5, 10])) # should be 0
assert t4 == 0, 'Test 4 failed'

t5 = (tgtSum(9, [1, 2, 3, 4, 5, 10])) # should be 0
assert t5 == 0, 'Test 5 failed'

t6 = (tgtSum(457, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t6 == 1, 'Test 6 failed'

t7 = (tgtSum(512, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 0
assert t7 == 0, 'Test 7 failed'

t8 = (tgtSum(616, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413])) # should be 1
assert t8 == 1, 'Test 8 failed'

print('All tests passed (10 points)!')


# ### Part (B) 
# 
# Memoize your recurrence by using a memo table of the form $T[(i, j)]$ wherein $0 \leq i \leq len(S)$ and $0 \leq j \leq \textsf{tgt}$. It may be helpful to add a function `lookupMemoTable` inside your code to help you handle lookups where $j < 0$. Assume that the target satisfies `tgt >= 0`. 
# 

# In[43]:


def memoTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    ## Fill in base case for T[(i,j)] where i == k
    T = {} # Memo table initialized as empty dictionary
    for j in range(tgt+1):
        T[(k,j)] = j
    
    # your code here
    for i in range(k-1, -1, -1):
        for j in range(tgt + 1):
            optA = T[(i + 1, j)]
            if j - S[i] >= 0:
                optB = T[(i + 1, j - S[i])]
            else:
                optB = float('inf')
            T[(i, j)] = min(optA, optB)
                
    return T


# In[44]:


def checkMemoTblTargetSum(a, tgt, expected):
    T = memoTargetSum(a, tgt)
    for i in range(len(a)+1):
        for j in range(tgt+1):
            assert (i, j) in T, f'Memo table fails to have entry for i, j = {(i, j)}'
    assert T[(0,tgt)] == expected, f'Expected answer = {expected}, your code returns {T[(0, tgt)]}'
    return 

print('--test 1--')
a1 = [1, 2, 3, 4, 5, 10]
print(a1, 15)
checkMemoTblTargetSum(a1, 15, 0)

print('--test 2--')
a2= [1, 2, 3, 4, 5, 10]
print(a2, 26)
checkMemoTblTargetSum(a2, 26, 1)

print('--test3--')
a3= [11, 23, 37, 48, 94, 152, 230, 312, 339, 413]
print(a3, 457)
checkMemoTblTargetSum(a3, 457, 1)

print('--test4--')
print(a3, 512)
checkMemoTblTargetSum(a3, 512, 0)

print('--test5--')
print(a3, 616)
checkMemoTblTargetSum(a3, 616, 1)
print('All tests passed (10 points)!')


# ## Part (C)
# 
# Modify your code in part B to record additional information so that you can recover the solution.
# Implement a function `getBestTargetSum(S, tgt)` that returns a new sub list `T` of `S` so that the sum of elements of `T` is less than or equal to `tgt` and is as close as possible to `tgt`.
# 

# In[45]:


def getBestTargetSum(S, tgt):
    k = len(S)
    assert tgt >= 0
    # your code here
    j = tgt
    i = 0
    Table = memoTargetSum(S, tgt)
    res = []
    
    while i < k:
        currentCell = Table[(i, j)]
        cellBelow = Table[(i + 1, j)]
        
        if currentCell != cellBelow:
            #Use S[i]
            res.append(S[i])
            j = j - S[i]
        
        i = i + 1
    
    return res  


# In[46]:


def checkTgtSumRes(a, tgt,expected):
    a = sorted(a)
    res = getBestTargetSum(a, tgt)
    res = sorted(res)
    print('Your result:' , res)
    assert tgt - sum(res)  == expected, f'Your code returns result that sums up to {sum(res)}, expected was {expected}'
    i = 0
    j = 0
    n = len(a)
    m = len(res)
    while (i < n and j < m):
        if a[i] == res[j]: 
            j = j + 1
        i = i + 1
    assert j == m, 'Your result  {res} is not a subset of {a}'


print('--test 1--')
a1 = [1, 2, 3, 4, 5, 10]
print(a1, 15)
checkTgtSumRes(a1, 15, 0)

print('--test 2--')
a2 = [1, 8, 3, 4, 5, 12]
print(a2, 26)
checkTgtSumRes(a2, 26, 0)

print('--test 3--')
a3 = [8, 3, 2, 4, 5, 7, 12]
print(a3, 38)
checkTgtSumRes(a3, 38, 0)

print('--test 4 --')
a4 = sorted([1, 10, 19, 18, 12, 11, 0, 9,  16, 17, 2, 7, 14, 29, 38, 45, 13, 26, 51, 82, 111, 124, 135, 189])
print(a4)
checkTgtSumRes(a4, 155, 0)
print('--test 5--')
checkTgtSumRes(a4, 189, 0)

print('--test 7--')
checkTgtSumRes(a4, 347, 0)

print('--test 8--')
checkTgtSumRes(a4, 461, 0)


print('--test 9--')
checkTgtSumRes(a4, 462, 0)


print('--test 9--')
checkTgtSumRes(a4, 517, 0)


print('--test 10--')
checkTgtSumRes(a4, 975, 3)

print('All Tests Passed (15 points)')


# ## That's All Folks!
