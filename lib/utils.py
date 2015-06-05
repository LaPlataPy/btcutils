

def modular_inverse(a, n):
    """
    Used for division in elliptic curves. Very important in RSA/ECDSA algorithms.
    It uses EGCD.
    Extended Euclidean Algorithm:
        - http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
        - http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n