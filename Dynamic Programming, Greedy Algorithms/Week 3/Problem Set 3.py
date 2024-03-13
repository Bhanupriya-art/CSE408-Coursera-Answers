#!/usr/bin/env python
# coding: utf-8

# # Assigment 3: Greedy Algorithms
# 
# In this assignment, we will explore greedy algorithms for makespan scheduling. We will see how a greedy algorithm can sometimes provide a solution that is guaranteed to be within some constant factor of the best possible solution. Please fill out the missing answers and the missing code below. Note that the coding part of this assignment should be simple given where we are in this class but the ungraded answers will hopefully be most instructive for this assignment.
# 
# See https://jeffe.cs.illinois.edu/teaching/algorithms/notes/J-approx.pdf section J1 for more details.
#  
#   
# ## Problem 1: Makespan Scheduling.
# 
# Let us consider $n$ jobs that take times $T_1, \ldots, T_n$ to complete where each $T_i > 0$. We have $m \geq 2$ processors to process these jobs. Our goal is to assign these jobs to the processor.
# 
# An assignment is modeled as an array $A: [A_1, \ldots, A_n]$ wherein each $A_i$ represents the number of the processor to which job $i$ is assigned. Eg., $A_3 = 4$ means that job number $3$ is assigned to processor $4$.
# Therefore each $A_i \in \{ 1, \ldots, m \}$.
# 
# Once the assignment is complete, each processor runs the jobs assigned to it under some order. 
# 
# ### Question 1
# 
# Let $M_j$ be the total time taken by some processor $j$ to complete all the jobs assigned to it.
# 
# Write down an expression for $M_j$? We will not grade your answer but you may be able to check against the provided solutions.

# YOUR ANSWER HERE

# ### MakeSpan of an Assignment (Def)
# $$\newcommand\mspan{\sf MakeSpan }$$
# 
# The makespan of an assignment $A$ denoted $\mspan(A)$ is the maximum among the total times taken by each processor. Formally, 
# 
# $$\mspan(A) = \max_{j=1}^m M_j$$
# 
# The makespan of an assignment denotes the total time taken to complete all the jobs with the processors running in parallel since it measures the time taken by the processor which takes the longest to complete all its assigned tasks.
# 
# #### Example
# 
# Consider jobs with times $[T_1: 2,\ T_2: 2,\ T_3: 2,\ T_4: 2,\ T_5: 2,\ T_6: 2,\  T_7: 3]$ and $m = 3$ processors.
# 
# Consider the assignment $A: [A_1: 1,\ A_2: 1,\ A_3: 2,\ A_4: 2,\ A_5: 3,\ A_6: 3,\ A_7: 2 ]$.
# 
# ### Question 2 
# 
# Write down the total times taken by each processor under the given assignment. What is the makespan of this assignment? Is there a better assignment of jobs to processor that can reduce the makespan? If so what is it?
# 

# YOUR ANSWER HERE

# ## Problem A: Calculate Makespan of an Assignment

# In[1]:


def compute_makespan(times, m, assign):
    # times is an array of job times of size n
    # m is the number of processors
    # assign is an array of size n whose entries are between 0 to m-1 
    # indicating the processor number for
    # the corresponding job.
    # Return: makespan of the assignment
    # your code here
    
    total_times = [0]*m
    n = len(times)
    
    for i in range(n):
        this_processor = assign[i]
        this_time = times[i]
        total_times[this_processor] = total_times[this_processor] + this_time
        
    makespan = max(total_times)
    return(makespan)


# In[2]:


## BEGIN TESTS
print('Test 1 ... ', end = '')
times = [2, 2, 2, 2, 3, 3, 2]
assigns = [0, 0, 0, 0, 1, 1, 2]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 8, f'Expected makespan is 8, your code returned: {s}'
print(' passed!')

print('Test 2 ...', end='')
times = [2, 1, 2, 2, 1, 3, 2, 1, 1, 3]
assigns = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 10, f' Expected makespan is 10, your code returned {s}'
print('  passed!')
print('Tests passed: 10 points!')

## END TESTS


# ### Minimizing Makespan
# 
# Given a list $T: [T_1, \ldots, T_n]$ of job times and $m \geq 2$ processors, we wish to find an assignment that minimizes the overall makespan.
# 
# 
# ### Question 3
# 
# What is the number of possible assignments for a problem with $n = 1000$ jobs on $m = 10$ processors?

# YOUR ANSWER HERE

# As you will notice from the answer to the previous question, the number of possible assignments to a typical scheduling problem may well exceed the number of atoms in our Galaxy. Going through each and every one of them to find out the one that will minimize the makespan is impractical.  Furthermore, next module will study NP completeness. We will see that some problems including makespan scheduling are somehow inherently harder to solve on a computer. Thus, there are no known efficient solutions that solve for the optimal solution.
# 
# Therefore, we will (hat tip to the brilliant mathematician/computer scientist Ronald Graham https://en.wikipedia.org/wiki/Ronald_Graham) propose a simple greedy algorithm for makespan minimization.

# ## Greedy Makespan Minimization
# 
# The idea is simple: we go through each job and assign it to the processor that currently has the least load.
# 
# ~~~
# greedy_min_make_span(T, m):
#   # T is an array of n numbers, m >= 2
#   A = [Nil, ... , Nil] # Initialize the assignments to nil (array size n)
#   M = [ 0, 0, ...., 0] # initialize the current load of each processor to 0 (array size m)
#   for i = 1 to n
#     find processor j for which M[j] is the least.
#     A[i] = j
#     M[j] = M[j] + T[i]
#  # Assignment achieves a makespan of max(M[1], .. M[m])
#  return A
# ~~~
# 
# ### Question 4
# 
# What is the running time of the greedy makespan algorithm? What data structure would you use to achieve a running time of $n \log(m)$.

# YOUR ANSWER HERE

# In[3]:


import heapq

class processor:
    def __init__(self, num):
        self.number = num
        self.load = 0
        
    def update_load(self, job_time):
        self.load = self.load + job_time
    
class minHeap:
    def __init__(self, num_processors, num_jobs):
        self.processors = [processor(j) for j in range(num_processors)]
        
        ##PriorityQueue is minHeap of tuples (load, processor) with key = load
        self.priorityQ = []
        self.initialize_priority_queue(num_processors)
        self.assignments = [None]*num_jobs
        
    def insert_processor(self, i):
        this_tuple = (0, i)
        heapq.heappush(self.priorityQ, this_tuple)
        
    def initialize_priority_queue(self, num_processors):
        for i in range(num_processors):
            self.insert_processor(i)
    
    def get_next_processor(self):
        this_tuple = heapq.heappop(self.priorityQ)
        this_processor = self.processors[this_tuple[1]]
        return this_processor
    def add_job(self, job_time, job_num):
        ##Get next processor
        this_processor = self.get_next_processor()
        ##Update Processor Load
        this_processor.update_load(job_time)
        ##Record job assignment
        self.assignments[job_num] = this_processor.number
        ##Reinsert processor with new load
        heapq.heappush(self.priorityQ, (this_processor.load, this_processor.number))
        
        
    def extract_assignments(self):
        return self.assignments
    
    def extract_makespan(self):
        loads = [self.processors[i].load for i in range(len(self.processors))]
        return max(loads)


# ## Problem B: Implement the Greedy Makespan Algorithm

# In[4]:


def greedy_makespan_min(times, m):
    # times is a list of n jobs.
    assert len(times) >= 1
    assert all(elt >= 0 for elt in times)
    assert m >= 2
    n = len(times)
    # please do not reorder the jobs in times or else tests will fail.
    # you can implement a priority queue if you would like.
    # use https://docs.python.org/3/library/heapq.html heapq data structure 
    # Return a tuple of two things: 
    #    - Assignment list of n numbers from 0 to m-1
    #    - The makespan of your assignment
    # your code here
    
    n = len(times)
    priorityQ = minHeap(m, n)
    
    for k in range(n):
        this_load = times[k]
        priorityQ.add_job(this_load, k)
    
    assignments = priorityQ.extract_assignments()
    makespan = priorityQ.extract_makespan()
        
    return(assignments, makespan) 


# In[5]:


## BEGIN TESTS
def do_test(times, m, expected):
    (a, makespan) = greedy_makespan_min(times,m )
    print('\t Assignment returned: ', a)
    print('\t Claimed makespan: ', makespan)
    assert compute_makespan(times, m, a) == makespan, 'Assignment returned is not consistent with the reported makespan'
    assert makespan == expected, f'Expected makespan should be {expected}, your core returned {makespan}'
    print('Passed')
print('Test 1:')
times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7
do_test(times, m, expected)

print('Test 2:')
times = [1]*20 + [5]
m = 5
expected =9
do_test(times, m, expected)

print('Test 3:')
times = [1]*40 + [2]
m = 20
expected = 4
do_test(times, m, expected)
print('All tests passed: 15 points!')
## END TESTS


# ## Question 5
# 
# Construct a set of timings for $n$ jobs with $m \geq 2 $ processors that shows that greedy solution can be strictly worse than the best solution.

# YOUR ANSWER HERE

# In[6]:


def do_test(times, m, expected):
    (a, makespan) = greedy_makespan_min(times,m )
    print('\t Assignment returned: ', a)
    print('\t Claimed makespan: ', makespan)
    assert compute_makespan(times, m, a) == makespan, 'Assignment returned is not consistent with the reported makespan'
    assert makespan == expected, f'Expected makespan should be {expected}, your core returned {makespan}'
    print('Passed')
print('Test 1:')
times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7
do_test(times, m, expected)

print('Test 2:')
times = [1]*20 + [5]
m = 5
expected =9
do_test(times, m, expected)

print('Test 3:')
times = [1]*40 + [2]
m = 20
expected = 4
do_test(times, m, expected)
print('All tests passed: 15 points!')


# ## Analysis of Greedy Makespan Minimization 

# We will now analyze the greedy algorithm and show the following result.
# 
# For arbitrary (positive) times $[T_1, \ldots, T_n]$ and $m\geq 2$ processors.
# Let $A_g$ be the assignment returned by the greedy makespan with makespan value $T_g$.
# Let $A^*$ be the best possible assignment with makespan $T^*$.
# 
# **Theorem**  $T^* \leq T_g \leq \left( 2 - \frac{1}{m} \right) T^*$.
# 
# The first part that $T^* \leq T_g$ is obvious. The greedy algorithm returns _a_ solution whereas we
# claim that $T^*$ is the _best_ solution.
# 
# This theorem proves an amazing result. Although greedy may not always provide the best solution, 
# it is guaranteed to be no worse than $\left(2 - \frac{1}{m}\right)$ times the best possible solution 
# in the worst case. For instance if $m = 3$, then greedy algorithm finds an answer that is no 
# worse than $1.67$ times the best answer.
# 
# The advantage of this result is obvious: the greedy algorithm runs in time $\Theta (n \log(m))$ whereas the
# computing the optimal assignment is a very hard problem for which we know of no efficient algorithm in the worst case.
# 
# To see why this result holds, note the key property that the greedy algorithm satisfies.
# 
# ### Greedy Algorithm Property
# 
# At any point during the execution of the greedy algorithm: 
# 
# - Suppose $i-1$ out of the $n$ jobs have been assigned, and
# - If processor $j$ is selected as the one with the smallest total load so far
# 
# then the total load of processor $j$ must be $\leq $ the average of the job times across the processors: $T_{avg}:\ \frac{1}{m} ( T_1 + \ldots + T_n)$.
# 
# ### Question 6
#  
#  Prove that the above property holds for the greedy algorithm.
# 

# YOUR ANSWER HERE

# Using the property above, we observe the following: 
# 
# > The makespan of the greedy algorithm can be no more than $\frac{1}{m} (T_1 + \ldots + T_n) + T_{max}$ wherein 
# $T_{max}$ is the job that takes the longest to complete.
# 
# The reason for this is simple, consider the processor $j$ that is responsible for taking the longest time after greedy algorithm has finished making its assignment. When the last job was assigned to this processor by the greedy algorithm, its total load was below the overall average $\frac{1}{m} (T_1 + \cdots + T_n)$. However, the when the last job was added to this processor, its total load has to be below $\frac{1}{m} (T_1 + \ldots + T_n) + T_{max}$.
# 
# 
# Now, we make two observations about $T^*$: the makespan of the optimal algorithm.
#  - $T^* \geq T_{max}$. Some processor has to do the longest time job and the makespan has to include that.
#  - $T^* \geq \frac{1}{m} ( T_1 + \cdots + T_n)$. The maximum has to be greater than or equal to the average.
#  
# Combining, we have
# 
# $$T_g \leq T_{max} + \frac{1}{m} (T_1 + \ldots + T_n) \leq T^* + T^* = 2T^*\,.$$
# 
# This proves that the greedy algorithm is no worse than twice the optimal. However, we can improve the analysis by being a bit more careful. 
# 
# __A More Careful Analysis__
# 
# Once again consider the processor j which causes the makespan for the greedy algorithm. Suppose we are at the point where we will add the very last job assigned to this processor (call this job $T_i$). 
# 
# We will note that we can have a better bound for $M_j$:
# $$ M_j \leq \frac{1}{m} (T_1 + \ldots + T_{i-1} + T_{i+1} + \cdots + T_n)\,.$$
# I.e., the average need not include the last job $T_i$ itself. Once we note this, we can also show then that the makespan is  bounded by
# 
# $$T_g \leq \frac{1}{m} (T_1 + \ldots + T_{i-1} + T_{i+1} + \cdots + T_n) + T_i = \frac{1}{m} (T_1 + \cdots + T_m) + \left( 1 - \frac{1}{m}\right) T_i \leq T_{avg} + \left( 1 - \frac{1}{m}\right) T_{max}$$.
# 
# This improves the bound to $T_g \leq T^* + \left(1 - \frac{1}{m}\right)T^* \leq \left( 2 - \frac{1}{m}\right) T^*$. QED!
# 

# ## Sorting Job Times
# 
# The above algorithm assumes that jobs are sorted in arbitrary order. It is in fact an _online_ approach where we make a decision on how to allocate a job as it arrives. Let us consider an _offline_ strategy where we sort the jobs in ascending order smallest size job to largest or vice-versa. 
# 
# ### Question 7
# 
# Using the intuition developed so far, would sorting jobs make a difference to how the greedy algorithm performs? If so, which order should jobs be sorted?

# YOUR ANSWER HERE

# ## Answers to manually graded problems
# 
# ### Answer 1
# There are many ways to express this.
# 
# $M_j = \sum_{ i = 1}^{n} T_i \times [A_i = j] $ wherein the function $[A_i = j]$ equals $1$ if $A_i = j$ and $0$ otherwise. 
# 
# Here is another way to write the same thing.
# 
# $M_j = \sum_{ i \in \{ 1, \ldots, n \} \cap \{ i | A_i = j \}} T_i$
# 
# 
# ### Answer 2
# 
# The times taken by each processor are $M_1 = 4, M_2 = 7, M_3 = 4$. The makespan is $7$.
# 
# A better assignment is as follows:
# 
# $\hat{A}: [ 1, 1, 1, 2, 2, 2, 3]$ this assignment achieves a makespan of $6$.
# 
# 
# ### Answer 3
# 
# Each job can be assignment to one of 10 possible choices in terms of processors. The number of assignments is
# $m^n$ or $10^{1000}$.
# 
# ### Answer 4
# The running time as written is $\Theta(nm)$. However, if we maintain a priority queue for $M$ where the priority is given by its current load, then using extract min, we can get the minimum load processor in $\Theta(1)$. Also, we will need $\Theta(\log(m))$ time to bubble down when the load for processor $M[j]$ goes up.
# 
# ### Answer 5
# 
# Take $n$ jobs of time 1 and one job of time $n$ and schedule it over $m$ processors. The greedy algorithm will have a makespan of roughly $\frac{n}{m} + n$ whereas the best solution is to distribute the first $n$ jobs over
# the $m-1$ processors and then have the last job on the remaining processor, yielding a makespan of $n$.
# 
# #### Answer 6
# 
# Let us assume that processor $k$'s current total job allocation is $M_k$. Let processor $j$ have the minimum total load so far.
# 
# We have that $ M_j \leq M_k$ for all $k \in \{ 1, \ldots, m \}$. Thus, $M_1 + M_2 + \cdots + M_m \geq m M_j$.
# But what is $M_i$: it is the sum of job times that have been assigned to processor $i$. Therefore, the sum of all job times must exceed the sum of the times for the individual processors since each job is assigned to at most one processor.
# 
# The LHS is bounded as follows:
# $$ T_1 + T_2 + \cdots + T_n \geq M_1 + M_2 + \cdots + M_m \geq m M_j \,.$$
# This yields the fact that $M_j \leq \frac{1}{m} \left( T_1 + \cdots + T_n \right)$.
# 
# 
# ### Answer 7
# 
# The jobs should be sorted in descending order for the best performance.  To see why, let us go back to the key property of the greedy algorithm: when it assigns a job to processor j, the total load currently assigned to processor j must be less than the average (total of all job times divided by the number of processors). Thus, let us freeze the algorithm at the point when it assigns a job to the processor j that causes the worst total time (i.e the makespan) to be achieved. Since jobs are sorted in descending order, this job has to be smaller than the largest job $T_{max}$. In fact, a slightly more detailed analysis will show that this job will be less than half the make span of the optimal solution.  
# 

# ## That's All Folks!

# In[ ]:




