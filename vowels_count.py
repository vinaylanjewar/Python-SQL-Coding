## counting vowels in sentence

vowel = ['a','e','i','o','u','A','E','I','O','U']
word = 'I am learning Python'
count = 0
for i in word:
    if i in vowel:
        count = count + 1
print(count)
