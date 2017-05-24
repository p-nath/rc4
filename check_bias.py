def main():
  z0 = [0 for i in xrange(256)]
  z1 = [0 for i in xrange(256)]
  z2 = [0 for i in xrange(256)]
  z3 = [0 for i in xrange(256)]
  z4 = [0 for i in xrange(256)]
  z5 = [0 for i in xrange(256)]

  with open('output.txt', 'r') as fin:
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
  main()