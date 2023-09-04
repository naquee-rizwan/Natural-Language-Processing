from nltk.corpus import stopwords


class StopWords:
    """
    Remove common words in a language from a list of inputted words [mostly tokenized
    list of words is taken as input]. This is primarily done because stop words have
    very less semantic meaning and is generally used for providing syntactical benefit
    / meaning to a sequence of functional words.
    """

    def __init__(self):
        self.tokenized_stop_words_removed_list = []
        self.stop_words = set(stopwords.words("english"))

    # Remove stop words and save in a list

    def remove_stop_words(self, tokenized_text_list):
        # Use either for loop or one-liner as written below

        # for word in tokenized_text_list:
        #     if word not in self.stop_words:
        #         self.tokenized_stop_words_removed_list.append(word)
        self.tokenized_stop_words_removed_list = [word for word in tokenized_text_list if not word in self.stop_words]

    # Get the updated list after stop words removal

    def get_stop_words_removed_list(self):
        return self.tokenized_stop_words_removed_list
