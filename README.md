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

## Week 6:- Trees Quiz

### Q.1 Which of the following constructions defines the Motzkin (unary-binary) trees?<br><br>Answer:- M = Z + Z X M + Z X M X M

### Q.2 Of the following, which are the least numerous, for a given (large) number of nodes?<br><br>Answer:- unordered trees

### Q.3 Of the following, which are the most numerous, for a given (large) number of nodes?<br><br>Answer:- 3-ary trees

## Week 7:- Permutations

### Q.1 Of the following, which is the best approximation to the probability that a permutation of size Nhas exactly 1 cycle?<br><br>Answer:- 1 &frasl; N

### Q.2 Which event is leastlikely, in a random permutation of size 1000?<br><br>Answer:- It has no cycles of length less than 5.

## Week 8:- Strings and Tries

### Q.1 Which of the following is the OGF defining the bitstrings not containing 01010?<br><br>Answer:- 1 + z<sup>2</sup> + z<sup>4</sup> &frasl; z<sup>5</sup> + (1 - 2z)(1 + z<sup>2</sup> + z<sup>4</sup>)

### Q.2 Which of the following patterns has a longer expected wait time in a random bitstring than any of the others?<br><br>Answer:- 00000

## Week 9:- Strings and Words

### Q.1 Which of the following constructions defines birthday sequences?<br><br>Answer:- SEQ<sub>M</sub>(E+Z)

### Q.2 Which of the following EGFs define random mappings with no singleton cycles, as a function of the Cayley function C(z) = ze<sup>C(z)</sup>?<br><br>Answer:- e<sup>-C(z)</sup> &frasl; ( 1 - C(z) )

