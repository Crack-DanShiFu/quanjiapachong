from numpy import *
import numpy as np
from fractions import Fraction


#
# a = Fraction(4, 15)
# b = Fraction(2, 5)
# c = Fraction(1, 4)
#
# M = np.array([
#     [0, b, 2 * b, 0],
#     [a, 0, 0, b],
#     [a, 0, 0, b],
#     [a, 0.5, 0, 0]]
# )
# # M = 4 / 5 * M
# c = np.array(
#     [[c],
#      [c],
#      [c],
#      [c]
#      ]
# )
# for i in range(20):
#     c = np.dot(M, c) + np.array(
#         [[Fraction(1, 5)],
#          [0],
#          [Fraction(1, 5)],
#          [0]
#          ]
#     )
# print(c)
def Normalize(data):
    mx = max(data)
    return data / mx


h = np.array([[1],
              [1],
              [1],
              [1]]
             )
L = np.array([[0, 1, 1, 1],
              [1, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 1, 0], ]

             )
Lt = np.transpose(L)

for i in range(9):
    lth = np.dot(Lt, h)
    a = Normalize(lth)
    La = np.dot(L, a)
    h = Normalize(La)

print(h)
print('')
print(a)
