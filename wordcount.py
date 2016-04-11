# put your code here.

def count_words(file_name):
    """Counts how many times each space-separated word appears in text file """

    word_counts = {}
    data_file = open(file_name)

    for line in data_file:
        line.rstrip()
        word_list = line.split(' ')
        for word in word_list:
            # get method returns a default value associated with key 
            # by setting it to 0 
            # add one each time word appears through loop
            word_counts[word] = word_counts.get(word, 0) + 1

    print word_counts
    return

count_words("test.txt")


