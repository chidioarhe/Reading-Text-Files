# Read text from a file,
# count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename="story.txt"):
    # [assignment] Add your code here
    file = open(filename)
    data = file.read()
    print(count_words(data))


def count_words(str):

    # [assignment] Add your code here
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


file = open("story.txt", "r")
data = file.read()
print(count_words(data))
