"""
Word Occurrence
Estimate: 20 minutes
Actual: 42
"""
word_to_count = {}

text = "this is a collection of words of nice words this is a fun thing it is" #input("text: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
    # number_of_words = word_to_count.get(word, 0)
    # word_to_count[word] = number_of_words + 1
    # print(f"{word} : {number_of_words}")



