# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2oC8k1b274ifoVzt9LmetjPlJFMnvc0
"""

class math:
  def __init__(self,x,n):
      self.x = x
      self.n = n
  def power(self):
    po = 1
    for i in range(n):
      po *= self.x
    return po     
x,n = map(int,input().split())      
p = math(x,n)
print(p.power())