#Metodo de punto flotante doble
import struct

getBin = lambda x: x > 0 and "00" + str(bin(x))[2:] or "11" + str(bin(x))[3:]

def floatToBinary64(value):
  val = struct.unpack('Q', struct.pack('d', value))[0]
  return getBin(val)

binstr = floatToBinary64(0.4)
print("Punto Flotante Doble Precisionn de 0.4:", binstr)

#0011111111011001100110011001100110011001100110011001100110011010
