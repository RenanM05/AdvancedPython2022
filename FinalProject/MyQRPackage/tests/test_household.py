import unittest
import numpy as np
from QRDecomposition.household import householder_reflection

class TestHouseholderReflection(unittest.TestCase):
    def test_identity(self):
        """The Householder reflection of an identity vector should be identity."""
        v = np.array([1, 0, 0])
        H = householder_reflection(v)
        expected = np.eye(3)
        np.testing.assert_array_almost_equal(H, expected)

    def test_orthogonal(self):
        """The Householder matrix should be orthogonal."""
        v = np.random.rand(3)
        H = householder_reflection(v)
        np.testing.assert_array_almost_equal(np.dot(H, H.T), np.eye(3))

    def test_reflection(self):
        """The reflection of v by its Householder matrix should negate the first component."""
        v = np.random.rand(3)
        H = householder_reflection(v)
        v_reflected = np.dot(H, v)
        v_reflected[0] = -v_reflected[0]
        np.testing.assert_array_almost_equal(v, v_reflected)

if __name__ == '__main__':
    unittest.main()
