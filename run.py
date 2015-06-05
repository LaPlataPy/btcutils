from lib.address import BitcoinAddress

"""
Resources:
https://github.com/wobine/blackboard101/blob/master/EllipticCurvesPart4-PrivateKeyToPublicKey.py
https://github.com/wobine/blackboard101/blob/master/EllipticCurvesPart5-TheMagic-SigningAndVerifying.py
https://github.com/bitcoin/secp256k1
http://es.wikipedia.org/wiki/RIPEMD-160
https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
http://crypto.stackexchange.com/questions/18965/is-secp256r1-more-secure-than-secp256k1
http://www.hyperelliptic.org/tanja/vortraege/20130531.pdf
https://es.bitcoin.it/wiki/Secp256k1
http://bitcoin.stackexchange.com/questions/21907/what-does-the-curve-used-in-bitcoin-secp256k1-look-like
http://bitcoin.stackexchange.com/questions/8702/if-sha256-and-or-ripemd-160-were-broken-would-all-bitcoin-addresses-be-compromi?rq=1
https://en.bitcoin.it/wiki/Script#Standard_Transaction_to_Bitcoin_address
http://bitcoin.stackexchange.com/questions/5021/how-do-you-get-the-op-hash160-value-from-a-bitcoin-address
https://en.bitcoin.it/wiki/Technical_background_of_Bitcoin_addresses
https://brainwallet.org/
https://blockchain.info/qr?data={address}?amount={amount}
http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
"""

if __name__ == '__main__':
    private = 1234567
    btc_address = BitcoinAddress(private)
    print ">>>>>>>>>>>> PRIVATE KEY"
    print private
    print ">>>>>>>>>>>> PUBLIC KEY X y Y"
    print btc_address.public_cords
    print ">>>>>>>>>>>> PUBLIC KEY HEX"
    print btc_address.public_hex
    print ">>>>>>>>>>>> PUBLIC KEY COMPRESSED"
    print btc_address.public_compressed
    print ">>>>>>>>>>>> PUBLIC KEY ADDRESS"
    print btc_address.address