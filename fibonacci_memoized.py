# Comparison of:
#   1. a recursive implementation of a function to calculate the nth
#   number in a fibonacci series
#   2. an implementation that also utilizes memoization to reduce the
#   number of function calls

import time


def fibonacci(n):
  if n < 2: return n
  return fibonacci(n - 1) + fibonacci(n - 2)

memo = {}
def fibonacci_memoized(n):
  if n in memo.keys(): return memo[n]
  if n < 2: return n
  current = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
  memo[n] = current
  return current

# Comparison Tests
for n in (5, 10, 20, 30):
  start = time.perf_counter_ns()
  output = fibonacci(n)
  runtime = time.perf_counter_ns() - start
  print(f"fibonacci  n={n}")
  print(f"    output={output}  runtime(ns)={runtime}\n")

  memo = {}
  start = time.perf_counter_ns()
  output = fibonacci_memoized(n)
  runtime = time.perf_counter_ns() - start
  print(f"fibonacci_memoized  n={n}")
  print(f"    output={output}  runtime(ns)={runtime}\n")