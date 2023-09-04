from nltk.stem import PorterStemmer


class Stemmer:
    def __init__(self):
        self.stemmed_words_list = []
        self.stemmer = PorterStemmer()

    def stem_tokenized_words(self, tokenized_words_list):
        for word in tokenized_words_list:
            self.stemmed_words_list.append(self.stemmer.stem(word))

    def get_stemmed_tokenized_list(self):
        return self.stemmed_words_list
