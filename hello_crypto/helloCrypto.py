import math

# input: an unencrypted 4 character string
# return: an 8 digit number based on the input string
def cipher(input):
  alphabet = "abcdefghijklmnopqrstuvwxyz" # we use this alphabet to get the indices of characters
  cipher_token = "" # an 8 digit number, an encrypted token
  for i in range(0, len(input)): # for every letter in the input
    cipher_digit = alphabet.find(input[i]) + 10 # grab the index of that char from the alphabet and add an offset to that letter
    cipher_token += str(cipher_digit) # append that 2 digit number to our 8 digit encrypted token
  return int(cipher_token)

# input: an 8 digit number
# return: the remainder of a 20 digit prime and the input
def get_remainder(input):
  prime_num = 48112959837082048697
  temp = int(math.floor(prime_num/input))
  return temp

# PROGRAM ENTRY ---------------------------------------------------------
message1 = "we the people in order to form a more perfect union"
print "Input String to Encrypt: " + message1
message1 = message1.replace(" ","")
token_list = []
enciphered_list = []
remainder_token_list = []
for i in range(0, int(math.floor(len(message1)/4)+1)):
  current_token = message1[0:4]
  token_list.append(current_token)
  message1 = message1.replace(message1[0:4], "")
  enciphered_list.append(cipher(current_token))
  remainder_token_list.append(get_remainder(enciphered_list[i]))

print "----- RESULTS -----"
print "\033[4moriginal\033[0m   \033[4mciphered\033[0m       \033[4mremainder\033[0m"
for i in range(0, len(remainder_token_list)):
  print str("{0:<6}").format(token_list[i]) + "     " + str("{0:<10}").format(enciphered_list[i]) + "     " + str("{0:<20}").format(remainder_token_list[i])
