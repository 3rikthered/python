alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

phrase = "There is a theory which states that if ever anyone discovers exactly what the universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable."
key = "RESTAURANT"

# Numeric index to cycle through, based on the key; initialized at first character
index = 0

# Table to place the encrypted characters in
encryptedArray = []

# Iterate through the phrase
for character in phrase:

  # Searches through the alphabet and assigns the value associated with the character in the phrase
  keyValue = alphabet.find(character.upper())
    
  # Only continues encryption process for values found in the alphabet. Everything else gets discarded.
  if keyValue != -1:

    # Adds the value of the letter in the key to the value of the character in the phrase
    keyValue += alphabet.find(key[index])

    # If the keyValue is now greater than the length of the alphabet, modulo function acts as a wrap-around
    keyValue %= len(alphabet)

    # Adds the letter from the alphabet associacted with the new keyValue into the encrypted array
    encryptedArray.append(alphabet[keyValue])

    #move to next letter in key
    index += 1

   # Ensure key continually loops until the end of the phrase
    if index == len(key):
      index = 0
  
# Print out the encrypted array as a string
print(''.join(encryptedArray))
