#Algoritmo de conversiones binarias

import struct
import math

a = math.pi

def float_to_bin(num):			
  return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
  return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

numero=float_to_bin(a)
print (numero[0:15])

binary = 1010101
b = bin(binary)
print (bin_to_float (b))