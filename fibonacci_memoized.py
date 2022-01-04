# Comparison of:
#   1. a recursive implementation of a function to calculate the nth
#   number in a fibonacci series
#   2. an implementation that also utilizes memoization to reduce the
#   number of function calls

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

# Comparison Tests
print("\nComparison Tests\n================")
for n in (5, 10, 20, 30):
  print(f"n={n}")
  start = time.perf_counter_ns()
  output = fibonacci_recursive(n)
  runtime = time.perf_counter_ns() - start
  print(f"fibonacci_recursive  output={output}  runtime(ns)={runtime}")

  memo = {}
  start = time.perf_counter_ns()
  output = fibonacci_memoized(n)
  runtime = time.perf_counter_ns() - start
  print(f"fibonacci_memoized  output={output}  runtime(ns)={runtime}")
  print()

# Observations
# ============
# fibonacci_recursive
#   runtime complexity --> O(ϕ^2), ϕ is about 1.618 (golden ratio)
#   space complexity ----> O(n)
# fibonacci_memoized
#   runtime complexity --> O(n)
#   space complexity ----> O(n)