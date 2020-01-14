def can_see_stage(seats):
  for col in range(len(seats[0]) - 1):
    for row in range(len(seats)):
      if seats[col][row] >= seats[col + 1][row]:
        return False
  return True


print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))

