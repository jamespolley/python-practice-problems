"""
Small library for generating and/or working with arithmetic sequences.

Arithmetic sequence -> a sequence of numbers such that the difference between the consecutive terms is constant.

E.g. {3, 8, 13, 18, 23, ...} is an arithmetic sequence with a common difference of 5.
For more info: https://en.wikipedia.org/wiki/Arithmetic_progression
"""


def generate_arith_seq(a1, d, n):
  """Generates a list containing a finite arithmetic sequence, given:
  - value of the 1st term (a1),
  - common difference (d), AND
  - index of the final term(n), 1st term being 1
  ---  
  Raises an exeption if n is not 1 or greater."""
  if n < 1:
    raise Exception("n must be 1 or greater.")
  return [a1 + d*n for n in range(n)]

def arith_seq_find_vars(arith_seq):
  """Given a list containing a finite arithmetic sequence, finds the variables:
  - value of the final term (an),
  - value of the 1st term (a1),
  - common difference (d), AND
  - index of the final term (n), 1st term being 1
  ---
  Raises an exception if arithmetic sequence is invalid."""
  a1 = arith_seq[0]
  d = arith_seq[1] - arith_seq[0]
  n = len(arith_seq)
  if generate_arith_seq(a1, d, n) != arith_seq:
    raise Exception("Arithmetic sequence is not valid.")
  an = arith_seq_solve_unknown(None, a1, d, n)
  return an, a1, d, n

def arith_seq_solve_unknown(an=None, a1=None, d=None, n=None):
  """Given that the other variables are known, solves for:
  - value of the nth term (an),
  - value of the 1st term (a1),
  - common difference (d), OR
  - index of term n (n), 1st term being 1
  ---
  Raises an exception if too few known variables are given."""
  known_vars = sum([True for arg in (an, a1, d, n) if arg is not None])
  if known_vars < 3:
    raise Exception("Three known variables are required.")  
  if an is None: # Solve for an
    return a1 + (d * (n - 1))
  if a1 is None: # Solve for a1
    return an - (d * (n - 1))
  if d is None: # Solve for d
    return (an - a1) // (n - 1)
  if n is None: # Solve for n
    return ((an - a1) // d) + 1


# Tests
if __name__ == "__main__":
  print("\nTESTS\n")

  print("generate_arith_seq")
  print("==================")
  a1 = 5
  d = -3
  n = 8
  print(f"Variables: a1={a1}, d={d}, n={n}")
  print("  Result:", generate_arith_seq(a1, d, n), "\n")

  print("arith_seq_find_vars")
  print("===================")
  arith_seq = [1, 3, 5, 7, 9]
  print("Given the finite arithmetic sequence: {1, 3, 5, 7, 9}")
  an, a1, d, n = arith_seq_find_vars(arith_seq)
  print(f"  Result: an={an}, a1={a1}, d={d}, n={n}")
  arith_seq = [1, 4, 7, 11]
  print("Given the INVALID finite arithmetic sequence: {1, 4, 7, 11}")
  print("  Result: ", end="")
  try:
    an, a1, d, n = arith_seq_find_vars(arith_seq)
    print("VALID arithmetic sequence\n")
  except:
    print("INVALID arithmetic sequence\n")

  print("arith_seq_solve_unknown")
  print("=======================")
  an = 15
  a1 = 3
  d = 3
  n = 5
  print("Given the arithmetic sequence: {3, 6, 9, 12, 15, ...}")
  print(f"Variables: an={an}, a1={a1}, d={d}, n={n}")
  result = arith_seq_solve_unknown(a1=a1, d=d, n=n)
  print(f"  When an is unknown, result: an={result}")
  result = arith_seq_solve_unknown(an=an, d=d, n=n)
  print(f"  When a1 is unknown, result: a1={result}")
  result = arith_seq_solve_unknown(an=an, a1=a1, n=n)
  print(f"  When d is unknown, result: d={result}")
  result = arith_seq_solve_unknown(an=an, a1=a1, d=d)
  print(f"  When n is unknown, result: n={result}\n")