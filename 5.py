text = input("Enter a text: ")

char_freq = {}

for ch in text:
	if ch != " ":
		if ch in char_freq:
			char_freq[ch] += 1
		else:
			char_freq[ch] = 1
			
words = text.split()

word_freq = {}

for word in words:
	if word in word_freq:
		word_freq[word] += 1
	else:
		word_freq[word] = 1
		
print("\nCharacter Frequency: ")
for ch in char_freq:
	print(ch, ":", char_freq[ch])

print("\nWord Frequency: ")
for word in word_freq:
	print(word, ":", word_freq[word])
		
