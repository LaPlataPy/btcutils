from lib.address import BitcoinAddress


if __name__ == '__main__':
    private = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
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