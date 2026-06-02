# String Programs

# 1. Username Validation System
user = "Rathna123"
if user.isalnum():
    print("Valid Username")
else:
    print("Invalid Username")

print("\n" + "-" * 20)

# 2. Password Strength Checker
password = "Python123"

has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
else:
    print("Weak Password")

print("\n" + "-" * 20)

# 3. Email Domain Extractor
email = "rathna@gmail.com"
print(email.split("@")[1])

print("\n" + "-" * 20)

# 4. Log File Analyzer
log = "ERROR INFO ERROR WARNING ERROR"
print(log.count("ERROR"))

print("\n" + "-" * 20)

# 5. Chat Message Cleaner
msg = "   Hello    World   "
print(" ".join(msg.split()))

print("\n" + "-" * 20)

# 6. Product Code Verification
code = "PRD5678"

if code.startswith("PRD"):
    print("Valid Product")
else:
    print("Invalid Product")

print("\n" + "-" * 20)

# 7. Reverse Customer Feedback
feedback = "Excellent"
print(feedback[::-1])

print("\n" + "-" * 20)

# 8. Word Frequency Counter
review = "good service good quality good support"

words = review.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word} : {count}")

print("\n" + "-" * 20)

# 9. Secret Message Encryption
text = "abc"

encrypted = ""
for ch in text:
    encrypted += chr(ord(ch) + 1)

print(encrypted)

print("\n" + "-" * 20)

# 10. Anagram Checker
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
