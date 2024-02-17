import numpy as np

def householder_reflection(v):
    """Create a Householder reflection matrix."""
    u = v / (v[0] + np.copysign(np.linalg.norm(v), v[0]))
    u[0] = 1
    H = np.eye(len(v)) - (2 / np.dot(u, u)) * np.outer(u, u)
    return H

def qr_decomposition(A):
    """Perform QR decomposition of matrix A using Householder reflections."""
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for j in range(n):
        # Create the Householder reflection matrix for column j
        x = R[j:, j]
        H = np.eye(m)
        H[j:, j:] = householder_reflection(x)
        R = np.dot(H, R)
        Q = np.dot(Q, H.T)

    return Q, R

# Example usage:
A = np.random.rand(5, 5)
Q, R = qr_decomposition(A)

print("Q:", Q)
print("R:", R)
