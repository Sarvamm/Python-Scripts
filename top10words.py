paragraph = input("Enter a paragraph: ")
words = paragraph.split()
word_count = {}

for word in words:
    word = word.lower().strip(".,!?;:")
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_words[:10]

for word, count in top_10:
    print(word, count)
