from .utils import modular_inverse


class ElitpicCurve(object):

    @classmethod
    def add(cls, a, b):
        """
        More info here: 
            - http://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication

        modular_inverse is used for division
        """
        lambda_addition = ((b[1] - a[1]) * modular_inverse(b[0] - a[0], cls.p)) % cls.p
        x = (lambda_addition * lambda_addition - a[0] - b[0]) % cls.p
        y = (lambda_addition * (a[0] - x) - a[1]) % cls.p
        return (x, y)

    @classmethod
    def double(cls, a):
        """
        More info here: 
            - http://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication

        modular_inverse is used for division
        """
        lambda_double = ((3 * a[0] * a[0] + cls.a) * modular_inverse((2 * a[1]), cls.p)) % cls.p
        x = (lambda_double * lambda_double - 2 * a[0]) % cls.p
        y = (lambda_double * (a[0] - x) - a[1]) % cls.p
        return (x, y)

    @classmethod
    def multiply(cls, scalar):
        """
        IMPORTANT: scalar should be in hex format

        More info:
            - http://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
            - https://github.com/wobine/blackboard101/blob/master/EllipticCurvesPart4-PrivateKeyToPublicKey.py
        """
        if scalar == 0 or scalar >= cls.N: 
            raise Exception("Invalid Scalar/Private Key")

        scalar_bin = str(bin(scalar))[2:]
        Q = cls.G
        for i in range (1, len(scalar_bin)):
            Q = cls.double(Q);
            if scalar_bin[i] == "1":
                Q = cls.add(Q, cls.G);
        return (Q)


class Secp256k1(ElitpicCurve):
    """
    Specific Koblitz curve parameters extracted from: http://www.secg.org/sec2-v2.pdf
    Defined by T = (p, a, b, G, n, h)
    Where:
    p: big proven prime
    a: parameter of E: 'y**2 = x**3 + ax + b'
    b: parameter of E: 'y**2 = x**3 + ax + b'
    G(x,y): generator point used for the multiplication step
    N: number of points in the field
    h: cofactor used
    """
    p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1
    a = 0
    b = 7
    G = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 
         32670510020758816978083085130507043184471273380659243275938904335757337482424)
    N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    h = 1