with open("Q1.txt", "r") as file1:
    content = file1.read()

word_frequency = {}
splitted_words = content.split()

for word in splitted_words:
    word = word.strip("!.,").lower()

    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():
    print("'{}': {}".format(word,count))

for word, count in word_frequency.items():
    if count > most_frequent_count:
        most_frequent_word = word
        most_frequent_count = count

print("The most frequent word is '{}' which has a frequency of {}.".format(most_frequent_word, most_frequent_count))