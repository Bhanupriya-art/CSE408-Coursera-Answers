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

### Q.2 Let w<sub>n</sub> denote the generator of the n<sup>th</sup> roots of unity for n &#8805; 1. Select all the correct options from the list below.<br><br>Answer:- <br>1. w<sub>n</sub> = cos(2&Pi; &frasl; n) + jsin(2&Pi; &frasl; n)<br>2. w<sub>n</sub><sup>n - 1</sup> = w&#x0305;<sub>n</sub> = 1 &frasl; w<sub>n</sub><br>3. If n is even and n &#8805; 2 then w<sup>2</sup><sub>n</sub> = w<sub>n / 2</sub><br>4. For any 0 &#8804; k &#60; n we have w<sub>n</sub><sup>k</sup> = w&#x0305;<sub>n</sub><sup>n-k</sup> = 1 &frasl; w&#x0305;<sup>k</sup><sub>n</sub><br>5. 1 + w<sub>n</sub> + w<sup>2</sup><sub>n</sub> + ... + w<sup>n-1</sup><sub>n</sub> = for all n &#8805; 2

## Week 1:- FFT Algorithm and Applications

### Q.1 Consider a sequence [ a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> ]. Let [ A<sub>0</sub>, A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub> ] be the discrete fourier transform of this sequence.<br>Select all the correct options below.<br><br>Answer:- <br>1. The 4th roots of unity are {1, j, -1, -j}.<br>2.  A<sub>0</sub> = a<sub>0</sub> + a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub>.<br>3. The DFT can be viewed as evaluating the polynomial a(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + a<sub>3</sub>x<sup>3</sup> for x = 1,j, -1 and - j respectively.<br>4. A<sub>2</sub> = a(-1) =  a<sub>0</sub> - a<sub>1</sub> + a<sub>2</sub> - a<sub>3</sub>.<br>5. A<sub>1</sub> andd A<sub>3</sub> must be complex conjugates of each other as long as the sequence a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> consist of real numbers.<br>6. A<sub>0</sub> and A<sub>2</sub> must always be real numbers as long as the sequence a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub> consist of real numbers.

### Q.2 Let a<sub>0</sub>,...,a<sub>511</sub> be a sequence of real numbers obtained from sampling wind velocity with 8 samples per minute over 64 minutes (roughly 1 hour).<br>Suppose we compute the DFT and obtain the sequence [ A<sub>0</sub>,...,A<sub>n-1</sub> ]as the DFT coefficients.<br><br>Answer:- <br>1. A<sub>0</sub> = &#8721; $\_{j=0}^{511} a_j$.<br>2. A<sub>256</sub> = a<sub>0</sub> - a<sub>1</sub> + a<sub>2</sub> - a<sub>3</sub> + ... + a<sub>510</sub> - a<sub>511</sub><br>3. A<sub>128</sub> corresponds to the frequency: 8 &#215; 128 &frasl; = per minute = 2/minute.<br>4. The highest frequency component is A<sub>256</sub> which corresponds to a frequency of 4/minute.<br>5. The reason we assign negative frequencies to components A<sub>j</sub> for j &#62; n &frasl; 2 is because they correspond to roots of unity $w_n^j$ which can be seen as "rotating" in clockwise direction (opposite direction to roots $w_n^j$ for j &#8804; n &frasl; 2.

## Week 1:- Problem Set 1

### For the problem set 1 you need to go the Dynamic Programming, Greedy Algorithms Folder in that folder go to Week 1 Folder then there there is a file named "Problem Set 1.py". In that file there are question and the code blocks in which some code is written you can directly copy paste the code accordingly.<br><br>  

Dynamic Programming, Greedy Algorithms Folder -> Week 1 -> Open Problem Set 1.py -> Then in Problem Set 1 module click on Launch Lab -> Then Copy & Paste code accordingly -> Then Submit your assignment.

## Week 2:- Rod Cutting Problem and Recurrence (Practice Quiz)

### Q.1 Consider the rod cutting problem with the following price table:<br>
| Length | Price |
|----------|----------|
| 2 | 1.9 |
| 3 | 2.2 |
| 5 | 4.2 |
### Assume that "wasting" earns no revenue. <br>We have a rod of length L = 11. Choose all the correct facts below.<br><br>Answer:- The optimal solution involves 1 cut of length 5 and 3 cuts of length 2.

### Q.2 Consider the rod cutting problem with the following price table:
| Length | Price |
|----------|----------|
| 2 | 1.9 |
| 3 | 2.2 |
| 5 | 4.2 |
### Assume that "wasting" earns a penalty that is −1 × waste length<br>Let maxRev(L) denote the maximum revenue obtainable from a rod of length L with the price table fixed above. Fill in the missing portions of the recurrence below:<br>maxRev(L) = &#123; ?<sub>1</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; L < 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#123; ?<sub>2</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; L = 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#123; max (?<sub>3</sub>, maxRev(L - 2)+?<sub>4</sub>, maxRev(L - 3)+?<sub>5</sub>, maxRev(L - 5)+?<sub>6</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;otherwise<br><br>Answer:- <br>1. ?<sub>2</sub> should be 0<br>2. ?<sub>4</sub> should be 1.9<br>3. ?<sub>6</sub> should equal the revenue of a cut of length 5.

## Week 2:- Memoization

### Q.1 Consider the rod cutting problem with the following price table:
| Length | Price |
|----------|----------|
| 2 | 1.9 |
| 3 | 2.2 |
| 5 | 4.2 |
### Assume that "wasting" earns no revenue.<br>We have a rod of length L = 9.<br>Using the recurrence, we will fill out the memo table T below for the rod cutting problem for length L  = 9 
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 0 |
### Answer:- <br>1. T[1] = 0<br>2. T[2] = 1.9<br>3. T[3] = max(0, T[0] + 2.2, T[1] + 1.9, T[-2] + 4.2)<br>4. T[j] = max(0, T[j - 2] + 1.9, T[j - 3] + 2.2, T[j - 5] + 4.2)with T[j] = -&#8734; for j < 0

## Week 2:- Coinchanging Problem

### Q.1 Consider we wish to compute change for 48 cents given coins of denomination<br>{ 2, 5, 10, 20} cents. We design two tables<br><br>Tbl[j] that records the best solution in terms of number of coins for j cents.<br>S[j] that records the "first" coin denomination that we need to use for obtaining the solution for Tbl[j]<br>Select all the correct facts from the list below.<br><br>Answer:-<br>1. Tbl[j] = min(1 + Tbl[j - 2], 1 + Tbl[j - 5], 1 + Tbl[j - 10], 1 + Tbl[j - 20])<br>2. Tbl[3] = &#8734; denoting that we cannot make change for 3 cents using the given denominations.<br>3. Suppose we wish to recover the solution, let S[48] have the value 20 after we finish implementing the memoization. The solution recovery will add a 20 cent coin to our solution list and look up S[28]

### Q.2 Consider the usual solution that people use to make change for target T.<br><br>-Take the largest denomination coin that is &#8804; T let it be c<sub>j</sub>.<br>-Give c<sub>j</sub> and recursively make change for T - c<sub>j</sub>.<br>-Stop when the remaining change is 0.<br>Consider the denominations {1,2,5,10,20,25} cents.<br><br>Answer:-<br>1. Suppose we wish to make change for 50 cents, our approach will provide two 25 cent coins as change, which is optimal.<br>2. The algorithm makes optimal decision for T = 49, using four coins: one 25 cent, one 20 cent and two 2 cent coins.

## Week 2:- Knapsack Problem

### Q.1 Throughout this quiz consider a knapsack problem with three items 
| Item | Value | Weight |
|------|-------|--------|
| I<sub>1</sub> | v<sub>1</sub> | w<sub>1</sub> |
| I<sub>2</sub> | v<sub>2</sub> | w<sub>2</sub> |
| I<sub>3</sub> | v<sub>3</sub> | w<sub>3</sub> |
### Once again we wish to maximize the total value of our steal while keeping weights under limit W. However,  for each item we can steal arbitrarily many copies of that item. For instance, if we steal item I<sub>2</sub> 5 times, we have a value of 5v<sub>2</sub> and weight 5w<sub>2</sub>. There is no limit on the number of times an item can be stolen.<br><br>Assume w<sub>j</sub> > 0 for each item: otherwise, we can take infinitely many copies of the items and the problem becomes undefined.<br><br>Answer:- This sort of situation can happen if I<sub>j</sub> is a stock where we can invest in 0 or more units of the stock I<sub>j</sub>.

### Q.2 Refer to the problem introduced in the previous question.<br><br>Let maxValue(j, W) be the maximum value obtained for considering items I<sub>j</sub>,...,I<sub>3</sub>  and weight limit W.<br>Note that 1 &#8804; j &#8804; 4. In particular for j = 4, we obtain the empty list of items.<br><br>Select all the correct facts from the choices below.<br><br>Notation [a &frasl; b] is the value by computing a &frasl; b and rounding it down when a,b > 0.<br><br>Answer:-<br>1. The minimum number of times we can choose item I<sub>j</sub> is 0 and maximum number of times is [ W &frasl; w<sub>j</sub> ]<br>2. maxValue(4, W) = 0 whenever W &#8805; 0.<br>3. If the thief chose to steal item I<sub>j</sub>, K &#8805; 0 times, the remaining weight budget is W - kw<sub>j</sub> and value obtained is kv<sub>j</sub>.

## Week 2:- Longest Common Subsequence

### Q.1 Consider two strings:<br><br>s1 = "ATTCCGGAC" and s2 = "TTACGG"<br><br>We wish to find the longest common substring between these two strings.<br><br>Answer:-<br>1. The longest common substring is of length 5: "TTCGG"<br>2. Suppose we have committed to matching the second character "T" in s1 to the first character s2,  the remaining decision is to optimally find the LCS for the suffix: TCCGGAC and TACGG

### Q.2 Consider strings s1: ATCCG and s2: CACGC<br><br>We construct a memo table which for your convenience is labeled with the characters in strings s1 and s2
| | C | A | C | G | C | |
|-|---|---|---|---|---|-|
| A | | | | | | 0 |
| T | | | | | | 0 |
| C | | | ??7 | ??5 | ??6 | 0 |
| C | | | | ??4 | ??3 | 0 |
| G | | | | ??2 | ??1 | 0 |
| | 0 | 0 | 0 | 0 | 0 | 0 |
### Write down the values that will be filled in for the positions labeled with ??1 - ??7 in the memo table above and use those to select the correct answers below.<br><br>Answer:-<br>1. ??1 = 0<br>2. ??2 = 1<br>3. ??3 = 1<br>4. ??4 = max(??3, ??2)<br>5. ??7 = ??4 + 1<br>6. ??7 = 2

## Week 2:- Problem Set 2

### For the problem set 2 you need to go the Dynamic Programming, Greedy Algorithms Folder in that folder go to Week 2 Folder then there is a file named "Problem Set 2.py". In that file there are question and the code blocks in which some code is written you can directly copy paste the code accordingly.<br><br>  

Dynamic Programming, Greedy Algorithms Folder -> Week 2 -> Open Problem Set 2.py -> Then in Problem Set 2 module click on Launch Lab -> Then Copy & Paste code accordingly -> Then Submit your assignment.

## Week 3:- Greedy Algorithms(Practice Quiz)

### Q.1 Consider once again the coin changing problem with denominations: {1, 2, 5, 10} cents.<br><br>Answer:-<br>1. The greedy coin changing algorithm when applied to make change for 18 cents will utilize 4 coins.<br>2. If we added a 8 cent coin to our set of denominations, the greedy algorithm will not be an optimal algorithm for making change with the least number of coins.

### Q.2 Consider a version of knapsack problem for a perfumer who has an empty perfume bottle with volume V = 10 ml and would like to mix ingredients in various proportions to maximize the total profit which is simply calculated by summing up the profit/unit volume of each ingredient times the volume of the ingredient used.
| Liquid | Profit/Unit Volume | Available Amount |
|--------|--------------------|------------------|
| A | 1.5 $/ml | 10 ml |
| B | 2.2 $/ml | 4 ml |
| C | 3.3 $/ml | 3 ml |
| D | 2.1$/ml | 5 ml |
| E | 1.7 $/ml | 2 ml |
### Answer:-<br>1. The optimal solution would be to fill up 3 units of C, 4 units of B, and 3 units of D yielding a total profit of 3 x 3.3 + 4 x 2.2 + 3 x 2.1 = 25 dollars.<br>2. For solving problems like this, a greedy strategy would be to first take as many units of ingredient C as possible since that has the most profit per unit volume.

## Week 3:- Greedy Interval Scheduling

### Q.1 In this lecture, we saw how greedy algorithms were optimal for interval scheduling when our goal is to maximize the number of meetings held. Suppose we have the same problem setup of meetings with start/end times specified and our goal was to improve the overall room utilization : i.e, the amount of time the room is occupied in a meeting rather than the number of meetings.<br><br>Answer the following questions below by selecting the correct facts.<br><br>Answer:-<br>1. Suppose we design a greedy algorithm that first schedules the longest meeting, deletes all the conflicting meetings and recursively solves the remaining sub problem, this algorithm is not optimal in terms of total occupancy.<br>2. The greedy algorithm used to maximize the number of meetings held will not necessarily maximize the total time the room is occupied by a meeting.<br>3. Suppose all meetings are of the same duration then maximizing the number of meetings is equivalent to maximizing the total time utilized by the meetings.


## Week 3:- Huffman Codes

### Q.1 Consider a large document with 5 letters {A, B, C, D, E} and the following percentages of occurrence for each of the five letters:
| Letters | fraction of occurrence |
|---------|------------------------|
| A | 35% |
| B | 25% |
| C | 20% |
| D | 15% |
| E | 5% |

### Consider how many bits each character gets allocated by a Huffman code:
| Letters | # bits |
|---------|------------------------|
| A | b<sub>A</sub> |
| B | b<sub>B</sub> |
| C | b<sub>C</sub> |
| D | b<sub>D</sub> |
| E | b<sub>E</sub> |

### Select all the correct answers from the list below about the Huffman code generated for this example.<br><br>Answer:-<br>1. The construction of Huffman code will first merge D and E into a subtree.<br>2. b<sub>A</sub> = b<sub>B</sub> = 2<br>3. b<sub>C</sub> = 2<br>4. The average number of bits per character for the Huffman code is  2.2 bits/character

## Week 3:- Problem Set 3

### For the problem set 3 you need to go the Dynamic Programming, Greedy Algorithms Folder in that folder go to Week 3 Folder then there is a file named "Problem Set 3.py". In that file there are question and the code blocks in which some code is written you can directly copy paste the code accordingly.<br><br>  

Dynamic Programming, Greedy Algorithms Folder -> Week 3 -> Open Problem Set 3.py -> Then in Problem Set 3 module click on Launch Lab -> Then Copy & Paste code accordingly -> Then Submit your assignment.

```
Note:- A video Tutorial has also been added to the same Dynamic Programming, Greedy Algorithms folder.
Named as "Tutorial for Problem Set 3.MOV" In week 3 for problem set 3. If anyone is facing any issue related
to do how to do week 3 problem set, then they can refer to that video.
```


## Week 4:- Decision Problems and Languages

### Q.1 Select all the correct facts from the list be low.<br><br>Answer:-<br>1. Consider the language L = { 0, 10, 100, 110, ... } of binary encodings of all even numbers. An algorithm that recognizes L is also an algorithm that given a number returns true if even and false if odd.<br>2. Consider the problem of finding if a graph G is strongly connected (i.e, entire graph is a single SCC). The corresponding language is L = { < G > | G is a graph that is strongly connected }<br>3. It is possible to encode graphs as binary strings of 0s and 1s such that every graph G corresponds to a unique binary string.

## Week 4:- Polynomial Time and Certificates

### Q.1 Select all the problems for which we know of an efficient polynomial time algorithm through techniques studied thus far in this specialization.<br><br>Answer:-<br>1. Given a weighted graph G, does there exist a negative weight cycle?<br>2. Given a graph is there a spanning tree whose weight is less than K?<br>3. Given an array a of size  n and a number k, are there more than n/4 elements which are >= k?

### Q.2 Select all the correct answers regarding certificates from the list below.<br><br>Answer:-<br>1. Given a number n  that is known to be a product of two large prime numbers (such numbers are used extensively in cryptography), we wish to find out the kth bit of its smallest prime factor. The certificate is the prime factor p itself.<br>2. Let G be a weighted directed graph and s,t be two vertices of G. We wish to know if there a path from s to t of length ≤ W. The empty string can be a certificate for this problem that can be checked in polynomial time.<br>3. Let G be an undirected graph. We wish to know if there is a cycle that visits all vertices of G exactly once. The certificate for a yes answer is given by the cycle itself

## Week 4:- NP Completeness Reductions

### Q.1 Suppose problem A reduces in polynomial time to problem B. Let us suppose that problem B cannot be solved in polynomial time. Does it mean that A cannot also be solved in polynomial time?<br><br>Answer:- No, it is possible that there is some other "more ingenious" way of solving A in polynomial time that does not involve a reduction to B.

### Q.2 True of False: Every problem in P can be reduced in polynomial time to the k-clique problem of checking if a given graph G has  a clique  of size at least k.<br><br>Answer:- True: every problem P is trivially in NP and by Cook-Levin theorem all problems in NP can be reduced to 3-SAT and we saw in the lecture that 3-SAT was reduced in polynomial time to the k-clique problem.

### Q.3 Suppose we have a polynomial time reduction from problem A to problem B, select all the true facts from the list below.<br><br>Answer:-<br>1. If there is no algorithm that can solve A in polynomial time, then there is no algorithm that can solve B in polynomial time.<br>2. If A is NP complete and B is in NP, then B is also NP complete.

### Q.4 Suppose we wish to prove the travelling salesperson problem (TSP) discussed in the lecture is NP complete. Which of the following steps will be needed to do so?<br><br>Answer:-<br>1. We will need to show that TSP is in NP by showing that the yes answer comes with a certificate that can be checked in polynomial time.<br>2. We need to reduce 3-SAT or a previously known NP complete problem to the TSP in polynomial time.<br>3. A reduction from 3-SAT to TSP, will take a boolean 3-CNF-SAT formula and create a weighted graph G that is an instance of TSP.

## Week 4:- NP Completeness Problems

### Q.1 Consider a 3-CNF-SAT problem with n variables denoted x<sub>1</sub>,...,x<sub>m</sub> and m clauses. We wish to reduce it to a 0-1 ILP problem:<br>Find z<sub>1</sub> &#8712; {0, 1} ,..., z<sub>n</sub> &#8712; {0, 1} such that a set of m linear inequality constraints c<sub>1</sub>z<sub>1</sub> + c<sub>2</sub>z<sub>2</sub> + ... + c<sub>n</sub>z<sub>n</sub> &#8805; c<sub>0</sub> are all satisfied.<br>Select all the true facts about the reduction.<br><br>Answer:-<br>1. We use a 0-1 variable z<sub>i</sub> ​corresponding to each variable x<sub>i</sub> in the original 3-CNF-SAT problem.<br>2. A clause of the form x<sub>i</sub> &#8744; x<sub>j</sub> &#8744; x<sub>k</sub> translates into an inequality z<sub>i</sub> + z<sub>j</sub> + z<sub>k</sub> &#8805; 1.<br>3. The logical negation of a variable x<sub>i</sub> can be modeled as the arithmetic operation 1 - z<sub>i</sub><br>4. The clause x&#772;<sub>i</sub>&#772; &#8744; x<sub>j</sub> &#8744; x&#772;<sub>i</sub>&#772; is translated to the inequality -z<sub>i</sub> + z<sub>j</sub> -z<sub>k</sub> &#8805; -1<br>5. The reduction yields as many inequalities as the number of clauses in the 3-SAT formula

### Q.2 An independent set in a graph is a subset of vertices such that no two vertices in the independent set have an edge between them.<br>**k-Indpendent-Set Problem**<br>Given a graph G and a number k,  we wish to know if there is an independent set of size at least k in G.<br><br>Answer:-<br>1. The k Independent-Set problem is in NP since the certificate can involve just the set of k vertices that we claim to belong to an independent set.<br>2. A graph G has an independent set of size k if and only if its complement has a clique of size k.<br>3. We can reduce the problem of finding k-clique in a graph G to that of finding a k-independent-set in its complement G&#772;.










