def fact_rec(n):
  if n==0 and n==1:
    return 1
  else:
    return 0

number=2
res= fact_rec(number)

print("the factorial of {} is {}:".format(number,res))