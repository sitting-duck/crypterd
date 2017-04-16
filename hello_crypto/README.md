Collaboration: Jacob Thias and Ashley Tharp

Babby's first cipher.

The ouput will look something like: 

Input String to Encrypt: we the people in order to form a more perfect union

----- RESULTS -----
  
|original   |ciphered       |remainder           |
|-----------|---------------|--------------------|
|weth       |32142917       |1496844851918       |       
|epeo       |14251424       |3376010694586       |       
|plei       |25211418       |1908379760197       |       
|nord       |23242713       |2070023402047       |       
|erto       |14272924       |3370925245386       |       
|form       |15242722       |3156454591055       |       
|amor       |10222427       |4706608307115       |       
|eper       |14251427       |3376009983918       |       
|fect       |15141229       |3177612585945       |       
|unio       |30231824       |1591467317257       |       
|n          |23             |2091867819003567360 |


The First column is the input string removed of spaces, and broken into 4 character tokens.

The 2nd column is the result of ciphering each 4 character token with a basic ceasar cipher.

The 3rd column is the modulo remainder of the ciphered token with a 20 digit prime number.
