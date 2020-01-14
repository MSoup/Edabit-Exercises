def additive_persistence(n):
  def getNewTotal(num):
    return sum([int(i) for i in str(num)])

  #First iteration 1
  count = 0
  #Keep going until len(n) == 1
  #Preserve original n for good practice
  newN = n

  while len(str(newN)) != 1:
    newN = getNewTotal(newN)
    #Increase count every loop
    count += 1

  return count

def multiplicative_persistence(n):
  def getNewTotal(num):
    product = 1
    for i in str(num):
      product *= int(i)
    return product

  #First iteration 0
  count = 0
  #Keep going until len(n) == 1
  #Preserve original n for good practice
  newN = n

  while len(str(newN)) != 1:
    newN = getNewTotal(newN)
    #Increase count every loop
    count += 1

  return count


print(additive_persistence(77))
print(multiplicative_persistence(77))