# caeser-cipher
A  python fonction that encrypt a message using  the CEASER CIPHER  method

The Caesar cipher is a simple type of substitution cipher that involves shifting each letter in the plaintext alphabet by a certain number of positions. It is named after Julius Caesar, who used it in his private correspondence.

Encryption

To encrypt a message using the Caesar cipher, you first need to determine the shift. The shift is the number of positions by which each letter in the plaintext alphabet will be shifted. For example, if you choose a shift of 3, then A will be replaced by D, B will become E, and so on.

Once you have determined the shift, you can use the following table to encrypt your message:

| Plaintext alphabet | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
| Encrypted alphabet | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

To encrypt a message, simply replace each letter in the plaintext with the corresponding letter in the encrypted alphabet. For example, if you want to encrypt the message "Hello, world!", you would use the following steps:

Determine the shift. For this example, let's use a shift of 3.
Replace each letter in the plaintext with the corresponding letter in the encrypted alphabet. For example, "H" becomes "K", "e" becomes "h", and so on.
The encrypted message is "Khoor, zruog!".

Decryption

To decrypt a message that has been encrypted using the Caesar cipher, you simply reverse the process. First, determine the shift. Then, replace each letter in the encrypted alphabet with the corresponding letter in the plaintext alphabet.

For example, to decrypt the message "Khoor, zruog!", you would use the following steps:

Determine the shift. For this example, let's assume we know that the shift is 3.
Replace each letter in the encrypted alphabet with the corresponding letter in the plaintext alphabet. For example, "K" becomes "H", "h" becomes "e", and so on.
The decrypted message is "Hello, world!".

The same function  below can be used to decrypt a message by using the opposit of the shift , for example 
ceaser_cipher("Khoor, zruog!", -3) --> "Hello , world!"
Security

