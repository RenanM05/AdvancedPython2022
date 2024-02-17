# test folder will try the follow steps:

@Household 
The test check if 
1. the Householder matrix for a unit vector is an identity matrix
2. the Householder matrix is orthogonal,
3. the Householder matrix properly reflects a vector (negating its first component).

@QRdecomposition
1. test_qr_decomposition checks the decomposition on a 4x4 matrix.
2. test_qr_square_matrix checks the decomposition on a square matrix of size 3x3.
3. test_qr_non_square_matrix checks the decomposition on a non-square matrix of size 3x2.


# Example usage :
A = np.random.rand(5, 5)
Q, R = qr_decomposition(A)

print("Q:", Q)
print("R:", R)
