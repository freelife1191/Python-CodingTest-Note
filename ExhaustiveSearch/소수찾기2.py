import math
def solution(n):
  n = n + 1
  is_primes = [True] * n
  max_langth = math.ceil(math.sqrt(n))

  for i in range(2, max_langth):
    if is_primes[i]:
      for j in range(i+i, n, i):
        is_primes[j] = False
  # print([i for i in range(2, n) if is_primes[i]])
  return len([i for i in range(2, n) if is_primes[i]])
