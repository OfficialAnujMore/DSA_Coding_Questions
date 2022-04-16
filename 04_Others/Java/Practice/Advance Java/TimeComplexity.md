1. Time taken by an algorithm as a function of the length of input

2. Consider the biggest power available in a function as a function.
   1. f(n) = 3n^2 + 5n = O(n^2)
   2. f(n) = n + nlog(n) = O(n), because n will always be greater than nlog(n)
   3. f(n) = 3n^3 + 5n^5 = O(n^5)
   4. f(n) = 100 = O(1)

3. Examples
    1. O(n) = n/4, (n+100)/4, 5n + 3log(n)
    2. O(n2) = n^2/1000, 3n^2+ nog(n)

4. 

    Length (n)              Time complexity
  1. <=[10-11]              O(n!), O(n^6)
  2. < [15-18]              O(2^n x n^2) 
  3. <100                   O(n^4)
  4. <400                   O(n^3)
  5. <2000                  O(n^2 x logn)
  6. <10^4                  O(n^2)
  7. <10^6                  O(nlogn)
  8. <10^8                  O(n!), O(logn)