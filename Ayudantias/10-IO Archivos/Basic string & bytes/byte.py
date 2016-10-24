characters = "ñandú"
byte = characters.encode("latin1", errors = 'replace')

# Codificamos de distintas formas el mismo string
print(characters.encode("latin1", errors = 'replace'))
print(characters.encode("ascii", errors = 'replace'))
print(characters.encode("ascii", errors = 'xmlcharrefreplace'))


print('-'*30)
# Lo bytes podemos indexarlos y sumarlos

print(byte)
print(byte[1])
print(byte + b'\x67')
# Veamos como afecta decodificarlos de forma distinta
print(byte.decode("latin1"))
print(byte.decode("ascii", errors = 'ignore'))

print('-'*30)

little = int.from_bytes(byte, byteorder='little')
print(little)
big = little.to_bytes(5, 'big')
print(big.decode("latin1"))

print('-'*30)
b = bytearray(b'abcdef')
print(b)
b[4] = 120
b.extend(b'bers')
print(b)
