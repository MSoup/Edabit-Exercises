#Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the answer is only 1 digit long. 

def sum_dig_prod(*argv):
  #Get Product Function
  def getNewTotal(num):
    product = 1
    for i in str(num):
      product *= int(i)
    return product

  #Get initial sum
  total = sum([i for i in argv])
  
  while len(str(total)) != 1:
    total = getNewTotal(total)

  return total

print(sum_dig_prod(16, 28))