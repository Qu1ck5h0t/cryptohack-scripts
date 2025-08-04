# worked first try. EZ
ints=[14,6,11]
p = 29
def EulersCriterion(input, p):
  out = []
  for i in input:
    if (i ** ((p-1)//2))%p == 1:
      out.append(i)
  return out
def TonelliShanks(inp, p):
  n = p - 1
  s = 0
  while n % 2 == 0:
    n = n//2
    s = s + 1
  a = 1
  while (a ** ((p-1)//2))%p == 1:
    a = a + 1
  m = s
  c = a**n%p
  t = inp**n%p
  R = inp**((n+1)//2)%p
  if t == 0:
    return 0
  elif t == 1:
    return R
  while t != 1:  
    i = 0
    while ((t**2**i)%p != 1):
      i = i + 1
    b = (c ** 2 ** (m-i-1))%p
    R = R * b%p
    t = t * (b**2)%p
    c = b ** 2%p
    m = i
  return R

ints = EulersCriterion(ints, p)
for i in range(len(ints)):
  ints[i] = TonelliShanks(ints[i], p)
print(ints)
