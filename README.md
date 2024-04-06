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

### Q.2 Select all the correct facts about the behavior of the Huffman coding algorithm given a set of characters A<sub>1</sub> ,..., A<sub>n</sub> and their frequencies f<sub>1</sub> ,..., f<sub>n</sub>.<br><br>Answer:-<br>1. The character with lowest frequency will always have the highest number of bits assigned.<br>2. The character with second lowest frequency will also have the highest number of bits assigned.<br>3. Supposen = 32 and we assign 5 bits to each character. A Huffman code will always assign 5 or fewer bits per character, on average.

## Week 3:- Problem Set 3

### For the problem set 3 you need to go the Dynamic Programming, Greedy Algorithms Folder in that folder go to Week 3 Folder then there is a file named "Problem Set 3.py". In that file there are question and the code blocks in which some code is written you can directly copy paste the code accordingly.<br><br>  

Dynamic Programming, Greedy Algorithms Folder -> Week 3 -> Open Problem Set 3.py -> Then in Problem Set 3 module click on Launch Lab -> Then Copy & Paste code accordingly -> Then Submit your assignment.

```
Note:- A video Tutorial has also been added to the same Dynamic Programming, Greedy Algorithms folder.
Named as "Tutorial for Problem Set 3.MOV" In week 3 for problem set 3. If anyone is facing any issue related
to do how to do week 3 problem set, then they can refer to that video. Or you can see it below.
```

### Step-By-Step Guide for problem set 3


https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/decf1bc5-e7d3-444d-8da2-944acc2bb258




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

## Week 4:- Problem Set 4

### For the problem set 4 you need to go the Dynamic Programming, Greedy Algorithms Folder in that folder go to Week 4 Folder then there is a file named "Problem Set 4.py". In that file there are question and the code blocks in which some code is written you can directly copy paste the code accordingly.<br><br>  

Dynamic Programming, Greedy Algorithms Folder -> Week 4 -> Open Problem Set 4.py -> Then in Problem Set 4 module click on Launch Lab -> Then Copy & Paste code accordingly -> Then Submit your assignment.


# Link of course:-  https://www.coursera.org/learn/linear-programming-and-approximation-algorithms

# Approximation Algorithms and Linear Programming

## Interactive Notes: Basics of Linear Programs
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 1:- Basics of Linear Programs

### Q.1 Consider the following linear program: <br><br> max&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3x + 4y<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x + y &#8804; 4<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x &#8805; 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y &#8805; 0<br><br>Check all options that are correct.<br><br>Answer:-<br>1. The optimal solution for the above LP is 16.<br>2. If we remove the constraint<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x + y &#8804; 4<br>it is still a feasible LP problem.<br>3. If we changed the problem's objective function to <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; min - 3x - 4y<br>then the optimal solution for (x,y) remains unchanged.

### Q.2 Consider the following scenario.<br><br>Green Energy Solutions is a company specializing in solar panel installations. They have a limited workforce and want to maximize their profit while adhering to certain constraints. The company has two types of solar panel installations: Type A and Type B.<br><br>Each Type A installation:<ul><li>Requires 12 hours of labor</li><li>Costs $500 in materials</li><li>Generates $800 profit per installation.</li></ul><br><br>Each Type B installation:<ul><li> Requires 8 hours of labor</li><li>Costs $300 in materials</li><li>Generates $600 profit per installation. </li></ul><br>The company has a total of 1000 labor hours available.<br><br>The company has $400,000 in cash at hand.<br><br>Due to supply constraints, the company can only install a maximum of 300 Type A panels.<br><br>Formulate a linear program to maximize the profits while adhering to the constraints above. Let decision variable A denote the number of type A installation and decision variable B denote the number of type B installations.<br>Choose the correct answers from the choices given below.<br><br>Answer:-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;800A+600B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12A+8B≤1000<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;500A+300B≤400000<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A≤300<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A,B≥0
​
### Q.3 Select all options that are linear programs.<br><br>Answer:-  <br>1. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min&nbsp;&nbsp;&nbsp;5x+7y<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3x+2y≤12<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4x+5y≤15<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x,y≥0<br><br>2. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;5x+3y<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x+y≤10<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3x+2y≤15<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x,y≥0

### Q.4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;2x+y<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x+y≥5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x,y≥0<br>The given linear program is:<br><br>Answer:- Feasible but not bounded

### Q.5 Select all the options that are correct.<br><br>Answer:- An LP problem can have more than one optimal solution

## Lab: Formulate and Solve LPs using PULP
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 1:- Solving LPs using PULP

### Q.1 What does the statement<br>x_var = pulp.LpVariable('x', lowBound=0, upBound=10, cat='Continuous')<br>achieve? Select all the correct answers. See documentation here: https://www.coin-or.org/PuLP/pulp.html<br><br>Answer:-<br>1. Setting cat=Continuous is optional since the category is set to Continuous by default.<br>2. In a linear programming problem, every decision variable should have cat = Continuous<br>3. It adds a decision variable 'x' to the problem.

### Q.2 Consider the following code sinppet:<br>
```
from pulp import *
mdl = LpProblem('my_problem', LpMaximize)
x = LpVariable('x', lowBound = 0)
y = LpVariable('y', lowBound = 0, upBound = 4)
mdl += (x + 2 * y) 
mdl += x <= y + 3
mdl += x >= y - 1 
mdl += x - 2 * y <= 5
status= mdl.solve()
print(x.value())
print(y.value())
print(mdl.objective.value())
```
### Select all the correct facts about the code snippet above. Make sure that no incorrect facts are selected.<br><br>Answer:-<br>1. The LP problem as entered in the code snippet is feasible<br>2. The LP problem as entered in the code snippet is bounded.<br>3. The linear programming problem seeks to maximize the objective x + 2 * y<br>4. The constraint x − 2 y≤ 5 is part of the linear program.

### Q.3 Consider again the code snippet  from the previous problem
```
from pulp import *
mdl = LpProblem('my_problem', LpMaximize)
x = LpVariable('x', lowBound = 0)
y = LpVariable('y', lowBound = 0, upBound = 4)
mdl += (x + 2 * y) 
mdl += x <= y + 3
mdl += x >= y - 1 
mdl += x - 2 * y <= 5
status= mdl.solve()
assert status == LpStatusOptimal
print(x.value())
print(y.value())
print(mdl.objective.value())
```
### Select all the correct choices from the list below<br><br>Answer:- All options are correct

### Q.4 Consider the code snippet below:
```
from pulp import *
mdl = LpProblem('n_problem', LpMaximize)
n = 15
vars = [ LpVariable(f'x{i}', lowBound = 0.0) for i in range(n)]
mdl += lpSum(vars)
for i in range(14):
    mdl += vars[i] - vars[i+1] <= i 
    mdl += vars[i] - vars[i+1] >= -i
status = mdl.solve() 
if status == LpStatusOptimal:
    print('Optimal solution found!')
    print([vi.value() for vi in vars])
    print(mdl.objective.value())
elif status == LpStatusInfeasible:
    print('Infeasible problem')
elif status == LpStatusUnbounded:
    print('Unbounded problem')
else:
    print('Unknown status')
```
### Answer:-<br>1. The objective for this problem is the sum of all the variables in the list vars<br>2. Line 4 of the problem declares n=15 variables and stores them in the list vars<br>3. The problem is unbounded.

## Interactive Notes: Diet Problem and Network Flow Problems
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 1:- Network Flow Problems as LPs

### Q.1 Select all the options that are true for network flow problems. Assume all edge capacities are finite and non-negative.<br><br>Answer:-<br>1. At each vertex , the incoming flow equals the outgoing flow.<br>2. Network flow problems are always feasible as long as the graph is connected.<br>3. Flow capacity can be less than or equal to the capacity of the edge.

### Q.2 For the given network , what is the maximum flow that can be transported from source to sink ?

<img width="811" alt="Screenshot 2024-03-24 at 11 55 34 PM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/d592e04d-d2b0-42af-b96f-58947016c33a">

### Answer:- 15

### Q.3 
<img width="985" alt="Screenshot 2024-03-25 at 12 03 13 AM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/0a78f9df-efea-48c1-983a-36dd72092048">

### Select all the correct flow conservation constraints from the list below.<br><br>Answer:-<br>1. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>BD</sub> = x<sub>DC</sub> + x<sub>DE</sub><br>2. x<sub>AC</sub> + x<sub>DC</sub> = x<sub>CE</sub><br>3. x<sub>AB</sub> = x<sub>BD</sub>

## Week 1:- Geometry of Linear Programs

### Q.1 If a LP has an optimal solution, then at least one solution can always be found at:<br><br>Answer:- the vertices of the feasible region.

### Q.2 Consider the following objective function<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min 4x + 2y + 3z​<br>The feasible region is a  convex polyhedron with the following vertices A(2, 3, 1), B(4, 1, 2), C(5, 4, 1), D(3, 5, 3), and E(1, 2, 1).  we have provided a name for each vertex and its coordinates <br>The optimal value for this LP is:<br><br>Answer:- 9

### Q.3 Select all that apply for a convex polyhedron in the context of linear programming.<br><br>Answer:-<br>1. The optimal solution always lies at one of the vertices of the convex polyhedron.<br>2. Every point within the convex polyhedron , forms a feasible solution.<br>3. For any 2 points within the convex polyhedron , the line segment joining the 2 points also lies completely within the polyhedron.<br>4. Convex polyhedron is formed by the intersection of half spaces defined by constraints.

### Q.4 Which of the following graphs correctly depicts the feasible region for the given LP :<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;4x + 3<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x + y ≤ 8<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x + 2y ≤ 6<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x &#8805; 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y &#8805; 0<br><br>Answer:-<br>
<img width="917" alt="Screenshot 2024-03-25 at 12 17 59 AM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/2caa1d16-363b-47fe-a5c1-7d0c6012c057">

## Interactive Notes on Geometry of Linear Programs and Simplex Algorithm
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 1:- LP Algorithms

### Q.1 Select all options that are true about vertices of a polyhedron.<br><br>Answer:-<br>1. A vertex of a polyhedron satisfies all the constraints.<br>2. Vertex lies on at least n faces of the polyhedron , where n is the number of decision variables.

### Q.2 Which of the following statements are true about the simplex algorithm in LP ?<br><br>Answer:-<br>1. At every iteration , the algorithm moves to an adjacent vertex to improve the value of the objective function.<br>2. The average case time complexity for simplex algorithm is polynomial time.

## Problem Set # 1 :- Programming Assignment: Linear Programming
### To complete this lab Click on the link below:-
<a href="Approximation Algorithms and Linear Programming/Week 1/Problem Set 1.ipynb">Click Here</a> 

## Week 2:- Integer Linear Programming

### Q.1 Consider the integer linear programming problem:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;2x<sub>1</sub> + 3x<sub>2</sub><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s.t.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> &#8805; 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> &#8804; 9.8<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>2</sub> &#8805; 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>2</sub> &#8804; 10.5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub> &#8712; Z<br>Select all true facts about this problem below, ensure no wrong facts are selected.<br><br>Answer:-<br>1. The LP relaxation achieves an optimal objective value of  51.1 whereas the ILP optimal solution is 48.<br>2. The integrality gap for this problem is 51.1/48<br>3. The problem has an optimal solution and it is given by x<sub>1</sub> = 9, x<sub>2</sub> = 10.
 
### Q.2 Select all the true facts about integer linear programming problems in relation to their LP relaxations. Make sure that no incorrect fact is selected.<br><br>Answer:-<br>1. If the ILP is unbounded, the LP relaxation is unbounded too.<br>2. If the problem involves maximizing an objective, the optimal ILP objective is always less than or equal to that of the LP relaxation.

### Q.3 The following questions concern the NP-completeness of integer linear programming. Please select all correct facts.<br><br>Answer:- All are correct.

### Q.4 Suppose we are given an ILP which seeks to minimize an objective functions subject to constraints. We solve the LP relaxation and find an optimal solution with the objective evaluating to 54.3<br><br>What can you say about the original ILP.<br><br>Answer:-<br>1. If the ILP is feasible, its optimal solution must be greater than or equal to 54.3<br>2. It is possible that the ILP's optimal solution (if it exists) will be 76.5 X 10<sup>2331</sup><br>3. If the ILP is feasible, it is guaranteed to be bounded.<br>4. If the integrality gap of the ILP problem was known to be 3, then the ILP optimal solution will be in the range [ 54.3,3 X 54.3]

## Week 2:- Formulating/Solving ILPs

###  **Important Note**<br><br>The problems below ask you to setup and solve ILPs using Pulp. It helps to have python3 installed in your computer. If you have a package manager such as pip/conda, you can directly use them to install pulp library. This will allow you to program in python either through your REPL, or through an IDE such as Atom, VSCode, IntelliJ PyCharm and so on.<br><br>Alternatively, if you are not setup to program on your local machine, we suggest using google colab to have a python3 jupyter notebook. In the very first cell of the notebook type !pip3 install pulp to install the pulp library. In the next cell please type from pulp import * to check if it got installed.
<img width="600" alt="Screenshot 2024-04-06 at 9 43 19 PM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/d66b1b4d-b2fc-47f2-9428-d996ed847adc">

<br>
### You can type python programs to solve the ILPs and find out the answers for the problems below.<br><br>The questions below pertain to the ILP<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;2x<sub>1</sub> - 3x<sub>2</sub> + x<sub>3</sub><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s.t.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> + x<sub>3</sub> &#8804; 5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> + 4x<sub>3</sub> &#8804; 7<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> + 2x<sub>2</sub> - x<sub>3</sub> + x<sub>4</sub> &#8804; 14<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>3</sub> - x<sub>4</sub> + x<sub>5</sub> &#8804; 7<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub> &#8712; [-15, 15]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub> &#8712; Z<br><br>Q.1 Please use a python interpreter to setup and solve the following integer linear programming problem using pulp.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;2x<sub>1</sub> - 3x<sub>2</sub> + x<sub>3</sub><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s.t.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> + x<sub>3</sub> &#8804; 5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> + 4x<sub>3</sub> &#8804; 7<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> + 2x<sub>2</sub> - x<sub>3</sub> + x<sub>4</sub> &#8804; 14<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>3</sub> - x<sub>4</sub> + x<sub>5</sub> &#8804; 7<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub> &#8712; [-15, 15]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub> &#8712; Z<br><br>Write down the optimal value of the objective function correct to two decimal places.<br><br>Answer:- ```40.00```

### Q.2 Solve the LP relaxation of the ILP from the previous problem using PuLP. What is the answer obtained?<br><br>Answer:- ```40.00```

### Q.3 What can you conclude from solving the LP relaxation and original ILP for the previous problem.<br><br>Answer:-<br>1. They have the same solution.<br>2. The LP relaxation yields an integral solution for all the decision variables and we know from just that information that the ILP will also have the same optimal solution.<br>3. The integrality gap is 1.<br><br>The questions below pertains to the following ILP<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max&nbsp;&nbsp;&nbsp;2x<sub>1</sub> - 3x<sub>2</sub> + x<sub>3</sub><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s.t.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> &#8805; 5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub> - x<sub>2</sub> &#8804; 0.75<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>2</sub> - x<sub>3</sub> &#8804; 1.25<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>2</sub> - x<sub>3</sub> &#8805; 0.95<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> &#8712; [-1, 1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> &#8712; Z

### Q.4 What is the status obtained when solving the ILP?<br><br>Answer:- Infeasible

### Q.5 What is the status of the LP relaxation?<br><br>Answer:- Optimal solution obtained

## Interactive Notes: Vertex Cover as an ILP
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 2:- Vertex Cover Problem ILP formulation

### Q.1 Which of the following statements is true about an optimal solution to the vertex cover problem?<br><br>Answer:- It includes the minimum number of vertices that cover all edges

### Q.2 If you add a constraint 'xi + xj <= 1 for some edge (i, i)' to the vertex cover problem, what will be the effect?<br><br>Answer:- Some valid vertex covers will be excluded

### Q.3 Which of the following is a correct integer linear programming formulation for the vertex cover problem?<br><br>Answer:- Minimize &#8721; xi subject to xi + xj >= 1 for every edge (i, j) and xi in {0, 1} for every vertex i

### Q.4 Given a graph with vertices (1, 2, 3, 4} and edges (1, 2), (2, 3), (3, 4), which of the following is a feasible solution for the vertex cover problem?<br><br>Answer:-<br>1. {2,4}<br>2. {1,3}

### Q.5 In an integer linear programming formulation, why is the condition 'xi in (0, 1} for every vertex i' necessary for the vertex cover problem?<br><br>Answer:- It ensures that the solution is a vertex cover

## Interactive Notes: Integrality Gap for Vertex Cover
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 2:- Vertex Cover ILP, LP Relaxation and Integrality Gap.

### Q.1 We wish to find the optimal vertex cover for a graph G. Solving the LP relaxation of the vertex cover problem yields an optimal solution with value 442. What can we say about the size of the optimal vertex cover of the graph G? Choose all the options that are correct.<br><br>Answer:-<br>1. The optimal vertex cover size lies in the range [442, 884].<br>2. Using the rounding procedure on fractional solutions of the LP relaxation would yield a vertex cover of size between 442 and 884.

### Q.2 Calculate the optimal vertex cover for the graph below. Feel free to use the code/notes provided as part of the ungraded lab. Hopefully you have a python setup either on your computer with the pulp library installed or you are using google colab as indicated in the previous quiz on solving ILPs.
<img width="703" alt="Screenshot 2024-03-26 at 3 55 41 PM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/ddcfe0bb-4605-4d32-a5d8-7e66de44abd9">

### Answer:- 5

### Q.3 Solve the LP relaxation for the graph in the previous problem and write down its optimal objective value below.<br><br>Answer:- 3.5

### Q.4 If we rounded the LP relaxation for the problem above, what is the vertex cover we obtain?<br><br>Answer:- All the vertices of the graph are part of this cover.

## Interactive Notes: Branch and Bound Solvers for ILPs
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 2:- Branch and Bound Solvers

### Q.1 Suppose we are solving an ILP using branch and bound algorithm. Select all the facts below about the algorithm that are true.<br><br>Answer:-<br>1. Each step of branch and bound solves the LP relaxation of some ILP problem that is either the original problem or  obtained by branching.<br>2. If the LP relaxation at the "root" of the branch and bound is infeasible, the whole ILP must be infeasible.<br>3. If the original ILP is unbounded, then the LP relaxation at the root of branch and bound (the very first LP we will solve) will be unbounded.

### Q.2 We are solving a branch and bound problem and at some stage, we solve a LP relaxation that yields the solution x<sub>1</sub> = 2.5, x<sub>2</sub> = 1.3, x<sub>3</sub> = 5, x<sub>4</sub> = 6.9.<br><br>Select all the valid options for the branch and bound algorithm.<br><br>Answer:-<br>1. We recursively solve two subproblems with the constraints x<sub>4</sub> &#8804; 6 and x<sub>4</sub> &#8805; 7, respectively.<br>2. We may recursively solve two subproblems with the constraints x<sub>1</sub> &#8804; 2 and x<sub>1</sub> &#8805; 3, respectively.

### Q.3 We are solving an ILP whose objective function is max x<sub>1</sub> + x<sub>2</sub> - x<sub>3</sub>. At some point in the branch and bound algorithm, we have seen integer solutions shown below:<br>
| x<sub>1</sub> | x<sub>2</sub> | x<sub>3</sub> | objective |
|---------------|---------------|---------------|-----------|
|       1        |        2       |      -1         |     4      |
|       4       |        1       |      2         |     3      |
|       5        |        2       |      -2         |     9      |
|       1        |        1       |      1         |     2      |

### Select all true facts from the list below.<br><br>Answer:-<br>1. Suppose we solve an LP relaxation and find that the objective value is 9.8 , we can prune this branch from further consideration.<br>2. Suppose we solve an LP relaxation and find that the objective value is 8.5, we can prune this branch from further consideration.<br>3. The optimal solution of the ILP will have objective value greater than or equal to 9.

## Problem Set # 2 :- Programming Assignment: Integer Linear Programs
### To complete this lab Click on the link below:-
<a href="Approximation Algorithms and Linear Programming/Week 2/ProblemSet2.ipynb">Click Here</a>

## Week:- 3 Approximation Algorithm Basics

### Q.1 We have designed an efficient 2-factor approximation algorithm for a minimization problem.  Running the approximation algorithm on an instance yields a solution with objective value 12. What can we say about the optimum?<br><br>Answer:- The optimal solution is in the range 6 ≤ OPT ≤ 12.

### Q,2 We have designed an efficient 3-factor approximation algorithm for a maximization problem.  Running the approximation algorithm on an instance yields a solution with objective value 12. What can we say about the optimum?<br><br>Answer:-<br>1. The optimal solution may be the same as that of the approximation algorithm.<br>2. The optimal solution is in the range 12 ≤ OPT ≤ 36

## Interactive Notes: Jobshop Scheduling
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 3:- Job Shop Scheduling Questions

### The questions below concern the following instance of the jobshop scheduling problem.
| Job ID | Time |
|--------|------|
| 1 | 5 |
| 2 | 6 |
| 3 | 2 |
| 4 | 5 |
| 5 | 2 |
| 6 | 1 |
| 7 | 3 |
| 8 | 4 |

### Q.1 Consider an instance of the minimum makespan scheduling above. Suppose we have three processors. What is the makespan achieved if we ran the greedy algorithm. You can simply use a pencil and paper to run the greedy algorithm to work out the answer. Assume that the algorithm processes the jobs in the increasing order of Job ID.<br><br>Answer:- `11`

### Q.2 What is the makespan of the solution
| Processor | Job IDs |
|-----------|---------|
| 1 | 2, 3, 5 |
| 2 | 1, 6, 7 |
| 3 | 4, 8 |

### Answer:- `10`

### Q.3 Suppose we sorted the jobs in decreasing order of their times instead and ran the greedy algorithm. What is the makespan of the optimal solution obtained?<br><br>Answer:- `10`

### Q.4 Without solving the optimal problem, we wish to find bounds on the optimal solution anyways. Which of the following options are valid arguments that serve to place bounds on the  optimal solution.<br><br>Answer:-<br>1. The total times for all jobs is 28. No matter how we distribute it among three processors, at least one processor must have finish time more than $\frac{28}{3}$ or 9.3333.... Therefore, the optimal answer cannot be smaller than 10.<br>2. The algorithm is known to have an approximation ratio of 2 - $\frac{1}{3}$ = $\frac{5}{3}$. Therefore, the optimal solution has to be at least 11 &#215; $\frac{3}{5}$ &#8776; 6.6<br>3. The following assignment: 
| Processor | Job IDs |
|-----------|---------|
| 1 | 2, 3, 5 |
| 2 | 1, 6, 7 |
| 3 | 4, 8 |

### has a makespan of 10. And therefore, the optimal solution must have value $\leq 10$.<br>4. By pigeon hole principle, if we consider the first four job IDs 1, 2, 3, 4; at least two of the jobs must share the same processor in any assignment. This yields a lower bound of 7 on the optimal solution.

## Interactive Notes on Vertex Cover Approximation Algorithms
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 3:- Vertex Cover

### The questions below concern the following graph with 7 nodes.
<img width="740" alt="Screenshot 2024-03-26 at 9 59 43 PM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/c112ccf3-cdb4-4dae-8284-0353bcee7614">

### Q.1 Suppose we apply the greedy algorithm that repeatedly chooses the maximum degree node in the graph, adds it to the cover and then deletes it from the graph.  Note that we break ties between multiple vertices that have the same degree by choosing the vertex with lowest number/ID.<br><br>Answer:-<br>1. Node 4 is the second node added to the cover.<br>2. Node 3 is the very first node added to the cover.<br>3. Node 6 is the third node added to the cover.<br>4. The greedy algorithm produces a vertex cover of size 5 that involves nodes 1, 3, 4, 5, 6

### Q.2 Suppose we ran the greedy algorithm based on maximal matching and processed the edges in the following order:<br><br>`[(1,2), (1,3), (1, 4), (2,3), (2,6), (3,4), (3,5), (3,6), (4, 5), (4,7), (5, 6), (5,7), (6,7)]`<br><br>What is the size of the vertex cover that we obtain?<br><br>Answer:-`6`

## Interactive Notes on Maximum Satisfiability Approximation
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 3:- Max-SAT Approximation

### The problems below concern the following instance for the MAX-SAT problem involving propositional variables $\{x_1}$, $\{x_2}$, $\{x_3}$, $\{x_4}$. Note that &#8744; stands for Or, $\overline{x_j}$ epresents the negation of $\{x_j}$<br><br>Consider the MAXSAT instance involving the following clauses.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\{x_1}$ &#8744; $\{x_2}$ &#8744; $\overline{x_4}$ <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\overline{x_2}$ &#8744; $\{x_3}$ &#8744; $\{x_4}$ <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\{x_1}$ &#8744; $\overline{x_2}$ &#8744; $\{x_3}$ <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\{x_2}$ &#8744; $\overline{x_3}$ &#8744; $\overline{x_4}$<br><br><br>Q.1 What is the expected number of clauses that a randomly chosen truth assignment where each variable is independently assigned true/false with probability $\frac{1}{2}$ .<br><br>Answer:- `3.5`

### Q.2 Using just  the information from the previous problem select which fact you can conclude.<br><br>Answer:- There is a truth assignment that satisfies all the clauses.

### Q.3 Suppose we set $\{x_1}$ = true, what is the expected number of clauses we can satisfy in the resulting formula?<br><br>Answer:- `3.75`

### Q.4 Suppose we set $\{x_1}$ - false, what is the expected number of clauses we can satisfy in the resulting formula?<br><br>Answer:- `3.25`

### Q.5 What truth value will our approximation algorithm for MAXSAT assign to $\{x_1}$ ?<br><br>Answer:- `True`

## Problem Set # 3 :- Programming Assignment: Approximation Algorithms
### To complete this lab Click on the link below:-
<a href="Approximation Algorithms and Linear Programming/Week 3/Problem-Set-3.ipynb">Click Here</a>


## Interactive Notes on TSP Basics, NP-Hardness and Inapproximability
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 4:- TSP Basics

### Q.1 The questions below concern the following TSP instance involving 5 nodes:
![eicLGcr0R7-dQsS1-tuUPw_6d525c030e0140ac97206c949eb66df1_IMG_8FC0BB8E69EC-1](https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/d1c1b44e-5a56-4392-82c9-6fd8a9d560c2)
### Edges shown in black are assigned a weight of 1 whereas edges shown in red are assigned a weight of 2.<br><br>Q1. Select all the correct answers from the list below.<br><br>Answer:-<br>1. The sequence of vertices 1,2,3,4,5, 1  (1 is the start/end point) is a valid TSP tour of cost 6 <br>2. There is a TSP tour whose cost is 5, i.e, it involves only the black edges in the graph. 

### Q.2 The TSP above is an instance of a Metric TSP. It is symmetric and satisfies the triangle inequality.<br><br>Answer:- True

### Q.3 This question concerns the following instance of the Hamiltonian Cycle Problem:
![7DvSL14CRue5RQQDOzFVyA_116ca8259056434491dd6b70378df8f1_IMG_7932ED17635F-1](https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/d4689cd9-762c-4fc2-8e64-3cdcfdbf7648)
### We wish to find out if there is a Hamiltonian cycle problem using a reduction to the TSP problem. Select all the correct answers about this reduction.<br><br>Answer:-<br>1. The reduction will need to assign a weight of 1 to each edge in the original graph and add the missing edges (4,5), (1,3) and (2,4) with some weight $\{W > 1}$.<br>2. Let $\{W > 1}$ be the weight given to the missing edges that we will need to add back for the reduction to TSP. The optimal TSP tour cost will be at least $\{5 + W}$ if there is no Hamiltonian cycle.<br>3. Once we reduce to the TSP, we conclude the presence of a Hamiltonian cycle if the optimal TSP tour has weight 6.

## Interactive Notes on Exact Approaches to TSP
```
For this lab just launch lab and then cut the tab and refresh your course you will find it is already completed.
```

## Week 4:- Held-Karp Algorithm

### The problem below concerns the following TSP instance. Edges shown in black have a weight of 1 1 whereas red edges have a weight of 3.
![eicLGcr0R7-dQsS1-tuUPw_6d525c030e0140ac97206c949eb66df1_IMG_8FC0BB8E69EC-1](https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/74ab48b7-66a1-4b60-b2f8-7eaac3f6acd1)
### Assume vertex 1 is the designated start/end point of the tour. Let $C_{ij}$ represent the cost of the edge from vertex i to vertex j.<br><br>Q.1 Which of the following expressions is the appropriate equation for the value of $minCostPath(\\{2,3\\},4)$?<br<br>Answer:- $\min(\text{{minCostPath}}(\\{2\\},3) + C_{3,4}, \text{{minCostPath}}(\\{3\\},2) + C_{2,4})$

### Q.2 Calculate the value of $minCostPath(\\{2,3\\},4)$?<br<br>Answer:- `3`

### Q.3 What vertex in the graph would you associate with the memo table corresponding to $minCostPath(\\{2,3\\},4)$ to recover the minimum cost path?<br<br>Answer:- `3`

### Q.4 Consider the recurrence for the minimum cost TSP tour:<br><br> <img width="500" alt="Screenshot 2024-03-29 at 1 40 46 AM" src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/372ac2f8-6ab0-4115-a0f0-8eb489fb0173"><br><br>Select appropriate choices for the missing portions.<br><br>Answer:-<br>1. ??<sub>4</sub> $= C_{2,1}$ <br>2. ??<sub>6</sub> $= C_{3,1}$ <br>3. ??<sub>1</sub> $= C_{4,1} = 2$

## Week 4:- TSP Integer Programming

### The following problems concern the TSP instance below. Black colored edges have weight 1 1 whereas red edges have weight 2.<br><br> ![eicLGcr0R7-dQsS1-tuUPw_6d525c030e0140ac97206c949eb66df1_IMG_8FC0BB8E69EC-1](https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/9f835762-7660-4d40-8d5e-1546a094380c) <br><br>We consider both the encodings MTZ and subtour elimination as presented in our interactive notes. Note that they are more general than the ones in the video which did not go into the details for non-symmetric cases. Please read through these notes and look at the provided code before attempting the problems below.<br><br>Q.1 Select all the correct facts about the ILP encoding/decision variables $x_{i,j}$ .<br><br>Answer:-<br> 1. Setting the  variable $x_{i,j} = 1$ denotes that we go from vertex i to j using the edge (i,j) in our tour.<br>2. The constraint $x_{2,1} + x_{3,1} + x_{4,1} + x_{5,1} = 1$ expresses that we have exactly one edge entering the vertex 1 in our tour.

### Q.2 Select all the correct facts about the MTZ encoding as it pertains to the problem above.<br><br>Answer:-<br>1. Time stamp variables $t_2,t_3,t,_4,t_5$  are added to eliminate possible subtours by assigning increasing time stamps to nodes visited along a tour.<br>2. The constraint t<sub>3</sub> &ge; t<sub>2</sub> + x<sub>2,3</sub> - M(1 - x<sub>2,3</sub>) for a large number M is equivalent to if x<sub>2,3</sub> = 1 then $t_3 \geq t_2 + 1$ else $t_3 \geq t_2 - M$

### Q.3 Suppose we solve the degree ILP relaxation and obtain a subtour {2,3,5}, which of the following inequalities will eliminate the subtour. Once again, please refer to the detailed notes which present the general case for non-symmetric TSPs rather than the video lecture which is restricted to the symmetric case.<br><br>Answer:-<br>1. $x_{2,4} + x_{3,4} + x_{5,4} + x_{2,1} + x_{3,1} + x_{5,1} \geq 1$ <br>2. $x_{4,2} + x_{4,3} + x_{4,5} + x_{1,2} + x_{1,3} + x_{1,5} \geq 1$

## Week 4:- Approximations for Metric TSPs

### Suppose we have a TSP instance for which the minimum spanning tree (MST) is shown below.
<img src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/2aac6c18-7a9a-49b8-b506-c957d3311ac0" alt="EPPcriinQSaZTJU5q_Oycw_2e4ae7df467c49e0aeed293fd30fd8f1_tsp-mst-quiz" width="300px">

### The edges not in the MST have not been shown. We perform a depth first traversal of the TSP and it yields the following sequence of visits that form a TSP tour:<br><br>[1,2,5,6,3,4]<br><br>Note that we take vertex 1 to be the start/end point.<br><br>Q.1 Which of the following  are the shorcut edges in the TSP tour constructed?<br><br>Answer:-<br>1. (6,3)<br>2. (5,6)<br>3. (4,1)

### Q.2 What can we say for sure about the cost of the edge (6,5) denoted $C_{6,5}$ in the original TSP?<br><br>Answer:-<br>1. $C_{6,5} &#8804; 2$<br>2. $C_{6,5} = C_{5,6}$

### Q.3 What can we say for sure about the cost of the TSP tour [1,2,5,6,3,4] obtained computed by shorcutting the MST as above? Select all choices that apply<br><br>Answer:-<br>1. The cost of the tour must be less than or equal to twice the cost of the MST.<br>2. The cost of the TSP tour must be  &#8804; 10

### Q.4 Which of the following statements about the cost of the optimal TSP tour for the instance above can be concluded.<br><br>Answer:-<br>1. The optimal tour cost has to be &#8805; 5.<br>2. The optimal tour cost has to be &#8804; 10.<br><br>Proceeding with the previous example, the odd degree vertices in the MST are {1,4,5,6} each of which is a leaf and has degree 1. Suppose we construct a minimum weight matching over these odd degree vertices to obtain the following graph which shows the original MST edges in black and the matching edges and weights in blue.<br><br> <img src="https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/assets/120407422/2aac6c18-7a9a-49b8-b506-c957d3311ac0" alt="EPPcriinQSaZTJU5q_Oycw_2e4ae7df467c49e0aeed293fd30fd8f1_tsp-mst-quiz" width="300px"> <br><br>An Eulerian tour of this graph is obtained as<br><br>[1,2,5,4,3,2,6,1]<br><br>You can verify that this tour visits all edges in the graph formed by MST and matching edges.

### Q.5 Which of the following is the TSP tour that will be obtained by shortcutting the Eulerian tour?<br><br>Answer:- [1,2,5,4,3,6]

### Q.6 Which of the following is a valid observation about the cost of the TSP tour obtained by shortcutting the Eulerian tour?<br><br>Answer:-<br>1. Cost of TSP tour is less than or equal to 8.7<br>2. The cost of the tour must be less than or equal to the cost of all the edges in the matching + cost of all edges in the MST<br>3. Cost of TSP tour is less than or equal to 10 (the bound we placed on the cost of the previous tour using DFS).

## Week 4:- Fully Polynomial Time Approximation Scheme

### Q.1 A fully polynomial time approximation scheme for a maximization problem guarantees a solution within ( 1 - &#8714; ) OPT where OPT is the optimal solution value in time $n^2 &#215; \left(\frac{1}{\epsilon}\right)^2$. . We wish to compute an approximation that is guaranteed to be no worst than 0.9OPT What is the time cost for the algorithm?<br><br>Answer:- $100n^2$<br><br>The questions below concern  a Knapsack problem instance with 4 items and the following data about weights and value. <br>
| | a1 | a2 | a3 | a4 | 
|-|----|----|----|----|
| Weight | 2 | 4 | 3 | 1 |
| Value | 1 | 2 | 1 | 1 |
### The total weight budget is $ 6 $.<br><br>Recall that $W_{i,v}$ is defined as the minimum weight of items needed to achieve value exactly v while choosing the subset of items { a<sub>1</sub>,...,a<sub>i</sub> }<br><br>Also recall the recurrence/base cases for $W$<br><br>$W (0,0) = 0, W (0,v) = &#8734;$ $if$ $v > 0, W (i,0) = 0$<br>$W (i,v) = min( W (i - 1,v), W (i - 1, v - v_i) + w_i )$ where $w_i, v_i$ are the weight and value, respectively of item $a_i$. 

### Q.2 Which of the following expressions in terms of $W$ yield the optimal value for the original Knapsack problem?<br><br>Answer:- $\max \{v \mid 0 \leq v \leq 5 \text{ and } W(4,v) \leq 6\}$

### Q.3 Select all the correct choices from the list below.<br><br>Answer:-<br>1. $W (0,0) = 0$<br>2. $W (1,1) = min( W (0,1), W (1,0) + 2)$<br>3. $W (1,1) = 2$ 


























