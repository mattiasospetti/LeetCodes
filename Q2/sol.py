# Here the most reasonable solutions would require the use of a double dictionary
# (I'm still figuring out if we can get rid of the second one, since it seems a specular vector of the first one)
# In case, open an issue/discussion and let me know!

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words): #first check, in case we'll submit sth. like 'abba' and 'cat dog dog cat cat', there's an obvious error
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):  # we'll check elem by elem
                                            # ex: 'abba' 'cat dog dog cat'
                                            # --> ('a','cat')
                                            # --> ('b','dog'), and so on...
        if char not in char_to_word and word not in word_to_char: #first case: a (pattern,word) we never met (yet)
            char_to_word[char] = word
            word_to_char[word] = char # Let's store this first couple inside the dictionary
        
        # second False case: if the current pattern 'char' is new (but not the 'word', otherwise we fell into the above 'if' statement)
        # or even if the word the previously stored for this 'char' is not what we got now. This means there's a misalignment
            
        elif char not in char_to_word or char_to_word[char] != word:
            return False
        
        # in the third False case we'll check the 'word': as previously done, we check if we haven't me it yet,
        # or if the current 'char' (pattern character) doesn't corrispond to the current 'word'

        elif word not in word_to_char or word_to_char[word] != char:
            return False
    
    # if we didn't feel in any of the previous cases, this means everything is ok --> True! 

    return True

# some examples here (as LeetCode suggests):
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))  # Expected output: True

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))  # Expected output: False

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))  # Expected output: False
