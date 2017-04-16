import math

def cipher(input):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in range(0, len(input)):
    cipherDigit = alphabet.find(input[i]) + 10
    print "got cipherDigit: " + str(cipherDigit)
  print "end cipher token"

message1 = "we the people"
message1 = message1.replace(" ","")
print message1
token_list = []
enciphered_list = []
for i in range(0, int(math.floor(len(message1)/4)+1)):
  current_token = message1[0:4]
  token_list.append(current_token)
  message1 = message1.replace(message1[0:4], "")
  enciphered_list.append(cipher(current_token))
  
