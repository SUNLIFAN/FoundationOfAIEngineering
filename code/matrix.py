import numpy as np

A =  np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])# initialize matrix A

print ('matrix A:')

print (A)

 

A_inv =  np.linalg.inv(A)# compute the inverse of A

print ('inverse of A:')

print (A_inv)

 

print ('vector b:')

b =  np.array([[3], [-2], [13.5]])# initialize vector b

print (b)

 

print ('solve x:')

x =  np.dot(A_inv, b)#solve x

print (x)


