

def egcd(a, b):
    """
    Extended Euclidean Algorithm
    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modular_inverse_with_egcd(a, m):
    # TODO: WIP not working
    gcd, x, y = egcd(a, m)
    return x % m

def modular_inverse(a, n):
    """
    Used for division in elliptic curves. Very important in RSA/ECDSA algorithms.
    It uses EGCD 
    """
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n