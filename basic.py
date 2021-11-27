num = 2**68
_temp = 0
text = "Fail\n"

for i in range(500000):
  num+=1
  _temp = num
  print(num)
  while True:
    if num % 2==0:
      num = num/2
    elif num %2==1:
      num=num*3+1
    if num==1:
      break
  num = _temp