def checkPrime(number):
  """
  Tests if number is prime
  Args:
    number: float
  Returns:
    bool
  """
  is_prime = True
  for num in range(2, number):
    if number % num == 0:
      is_prime = False
  return is_prime

assert(not checkPrime(25))
assert(checkPrime(71))
print("OK!")