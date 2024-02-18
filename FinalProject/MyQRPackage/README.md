# MyQRPackage

A package for QR decomposition using Householder reflections.

## Installation

```bash
pip install MyQRPackage
```
<https://pypi.org/project/MyQRPackage/>

# Example usage :
Create a python file `use_myqrpackage.py` with the following code below
```python
import numpy 
from MyQRPackage.QRDecomposition import qr_decomposition

A = numpy.random.rand(5, 5)
Q, R = qr_decomposition(A)
print("Q:", Q)
print("R:", R)
```
Run
```bash
python3 use_myqrpackage.py
```

# Other information:

The main content of MyQRPackage is represented in a tree format below:

```markdown
.travis.yml
setup.py
MyQRPackage/
│
├── QRDecomposition/
│   ├── __init__.py
│   ├── household.py
│   └── qr_decomposition.py
│
├── tests/
│   ├── __init__.py
│   ├── test_household.py
│   └── test_qr_decomposition.py
│
│── dist/
│── MyQRPackage.egg-info/
└── README.md
```

The other folders, like: * dist, MyQRPackage.egg-info* is due to the command 
```bash
python setup.py sdist bdist_wheel
```
Notice that the code was uploaded to my PyPI using twine:

```bash
twine upload dist/*
```

If you download this code from the source, I recommend you to test it using the following command:
```bash
$pytest
```
Run `pytest` in the main root folder, e.g., `python3 MyQRPackage/pytest`. 


>> Travis CI
It is a hidden file called `.travi.yml`. This file is at the same level as `MyQRPackage`


## Testing folder 
This part is designed to test the robustness of the code. 
I list below what it does: 

@Household (test_household.py)
1. the Householder matrix for a unit vector is an identity matrix
2. the Householder matrix is orthogonal,
3. the Householder matrix properly reflects a vector (negating its first component).

@QRdecomposition (test_qr_decomposition.py)
1. `test_qr_decomposition` checks the decomposition on a 4x4 matrix.
2. `test_qr_square_matrix` checks the decomposition on a square matrix of size 3x3.
3. `test_qr_non_square_matrix` checks the decomposition on a non-square matrix of size 3x2.
