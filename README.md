# CSE408 ANSWERS

# Link of course:- https://www.coursera.org/learn/analysis-of-algorithms

# Analysis of Algorithm

## Week 1:- Analysis of Algorithm Graded Quiz:-

### Q.1 What is the order of growth of the solution to the Quicksort-like recurrence <br>F<sub>N</sub> = 2N + 1 + 1/N + &#x2211; <sub>1&#8804;K&#8804;N</sub> (F<sub>k - 1</sub> + F<sub>N - K</sub>) with F<sub>0</sub> = 0? <br> <br>1. 0<br>2. 1<br>3. 1/N<br>4. N<br>5. N log N<br>6. $ N^2$<br>7. $ N^3$<br><br> Answer:- 5. N log N

### Q.2 Which of the following is a drawback to analyzing algorithms by proving O- upper bounds on the worst case?<br><br> 1. Generally cannot be used to predict performance.<br>2. Input model may be unrealistic.<br>3. Generally cannot be used to compare algorithms.<br>4. Likely to be too much detail in the analysis.<br><br>Answer:- Option 1 & 3

### Q.3 What is the order of growth of the solution to the Quicksort-like recurrence <br>F<sub>N</sub> = N<sup>2</sup> + 1 + 1/N + &#x2211; <sub>1&#8804;K&#8804;N</sub> (F<sub>k - 1</sub> + F<sub>N - K</sub>) with F<sub>0</sub> = 0? <br> <br>1. 0<br>2. 1<br>3. 1/N<br>4. N<br>5. N log N<br>6. $N^2$<br>7. $N^3$<br><br> Answer:- 6. $N^2$


## Week 2:- Recurrence Pop Quiz On Telescoping:-

### Q.1 Solve the recurrence a<sub>n</sub> = na<sub>n - 1</sub> + n! for n > 0 with a<sub>0</sub> = 1. Give a simple expression for a<sub>n</sub> <br><br>1. (n + 1)!<br>2. 2n!<br>3. n!<br>4. (2n)!<br>5. n! + (n - 1)!<br><br> Answer:- 1. (n + 1)!


## Week 2:- Recurrence Pop Quiz On Master Theorem:-

### Q.1 Suppose that a<sub>n</sub> = 2a<sub>[n/3]</sub> + n for n > 2 with a<sub>0</sub> = a<sub>1</sub> = a<sub>2</sub> = 1. What is the order of growth of a<sub>n</sub> ?<br><br>1. O(n<sup>3</sup>)<br>2. O(n<sup>2</sup>)<br>3. O(n log n)<br>4. O(n)<br><br> Answer:- 4. O(n)


## Week 2:- Recurrence Graded Quiz:- 

### Q.1 Which of the following is true of the number of comparisons used by Mergesort?<br><br>1. Is less than N lg N + N/4 for all N<br>2. Order of growth is N lg N<br>3. Exactly N lg N when N is a power of 2<br>4. Has periodic behavior<br><br>Answer:- All options are correct

### Q.2 Suppose that na<sub>n</sub> = (n - 3)a<sub>n - 1</sub> + n for n > 2 with a<sub>0</sub> = a<sub>1</sub> = a<sub>2</sub> = 0. What is the value of a<sub>999</sub>?<br><br>Answer:- 250

## Week 3:- Generating Functions Quiz:- 

### Q.1 Which of these sequences is represented by the OGF ln 1/1 - z<sup>2</sup> ? <br><br>Answer:-  0 , 0 , 1/2 , 0 , 1/4 , 0 , 1/6

### Q.2 Which of these sequences is represented by the OGF z<sup>2</sup> &frasl; (1 - z<sup>3</sup>) ?<br><br> Answer:- 0 , 0 , 1 , 3 , 6 , 10 , ...

### Q,3 Which of these sequences is represented by the OGF 3 &frasl; ( 1 - z ) ?<br><br> Answer:- 3, 3, 3, 3, 3, ...

### Q.4 Which of these sequences is represented by the OGF 1 &frasl; ( 1 - 3z) ? <br><br> Answer:- 1, 3, 9, 27, 81, 243, ...

### Q.5 Suppose that a<sub>n</sub> = 9a<sub>n - 1</sub> - 20a<sub>n - 2</sub> for n > 1 with a<sub>0</sub> = 0 and a<sub>1</sub> = 1. What is the value of lim<sub>n -> &#8734;</sub> a<sub>n</sub> / a<sub>n - 1</sub> ? <br><br> Answer:- 5

### Q.6 What is the value of &#x2211;<sub>0&#8804;k&#8804;n</sub>(<sup>2k</sup>&frasl;<sub>k</sub>)(<sup> 2n-2k </sup> &frasl; <sub> n-k </sub>) ?<br><br> Answer:- 4<sup>n</sup>

## Week 4:- Asymptotics

### Q.1 Give an asymptotic approximation of e<sup>H<sub>2N</sub></sup> to within O ( 1 &frasl; N<sup>2</sup> ) <br><br> Answer:- 2 - 1 &frasl; 2N + O ( 1 &frasl; N<sup>2</sup> )

### Q.2 Which of the following has approximate value 1.62889? <br> <br>Answer:- 1.05<sup>10</sup>

## Extra Question

### Q.1 Match each function with an asymptotic expansion.
| Functions | Asymptotic expansion |
|----------|----------|
| H<sub>N</sub> | ln N + γ + 1 &frasl; 2N + O( 1 &frasl; N<sup>2</sup>) |
| exp(H<sub>2N</sub> - H<sub>N</sub>) - 1 | 1 - 1 &frasl; 2N + O( 1 &frasl; N<sup>2</sup>) |
| exp(H<sub>N</sub>) | N + O(1) |
| exp( 1 &frasl; N) | 1 + 1 &frasl; N + O( 1 &frasl; N<sup>2</sup>) |
| (1 + 1 &frasl; N)<sup>-1</sup> | 1 - 1 &frasl; N + O( 1 &frasl; N<sup>2</sup>) 


### Q.2 Match each expression with an approximation to its value.
| Expression | value |
|----------|----------|
| 1.01<sup>10</sup> | 1.10462 |
| 1.05<sup>10</sup> | 1.62889 |
| 1.01<sup>20</sup> | 1.22019 |
| 1.01<sup>50</sup> | 1.64463 |
| 1.01<sup>100</sup> | 2.70481 |

## Week 5:- Analytic Combinatorics

### Q.1 Which of these constructions defines the set of all binary strings?<br><br>Answer:- B = E + (Z<sub>0</sub> - Z<sub>1</sub>) X B

### Q.2 What is the approximate value of [z<sup>n</sup>] 1 &frasl; (1 - 2z)(1 - 3z) ? <br><br>Answer:- 3<sup>n+1</sup>

## Extra Question

### Q.1 Match each combinatorial class with a construction.
| Expression | value |
|----------|----------|
| binary strings | B = E + ( Z<sub>0</sub> + Z<sub>1</sub> ) X B |
| binary strings with no 01 | E + ( Z<sub>0</sub> + Z<sub>1</sub> ) X B = B + ( Z<sub>0</sub> + Z<sub>1</sub> ) X B  |
| binary strings with no 11 | B = E + Z<sub>1</sub> + ( Z<sub>0</sub> + Z<sub>1</sub> X Z<sub>0</sub> ) X B |
| binary strings with no 001 | E + B X ( Z<sub>0</sub> + Z<sub>1</sub> ) = B + B X ( Z<sub>0</sub> X Z<sub>0</sub> X Z<sub>1</sub> ) |
| binary strings with no 00 | B = E + Z<sub>0</sub> + ( Z<sub>1</sub> + Z<sub>0</sub> X Z<sub>1</sub> ) X B |

### Q.2 Match each expression with an approximate value.
| Expression | value |
|----------|----------|
| [ z<sup>n</sup> ] 1 &frasl; $\sqrt{ 1 - 3z }$ | 3<sup>n</sup> &frasl; $\sqrt{ &pi; n}$ |
| [ z<sup>n</sup> ] 1 &frasl; $\sqrt{ 1 - 3z }$ ln 1 &frasl; 1 - 2z | 3<sup>n</sup> ln 3 &frasl; $\sqrt{ &pi; n}$ |
| [ z<sup>n</sup> ] 1 &frasl; ( 1 - 2z ) ( 1 - 3z ) | 3<sup>n + 1 </sup> |
| [ z<sup>n</sup> ] 1 &frasl; $\sqrt{ 1 - 2z }$ | 2<sup>n - 1</sup> &frasl; n |
| [ z<sup>n</sup> ] 1 &frasl; 1 - 3z ln 1 &frasl; 1 - 2z | 3<sup>n</sup> ln 3 |



## Week 6:- Trees Quiz

### Q.1 Which of the following constructions defines the Motzkin (unary-binary) trees?<br><br>Answer:- M = Z + Z X M + Z X M X M

### Q.2 Of the following, which are the least numerous, for a given (large) number of nodes?<br><br>Answer:- unordered trees

### Q.3 Of the following, which are the most numerous, for a given (large) number of nodes?<br><br>Answer:- 3-ary trees

## Week 7:- Permutations

### Q.1 Of the following, which is the best approximation to the probability that a permutation of size N has exactly 1 cycle?<br><br>Answer:- 1 &frasl; N

### Q.2 Which event is leastlikely, in a random permutation of size 1000?<br><br>Answer:- It has no cycles of length less than 5.

### Q.3 Of the following, which is the best approximation to the probability that a permutation of size N has exactly 3 cycle?<br><br>Answer:- ln N / N<sup>2</sup>

### Q.4 Of the following, which is the best approximation to the probability that a permutation of size N has exactly 2 cycle?<br><br>Answer:- ln N / N

### Q.5 Which event is mostlikely, in a random permutation of size 1000?<br><br>Answer:- It has no cycles of length 1, 2, 3, or 7.

## Week 8:- Strings and Tries

### Q.1 Which of the following is the OGF defining the bitstrings not containing 01010?<br><br>Answer:- 1 + z<sup>2</sup> + z<sup>4</sup> &frasl; z<sup>5</sup> + (1 - 2z)(1 + z<sup>2</sup> + z<sup>4</sup>)

### Q.2 Which of the following patterns has a longer expected wait time in a random bitstring than any of the others?<br><br>Answer:- 00000

### Q.3 Which of the following patterns has a shorter expected wait time in a random bitstring than any of the others?<br><br>Answer:- 00001


## Week 9:- Strings and Words

### Q.1 Which of the following constructions defines birthday sequences?<br><br>Answer:- SEQ<sub>M</sub>(E+Z)

### Q.2 Which of the following EGFs define random mappings with no singleton cycles, as a function of the Cayley function C(z) = ze<sup>C(z)</sup>?<br><br>Answer:- e<sup>-C(z)</sup> &frasl; ( 1 - C(z) )

### Q. Which of the following constructions defines words?<br><br>Answer:- SEQ<sub>M</sub>(SET(Z))


# Link of course:- https://www.coursera.org/learn/algorithms-on-strings

# Algorithms on Strings

## Week 1:- Tries and Suffix Trees

### Q.1 What is the tightest estimate you can prove on the memory consumption of a trie built off n non-empty patterns p<sub>1</sub>, p<sub>2</sub>,..., p<sub>n</sub> if all the patterns' lengths are bounded from above by L, and the sum of lengths of all patterns is no more than S?<br><br>Answer:- O(S)

### Q.2 What is the time complexity of searching all occurrences of n patterns p<sub>1</sub>, p<sub>2</sub>,..., p<sub>n</sub> in text T of length |T| if all patterns have length at most L  and the sum of their lengths is at most S?<br><br>Answer:- O(|T|L)

### Q.3 What is the smallest possible number of nodes in a trie built off n patterns p<sub>1</sub>, p<sub>2</sub>,..., p<sub>n</sub> if all the patterns have the same length L > 0 ?<br><br>Answer:- L + 1

### Q.4 If you take all the suffixes of a string S of length L and build a regular trie off those suffixes as patterns, what is the maximum possible number of nodes in such trie?<br><br>Answer:- L( L + 1 ) &frasl; 2 + 1

### Q.5 What is the smallest possible number of nodes in a suffix tree of string S with length L?<br><br>Answer:- L + 1

## Programming Assignment 1

### Please go to the Algorithms on Strings folder then click on week 1 then click on programming assignmnet 1 there are some files download that and upload that files in the assignment exercise with their respective names.<br><br>Algorithms On String Folder > Week 1 > Programming Assignment 1 > Download Files > Upload Files

## Week 2:- Burrows-Wheeler Transform and Suffix Arrays

### Q.1 What is the length of BWT(S) for a string S of length L?<br><br>Answer:- L

### Q.2 What is the time complexity of the algorithm from the lectures used to build BWT(S) for a string S of length L?<br><br>Answer:- O(L)

### Q.3 What is the time complexity of the algorithm from the lectures to build the inverse Burrows-Wheeler Transform of a string S of length L?<br><br>Answer:- O(L)

### Q.4 What is the time complexity of the algorithm from the lectures to build a suffix array of a string S of length l?<br><br>Answer:- O(L<sup>2</sup>)

## Programming Assignment 2

### Please go to the Algorithms on Strings folder then click on week 2 then click on programming assignmnet 2 there are some files download that and upload that files in the assignment exercise with their respective names.<br><br>Algorithms On String Folder > Week 2 > Programming Assignment 2 > Download Files > Upload Files


## Week 3:- Exact Pattern Matching

### Q.1 For the Brute Force algorithm (from this lecture) matching some Pattern against the Text AAAAAAAAAT, which of the Patterns below will require the maximum number of comparisons throughout the whole algorithm?<br><br>Answer:- AAAA

### Q.2 You've just tried to match the Pattern AACTAACAT against some Text starting from position 3 and you know that AACTAAC is the longest common prefix of the Pattern and the suffix of the Text starting in position 3:<br><br>???AACTAAC????????????????  AACTAACAT<br><br>What is the maximum amount by which you can shift the Pattern to the right without missing an occurrence of the Pattern in the Text?<br><br>Answer:- 4

### Q.3 What are the values of the prefix function for the string AC AT AC AT AC AC A?<br><br>Answer:- [ 0, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 2, 3 ]

### Q.4 What is the total number of times that the condition of the while loop will be checked in this pseudocode for ComputePrefixFunction if we call it for the string AC AT AC AT AC AC A?<br><br> ![Image](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/sMiFcU9TEealpAoth2FRAw_39b3af46e66f818d7c34435d33a09b2d_pseudocode_prefix_function.png?expiry=1707091200000&hmac=9rI5hV8JaOiyUP_pyoxf8SJkr9wlkru3qD5wrChgARg) <br><br>Answer:- 15

## Week 4:- Suffix Array Construction

### Q.1 For the string S=AACGATAGCGGTAGA$, what will be the contents of array order after SortCharacters?<br><br>Answer:- [ 15,0,1,4,6,12,14,2,8,3,7,9,10,13,5,11 ] 

### Q.2 For string S=AACGATAGCGGTAGA$, what will be the contents of the array class after ComputeCharClasses?<br><br>Answer:- [1,1,2,3,1,4,1,3,2,3,3,4,1,3,1,0]

### Q.3 For string S=AACGATAGCGGTAGA$, what will be the order of cyclic shifts of length 2 ordered by the second character in ascending order?<br><br>Answer:- A$,$A,AA,GA,TA,TA,GA,AC,GC,CG,AG,CG,GG,AG,AT,GT

### Q.4 For string S=AACGATAGCGGTAGA$, what will be the order of cyclic shifts of length 2 after SortDoubled with L = 1?<br><br>Answer:- [15,14,0,1,6,12,4,2,8,3,13,7,9,10,5,11]

### Q.5 For string S=AACGATAGCGGTAGA$, what will be the contents of the array class for the cyclic shifts of length 2 after UpdateClasses?<br><br>Answer:- [2,3,6,7,5,11,4,8,6,9,10,11,4,7,1,0]  

### Q.6 For string S=AACGATAGCGGTAGA$, what will be the suffix array?<br><br>Answer:- [15,14,0,1,12,6,4,2,8,13,3,7,9,10,11,5]  

## Programming Assignment 3

### Please go to the Algorithms on Strings folder then click on week 4 then click on programming assignmnet 3 there are some files download that and upload that files in the assignment exercise with their respective names.<br><br>Algorithms On String Folder > Week 4 > Programming Assignment 3 > Download Files > Upload Files


# Link of course:- https://www.coursera.org/learn/dynamic-programming-greedy-algorithms

# Dynamic Programming, Greedy Algorithms

## Week 1:- Max Subarray Problem

## Note:- We have to complete till Karatsuba's Multiplication Algorithm for week 5 according to our IP

### Q.1 Consider the array with numbers that is input to the max subarray problem<br> [1, 19, 5, -4, 7, 18, 15, -10 ]<br>Select all true facts from the list below making sure that no incorrect choices are selected.<br><br>Answer:-<br> 1. The output to the max subarray .problem should be 18-(-4) =22<br>2. The divide and conquer algorithm will compute the result of max subarray problem on the first half of the array, which in this instance yields the value 18<br>3. The divide and conquer algorithm will compute the result of max subarray problem on the second half of the array, which in this instance yields the value 11<br>4. The minimum element of the first half of the array is -4 and maximum element of the second half of the array is 18. These in turn form the result for the max subarray problem which is 22.

### Q.2 Consider the recurrence that represents the running time for the max subarray problem:<br>T(n) = &#123; &Theta;(1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n &#8804; 2<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2T(n &frasl; 2) &nbsp;&nbsp;&nbsp;&nbsp;Otherwise<br><br>Answer:-<br>1. The case when n &#8804; 2 represents the constant amount of work needed to find the max subarray for input arrays of size 1 or 2.<br>2. The recurrence assumes that n is a power of two, since repeated division by 2 can yield fractional results otherwise.<br>3. The &theta; (n) term in the recurrence for n> 2 represents the work to find minimum of first half and maximum of second half.<br>4. The recurrence and the running time are identical to that obtained for the mergesort algorithm covered earlier in course 1 of this specialization.

## Week 1:- Karatsuba's Multiplication Algorithm

### Q.1 The following questions concern the binary representation of numbers and addition. Note that we will write binary numbers as b<sub>n</sub>, ..., b<sub>0</sub> where b<sub>n</sub> is the most significant bit whereas b<sub>0</sub> is the least significant bit. However, represented as a list in the computer, the same number would be [b<sub>0</sub>, b<sub>1</sub>, ... , b<sub>n</sub>].<br><br>Answer:- <br>1. The number 6 in decimal is represented by the list [0, 1, 1]<br>2. Consider two lists [0, 1, 1] and [1, 1]. The sum of these two numbers is given by [1, 0, 0, 1]<br>3. The addition of a m bit number with a n bit number yields a number with as many as max (m, n) + 1 bits.<br>4. The algorithm for adding two n bit numbers runs in time &theta; (n).

### Q.2 The following questions concern the grade school algorithm we studied in the lecture. Note that we will represent numbers as lists of bits. Select all the correct answers from the list below.<br><br>Answer:- <br>1. The grade school multiplication algorithms performs as many additions as the number of 1 bits in the second argument.<br>2. The shift operation performed at each step of the multiplication algorithm appends a 0 to the beginning of the list.<br>3. Consider the multiplication of two numbers represented by list a = [1, 0, 1] with b = [1, 1]. The grade school multiplication algorithm performs additions of the number [1, 0, 1,0] with the number [0, 1, 0, 11, yielding the result [1, 1, 1, 1]. Note the number a<sub>n</sub> ... a<sub>0</sub> is represented as a list [ a<sub>0</sub>, a<sub>1</sub>, ... , a<sub>n</sub> ].

### Q.3 The following question concerns the multiplication of two n bit numbers a and b represented by the lists using the divide and conquer scheme presented in the lecture.<br>[ a<sub>0</sub>, ..., a<sub>n - 1</sub> ] and [ b<sub>0</sub>, ..., b<sub>n - 1</sub> ]<br>For any list of bits l, the number denoted by the list is denoted by [[l]]. Assume that n is a power of 2 and let m = n &frasl; 2.<br><br>Answer:- <br>1. The number denoted by the list [ a<sub>0</sub>, ..., a<sub>n - 1</sub> ] can be written as [[  [ a<sub>0</sub>, ..., a<sub>m - 1</sub> ] ]] + 2<sup>m</sup> [[  [ a<sub>m</sub>, ..., a<sub>n - 1</sub> ] ]]<br>2. Karatsuba multiplication of two n bit numbers makes three recursive calls with two of the calls involving multiplication of m bit numbers and one call involving multiplication of at most m + 1 bit number.<br>3. Depending on the implementation details and the computer on which we run, there is a cutoff value of n such that for all inputs with greater than in bits, the worst case running time of Karatsuba's algorithm will outperform the worst case running time of grade school multiplication.

## Week 1:- Master Method

### Q.1 Consider a recurrence of the form :<br> T(n) = &#123; &Theta;(1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n  &#8804;  1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#123;3T(n/3) + &Theta;(n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; otherwise<br>Select all the correct options from the list below.<br><br>Answer:-<br> 1) The recurrence above can be obtained from a divide and conquer scheme that divides inputs of size n into 3 subparts of size n/3 each.<br>2) Master method is applied with a = 6 = 3 and 1. Case-2 applies and the overall complexity is T(n) = &Theta;(n<sup>log<sub>3</sub></sup><sup>(3)</sup> log(n)) = &Theta;(nlog(n)).

### Q.2 Consider a recurrence of the form :<br> T(n) = &#123; &Theta;(1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n  &#8804;  1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#123;2T(n/3) + &Theta;(&#8730;n)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; otherwise<br>Select all the correct options from the list below.<br><br>Answer:- <br>1) The recurrence denotes a divide and conquer scheme wherein the divide and combine steps take &Theta;(&#8730;n) time in total;<br>2) Master method is applied with a = 2 and b = 3. We have log<sub>b</sub>(a) = log<sub>3</sub>(2) which is a number between 0 and 1 but is greater than half.<br>3) Case-1 of the master method applies and the complexity of the algorithm is &Theta;(n<sup>log<sub>3<sub></sup><sup>(2)</sup>).

## Week 1:- Complex Numbers and Roots of Unity

### Q.1 Select all the correct facts about complex numbers from the list below.<br><br>Answer:- <br>1. The complex number 3 + 4j has modulus 5.<br>2. The conjugate of the complex number re<sup>j&Theta;</sup> is given by re<sup>-j&Theta;</sup><br>3. The complex number j is one of the fourth roots of unity.<br>4. For any complex number z, the numbers z + z&#x0305; and z &#215; z&#x0305; are both real numbers.<br>5. The value of 1 &frasl; 1 + j is 1 &frasl; 2 (1 - j).

### Q.2 Let w<sub>n</sub> denote the generator of the n<sup>th</sup> roots of unity for n &#8805; 1. Select all the correct options from the list below.<br><br>Answer:- <br>1. w<sub>n</sub> = cos(2&Pi; &frasl; n) + jsin(2&Pi; &frasl; n)<br>2. w<sub>n</sub><sup>n - 1</sup> = w&#x0305;<sub>n</sub> = 1 &frasl; w<sub>n</sub><br>3. Iin is even and n &#8805; 2 then w<sup>2</sup><sub>n</sub> = w<sub>n / 2</sub><br>4. For any 0 &#8804; k &#60; n e have w<sub>n</sub><sup>k</sup> = w&#x0305;<sub>n</sub><sup>n-k</sup> = 1 &frasl; w&#x0305;<sup>k</sup><sub>n</sub><br>5. 1 + w<sub>n</sub> + w<sup>2</sup><sub>n</sub> + ... + w<sup>n-1</sup><sub>n</sub> = for all n &#8805; 2
