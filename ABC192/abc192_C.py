n=input()
total=0
flag=0
for x,i in enumerate(n):
  if i=="9":
    total+=9
  else:
    if flag:
      total+=9*(len(n)-x)-1
      break
    if x==0:
      flag=1
      total+=int(i)
    else:
      total+=9*(len(n)-x)-1
      break
print(total)