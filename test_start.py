import pytest
def add(a,b):
  return a+b

def test_plan():
  output=add(2,3)
  assert output==5
