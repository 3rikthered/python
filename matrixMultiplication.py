# Create first matrix, 3x2
matrixA = [[1, 2],
           [3, 4],
           [5, 6]]

# Create second matrix, 2x4
matrixB = [[9, 8, 7, 6],
           [5, 4, 3, 2]]

# iterates through each column in matrixB for each row in matrixA,
# multiplies every paired value in the locations
# then adds the multiplied pairs

matrixResultA = [[sum(x*y
                  for x,y in zip(row, column))
                  for column in zip(*matrixB)]
                  for row in matrixA]

matrixResultB = [[sum(x*y
                  for x,y in zip(row, column))
                  for column in zip(*matrixA)]
                  for row in matrixB]

print('')

for value in matrixResultA:
  print(value)

print('')

for value in matrixResultB:
  print(value)

print('')

print ('AB and BA are', 'equal' if (matrixResultA == matrixResultB)
                                else 'unequal')
