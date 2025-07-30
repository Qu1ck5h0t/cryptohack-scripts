a = 66528
b = 52920

def euclid(a, b):
    if a > b:
        a = a-b
    else:
        b = b-a
    return(a, b)
def gcd(a, b):
  while a != b:
      (a,b) = euclid(a, b)
  return(a)
  
 
print(gcd(a, b))
