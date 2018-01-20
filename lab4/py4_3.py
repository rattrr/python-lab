import sys

def file_to_words_list(filename):
    with open(filename) as f:
        return f.read().split()


def make_occurrences_dict(wordslist):
    occurrences = dict()
    for word in wordslist:
        if word.lower() in occurrences:
            occurrences[word.lower()] += 1
        else:
            occurrences[word.lower()] = 1
    return occurrences


for word, occurrences in make_occurrences_dict(file_to_words_list(sys.argv[1])).items():
    print "{}: {}".format(word, occurrences)
