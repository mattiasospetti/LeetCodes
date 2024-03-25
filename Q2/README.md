Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

**Example 1:**

**Input:** `pattern = "abba", s = "dog cat cat dog"` 
**Output:** `true`

**Example 2:**

**Input:** `pattern = "abba", s = "dog cat cat fish"` 
**Output:** `false`

**Example 3:**

**Input:** `pattern = "aaaa", s = "dog cat cat dog"` 
**Output:** `false`

N.B: this time I won't care about constraints, as I assume inputs will respect them.

This is what you'll see as a "starting point":
```
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
```

[Difficulty: Easy]
