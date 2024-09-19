class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
         # Dictionary to map characters from the pattern to words in the string
        char_to_word: dict[str, str] = {}
        # Dictionary to map words in the string back to characters in the pattern
        word_to_char: dict[str, str] = {}
        # Split the string 's' into words
        words: list[str] = s.split()
        
        # If the number of words does not match the length of the pattern, return false
        if len(words) != len(pattern):
            return False

        # Iterate through each character in the pattern and corresponding word in the string
        for i in range(len(pattern)):
            current_char: str = pattern[i]
            word: str = words[i]

            # If the current character and word are seen for the first time, add them to the dictionaries
            if current_char not in char_to_word and word not in word_to_char:
                char_to_word[current_char] = word
                word_to_char[word] = current_char
            else:
                # If the current character or word is already in the dictionaries, check for consistency
                if char_to_word.get(current_char) != word or word_to_char.get(word) != current_char:
                    return False  # Inconsistent mapping
        
        # If all checks are passed, return true
        return True

        