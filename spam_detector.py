import re

spam_words = [
    "click now", "earn money", "free money", "fucking",
    "bastard", "money", "click", "discount"
]

# Match longer phrases first to avoid partial matches (e.g. "free money" vs "money")
spam_words_sorted = sorted(spam_words, key=len, reverse=True)

# Build a regex that matches any spam phrase as a whole word/phrase, case-insensitive
pattern = r'\b(?:' + '|'.join(re.escape(w) for w in spam_words_sorted) + r')\b'
regex = re.compile(pattern, flags=re.IGNORECASE)

# Read entire file, do replacements, write back
with open("spam_file.txt", "r", encoding="utf-8") as f:
    text = f.read()

cleaned = regex.sub("####", text)

# It's safer to write to a new file then replace, but you can overwrite directly:
with open("spam_file.txt", "w", encoding="utf-8") as f:
    f.write(cleaned)
