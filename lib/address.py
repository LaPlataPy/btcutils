import binascii
import hashlib

try:
    from Crypto.Hash.RIPEMD import RIPEMD160Hash as RIPEMD160
except ImportError:
    #changed in 2.71a
    from Crypto.Hash import RIPEMD160
    RIPEMD160 = RIPEMD160.new

from .ECC import Secp256k1


class BitcoinAddress(object):

    def __init__(self, private):
        self.private = private
        self._generate()

    def _generate(self):
        self.public_cords = Secp256k1.multiply(self.private)
        self.public_hex = "04" + "%064x" % self.public_cords[0] + "%064x" % self.public_cords[1]

    @property
    def public_compressed(self):
        if self.public_cords[1] % 2 == 1:
            return "03" + str(hex(self.public_cords[0])[2:-1]).zfill(64)
        else:
            return "02" + str(hex(self.public_cords[0])[2:-1]).zfill(64)

    @property
    def address(self):
        pko = self.public_compressed
        pubkey = binascii.hexlify(pko)
        pubkey2 = hashlib.sha256(binascii.unhexlify('04' + pubkey)).hexdigest()
        pubkey3 = RIPEMD160(binascii.unhexlify(pubkey2)).hexdigest()
        pubkey4 = hashlib.sha256(binascii.unhexlify('00' + pubkey3)).hexdigest()
        pubkey5 = hashlib.sha256(binascii.unhexlify(pubkey4)).hexdigest()
        pubkey6 = pubkey3 + pubkey5[:8]
        pubnum = int(pubkey6, 16)
        pubnumlist = []
        while pubnum != 0:
            pubnumlist.append(pubnum % 58)
            pubnum /= 58
        address = ''
        for l in ['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'[x] for x in pubnumlist]:
            address = l + address
        return '1' + address