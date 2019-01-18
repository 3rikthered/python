#######################
# verification method #
#######################

def check():
  string = input('Enter a 16-digit binary: ')
  string = string.strip()
#require string length to be 16
  if len(string) != 16:
    print('Use 16 chars: ')
    return False
#require characters to only be 0 and 1
  if not all(i in '10' for i in string):
    print('Use only 0 or 1: ')
    return False
  return string

##################
# create strings #
##################

#first string
while True:
  x = check()
  if x:
    break

#second string
while True:
  y = check()
  if y:
    break

#######
# AND #
#######

print("\nAND\n\n" + x + "\n" + y + "\n----------------")

# if the bit at n position in both x and y are equal to 1,
# the AND value will also be 1
for (xval, yval) in zip(x,y):
  if xval == '1' and yval == '1':
    print ("1", end="")
  else: print ("0", end="")

######
# OR #
######

print ("\n\nOR\n\n" + x + "\n" + y + "\n----------------")


# if the bit at n position in either x or y are equal to 1,
# the OR value will also be 1
for (xval, yval) in zip(x,y):
  if xval == '1' or yval == '1':
    print ("1", end="")
  else:
    print ("0", end="")

#######
# XOR #
#######

print ("\n\nXOR\n\n" + x + "\n" + y + "\n----------------")

# if the bit at n position in either x or y are equal to 1, but not both,
# the AND value will also be 1

for (xval, yval) in zip(x,y):
  if (xval == '1' or yval == '1') and (xval != yval):
    print ("1", end="")
  else:
    print ("0", end="")

print ("\n")
