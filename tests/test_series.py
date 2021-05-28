from math_series.series import fibonacci, lucas

def test_connect():
  assert fibonacci

def test_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_two():
  actual = fibonacci(8)
  expected = 21
  assert actual == expected

def test_three():
  actual = fibonacci(9)
  expected = 34
  assert actual == expected

def test_four():
  actual = fibonacci(10)
  expected = 55
  assert actual == expected

def lucas_one():
  actual = lucas(10)
  expected = 17
  assert actual == expected