Title: Breaking Without Brute Force  
Name: Sarvesh Joaquim Gopu  


This lab explores how encryption systems can be broken or manipulated without brute force. It is divided into two tasks: breaking a substitution cipher using frequency analysis, and manipulating an OTP-encrypted message to forge a different plaintext without decrypting it.

Task 1: Substitution Cipher Decryption

The encrypted file 'story_cipher.txt' was encoded using a monoalphabetic substitution cipher. To break it, I performed frequency analysis and used trial-and-error by mapping the most frequent characters. Upon noticing that 'U' likely mapped to 'E', I built the rest of the mapping assuming a consistent shift pattern. My final substitution map looked like this:

my_mapping = {
  'A': 'K', 'B': 'L', 'C': 'M', 'D': 'N', 'E': 'O', 'F': 'P', 'G': 'Q', 'H': 'R',
  'I': 'S', 'J': 'T', 'K': 'U', 'L': 'V', 'M': 'W', 'N': 'X', 'O': 'Y', 'P': 'Z',
  'Q': 'A', 'R': 'B', 'S': 'C', 'T': 'D', 'U': 'E', 'V': 'F', 'W': 'G', 'X': 'H',
  'Y': 'I', 'Z': 'J'
}

I ran my script ex1.py which performed letter frequency analysis, followed by applying this mapping to decrypt the cipher.

Sample output from letter frequency:
U: 305 (11.49%)
J: 263 (9.91%)
Y: 229 (8.63%)
Q: 213 (8.02%)
...

After applying the mapping, the decrypted output was saved to solution.txt. It revealed a long review about an anime series called SYMPHOGEAR.

Decrypted text (sample from solution.txt):
WHAT IS SYMPHOGEAR. FOR A LOOOOONG, LOOONG TIME I HAVE NEVER BOTHERED ENGAGING MYSELF IN THIS FRANCHISE. I DID NOT UNDERSTAND WHAT IT IS. NOW THAT THE SHOW IS HAVING ITS LAST SEASON, I DECIDED TO FINALLY GIVE IN, GIVE SYMPHOGEAR A TRY FROM THE VERY START. I WONDERED HOW HAVE I MISSED OUT ON THE ANIME OF THE DECADE ALL THESE YEARS...
[Output continues and was successfully decrypted.]

Task 2: Forging a Message in OTP Encryption

In this task, an OTP (one-time pad) encrypted message was provided. The goal was to alter the decrypted output without knowing the key. Since OTP uses XOR and is reversible, I used this property:

new_ciphertext = original_ciphertext XOR (original_plaintext XOR target_plaintext)

This allowed me to forge the final decrypted message. My script ex2.py reads the original message and target message, computes the difference, and applies it to the ciphertext.

Command used:
python3 ex2.py

Output:
Original message:
b'Student ID 1000000 gets 0 points\n'
--------------------------------
Forged message:
b'Student ID 1000000 gets 4 points\n'
--------------------------------

The new ciphertext successfully decrypted to the forged message, proving that message integrity can be compromised even if the message cannot be decrypted.

Conclusion

This lab demonstrated the vulnerabilities of both classical and theoretical "perfect" encryption schemes. Substitution ciphers, though more secure than Caesar, can still be broken through linguistic patterns and frequency analysis. OTP, while theoretically unbreakable in confidentiality, is not secure in terms of integrity, allowing attackers to modify encrypted content without the key. Both exercises highlighted how encryption alone is not sufficient without authentication mechanisms.

Files submitted:
- ex1.py – Script for substitution cipher decryption
- story_cipher.txt – Ciphertext input
- solution.txt – Decrypted plain text output
- ex2.py – OTP manipulation script
- Jupyter Notebook (lab2_sarvesh_1008107.ipynb or .pdf) – Report with outputs


