# Lab 2 Part II OTP

import os
import base64


def XOR(a, b):
    """Encryption using XOR, do not modify"""
    r = b""
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, "big")
    return r


def gen_OTP(length):
    """Generate a random OTP - you are not supposed to know the key - do not modify"""
    return bytearray(os.urandom(length))


def decrypt(cipher, OTP):
    """Decryption also using XOR, do not modify"""
    return XOR(cipher, OTP)


# Original message
original_plaintext = b"Student ID 1000000 gets 0 points\n"

# Randomly generated OTP
OTP = gen_OTP(length=len(original_plaintext))

# Encrypt
original_cipher = XOR(original_plaintext, OTP)

# Decrypt
# This will print the original message
print("Original message:")
print(decrypt(original_cipher, OTP))
print("--------------------------------")


def hax():
    # Desired forged plaintext (same length)
    target = b"Student ID 1000000 gets 4 points\n"
    # Compute new_cipher = orig_cipher ⊕ orig_plaintext ⊕ target_plaintext
    new_cipher = XOR(original_cipher, XOR(original_plaintext, target))
    return new_cipher





new_cipher = hax()


# When we finally decrypt the message, it should show the manipulated message

print("Forged message:")
print(decrypt(new_cipher, OTP))
print("--------------------------------")
