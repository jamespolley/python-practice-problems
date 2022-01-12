"""
Comparison of:
  1. a recursive implementation of a function to calculate the nth
  number in a fibonacci series
  2. an implementation that also utilizes memoization to reduce the
  number of function calls
  3. an iterative implementation
"""

import time


def fibonacci_recursive(n):
  if n < 2: return n
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

memo = {}
def fibonacci_memoized(n):
  if n in memo.keys(): return memo[n]
  if n < 2: return n
  current = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
  memo[n] = current
  return current

def fibonacci_iterative(n):
  prev = 0
  curr = 1
  for i in range(1, n):
    next = prev + curr
    prev = curr
    curr = next
  return curr


# Comparison Tests
if __name__ == "__main__":
  print("\nCOMPARISON TESTS\n================")
  for n in (1, 5, 10, 20, 30):
    print(f"n={n}")
    start = time.perf_counter_ns()
    output = fibonacci_recursive(n)
    runtime = time.perf_counter_ns() - start
    print(f"fibonacci_recursive  output={output}  runtime(ns)={runtime}")

    memo = {}
    start = time.perf_counter_ns()
    output = fibonacci_memoized(n)
    runtime = time.perf_counter_ns() - start
    print(f"fibonacci_memoized   output={output}  runtime(ns)={runtime}")

    start = time.perf_counter_ns()
    output = fibonacci_iterative(n)
    runtime = time.perf_counter_ns() - start
    print(f"fibonacci_iterative  output={output}  runtime(ns)={runtime}")
    print()

# Observations
# ============
# fibonacci_recursive()
#   Runtime complexity --> O(ϕ^2), ϕ is about 1.618 (golden ratio)
#   Space complexity ----> O(n)
#   Conclusion: Requires the least amount of code and is the easiest to
#     read/understand, but runtime becomes increasingly slower as n
#     increases, because function calls with identical inputs are being
#     repeated.
# 
# fibonacci_memoized()
#   Runtime complexity --> O(n)
#   Space complexity ----> O(n)
#   Conclusion: Requires more memory than fibonacci_recursive(), but
#     runtime improves dramatically as n increases, because memoization
#     is used to save results, and therefore execution of function
#     calls with identical inputs is avoided.
# 
# fibonacci_iterative
#   Runtime complexity --> O(n)
#   Space complexity ----> O(1)
#   Conclusion: Requires the least memory and has the fastest runtime
#     by far (except for when n is very small).