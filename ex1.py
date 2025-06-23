import string
from collections import Counter

def load_cipher(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def freq_analysis(text):
    letter_counts = Counter(char.upper() for char in text if char.isalpha())
    total_letters = sum(letter_counts.values())
    print("\n=== Letter Frequency Analysis ===")
    print("Letter: Count (Percentage)")
    print("---------------------------")
    for letter, count in letter_counts.most_common():
        percentage = (count / total_letters) * 100
        print(f"{letter}: {count} ({percentage:.2f}%)")
    return letter_counts.most_common()

def apply_mapping(text, mapping):
    result = []
    for ch in text:
        upper = ch.upper()
        if upper in mapping:
            # preserve case: if original is lowercase, convert mapped to lowercase
            decrypted_char = mapping[upper]
            result.append(decrypted_char.lower() if ch.islower() else decrypted_char)
        else:
            result.append(ch)
    return ''.join(result)

# 1. Define your custom substitution mapping here:
#    map each ciphertext letter (uppercase) to the guessed plaintext (uppercase).

my_mapping = {
    'A': 'K',
    'B': 'L',
    'C': 'M',
    'D': 'N',
    'E': 'O',
    'F': 'P',
    'G': 'Q',
    'H': 'R',
    'I': 'S',
    'J': 'T',
    'K': 'U',
    'L': 'V',
    'M': 'W',
    'N': 'X',
    'O': 'Y',
    'P': 'Z',
    'Q': 'A',
    'R': 'B',
    'S': 'C',
    'T': 'D',
    'U': 'E',
    'V': 'F',
    'W': 'G',
    'X': 'H',
    'Y': 'I',
    'Z': 'J',
}

    
    # … add more letter→letter pairs as you guess them …


def main():
    cipher = load_cipher("story_cipher.txt")
    freq_analysis(cipher)

    # 2. Apply your custom substitution mapping directly:
    plaintext = apply_mapping(cipher, my_mapping)
    
    # Write the decrypted text to a file
    with open('solution.txt', 'w', encoding='utf-8') as f:
        f.write(plaintext)
    print("Decrypted text has been saved to 'solution.txt'.")

    # 3. As you identify more letter mappings, update `my_mapping`
    #    and re‐run this script until the text is fully readable.

if __name__ == "__main__":
    main()
