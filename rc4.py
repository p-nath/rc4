# 1 <= keylength <= 256

import sys
import os
import argparse

def KSA(key):
  keylength = len(key)
  s = range(256) # list[0, 1, ... 255]
  j = 0
  for i in xrange(256):
    j = (j + s[i] + key[i % keylength]) % 256
    # swap
    s[j], s[i] = s[i], s[j]
  return s

def PRGA(s, pt_length):
  j = 0
  i = 0
  kstream = []
  while pt_length - i > 0:
    i = (i + 1) % 256
    j = (j + s[i]) % 256 
    # swap
    s[i], s[j] = s[j], s[i]
    k = s[(s[i]+s[j]) % 256]
    kstream.append(k)
  return kstream

def RC4(plaintext, key, fout, check_bias):
  key_ascii = [ord(i) for i in key]

  s = KSA(key_ascii)
  i = 0
  keystream = PRGA(s, len(plaintext))
  # print keystream
  if check_bias:
    for i in xrange(len(keystream)):
      fout.write(str(keystream[i]) + ' ')
    fout.write('\n')
  else:
    for i in xrange(len(plaintext)):
      sys.stdout.write(format(ord(plaintext[i]) ^ keystream[i], '02x'))
      #fout.write(format(ord(plaintext[i]) ^ keystream[i], '0b'))
 

def ParseArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', action="store_true", dest="checkbias", default=False,
                     help='Set to 1 if you want to check bias in rc4.')
  parser.add_argument('-o', action="store", dest="fout", default="output.txt",
                     help='Specify output file to store encrypted cipher text')
  #parser.add_argument('-i', action="store", default=True)
  #parser.add_argument('-k', action="store", dest="key", type=str)
  return parser.parse_args()

def check_bias(foutname):
  z0 = [0 for i in xrange(256)]
  z1 = [0 for i in xrange(256)]
  z2 = [0 for i in xrange(256)]
  z3 = [0 for i in xrange(256)]
  z4 = [0 for i in xrange(256)]
  z5 = [0 for i in xrange(256)]

  with open(foutname, 'r') as fin:
    for line in fin:
      ct = [int(x) for x in line.split()]
      #print ct
      z0[ct[0]] += 1
      z1[ct[1]] += 1
      z2[ct[2]] += 1
      z3[ct[3]] += 1
      z4[ct[4]] += 1
      z5[ct[5]] += 1
  expected = float(1)/256
  print "Expected uniform probability is 1/256 =", expected
  print "Pr[0] for byte 1:", float(z0[0])/200000
  print "Pr[0] for byte 2:", float(z1[0])/200000
  print "Pr[0] for byte 3:", float(z2[0])/200000
  print "Pr[0] for byte 4:", float(z3[0])/200000
  print "Pr[0] for byte 5:", float(z4[0])/200000 
  print "Pr[0] for byte 5:", float(z5[0])/200000
  print "The second byte is biased towards 0 (2/256)."

if __name__ == '__main__':
  args = ParseArgs()
  checkbias = args.checkbias
  foutname = args.fout

  if checkbias:
    pt = 'Hello darkness my old friend.'
    n = 128
    fout = open(foutname, 'w')
    for i in range(200000):
      key = os.urandom(n)
      RC4(pt, key, fout, checkbias)
    fout.close()
    check_bias(foutname)
  else:
    key = 'Key'
    pt = 'Plaintext'
    RC4(pt, key, -1, checkbias)


  


