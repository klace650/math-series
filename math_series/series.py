def fibonacci(n):
  """
so this function just takes in a number (n)
and returns the fibonacci value for that number
  """
  if n <= 1:
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
  """
  this function returns the same but as a lucas number.
  """
  pass