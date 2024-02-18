# MyQRPackage 

'A package for QR decomposition using Householder reflections.'

# Installation
```markdown
Use `pip install -i https://test.pypi.org/simple/ MyQRPackage` to install MyQRPackage.

# Example usage :
```python
import numpy 
import MyQRPackage
from MyQRPackage.QRDecomposition import qr_decomposition

A = numpy.random.rand(5, 5)
Q, R = qr_decomposition(A)
print("Q:", Q)
print("R:", R)
```

# Other information:

The main content of MyQRPackage is represented in a tree format below:
"""
MyQRPackage/
    QRDecomposition/
        __init__.py
        household.py
        qr_decomposition.py
    tests/
        __init__.py
        test_household.py
        test_qr_decomposition.py
    setup.py
    README.md
"""

## Testing folder 
This part is designed to test the robustness of the code. 
I list below what it does: 

@Household 
The test check if 
1. the Householder matrix for a unit vector is an identity matrix
2. the Householder matrix is orthogonal,
3. the Householder matrix properly reflects a vector (negating its first component).

@QRdecomposition
1. test_qr_decomposition checks the decomposition on a 4x4 matrix.
2. test_qr_square_matrix checks the decomposition on a square matrix of size 3x3.
3. test_qr_non_square_matrix checks the decomposition on a non-square matrix of size 3x2.
