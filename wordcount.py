# put your code here.

def count_words(file_name):
    """Counts how many times each space-separated word appears in text file """

    word_count = {}
    data_file = open(file_name)

    word_frequency = 0

    for line in data_file:
        line.rstrip()
        word_list = line.split(' ')
        for word in word_list:
            if word not in word_count:
                # python is viewing this as list indexing vs dictionary setting
                word_count[word] = word_frequency
                word_frequency += 1
            else:
                word_frequency += 1

    print word_count
    return

count_words("test.txt")

# our function would find the value of word and frequency,
# then create a dictionary by taking those arguments
# def dictionary(key, value):
#   dictionary = {key: value}

