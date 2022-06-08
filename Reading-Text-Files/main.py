# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    keys = []
    with open(filename) as f:
        for line in f:
            keys.append(line.strip())

    sentence = ' '.join([str(item) for item in keys])
    return sentence


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    
    punct = ['.', ',', '?']
    #get words in a list
    my_list = text.split()
    clean_text = []

    #remove punctuation marks
    for word in my_list:
        if word[-1] in punct:
            clean_text.append(word[0:len(word)-1])
        else:
            clean_text.append(word)

    #get unique words
    unique_words = set(clean_text)

    #dictionary to hold the counts of each word
    word_dict = {}

    for word in unique_words:
        word_dict[word] = my_list.count(word)

    return(word_dict)


text_set = count_words()
print(text_set)