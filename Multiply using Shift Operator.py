a = 20
b = -5
res = 0
temp = b
while True:
     if temp & 1 and temp > 0:          
          res += a
     if temp & 1 and temp < 0:
          res -= a
          temp >>= 1
     if temp == 0 or temp == -1:
          break
     a <<= 1
     temp >>= 1
print('Multiplication of {} and {} is {}'.format(a,b,res ))