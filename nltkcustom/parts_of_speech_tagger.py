from nltk.tag import pos_tag


class PartsOfSpeechTagger:
    """
    This class is used to tag words in a list of tokenized words to their proper parts of speech.
    Kindly note not to import any other redundant packages / modules as it may violate SOLID principles.
    """
    def __init__(self):
        self.parts_of_speech_tagged_words_list = []

    # Process parts of speech tags for inputted list of (list of tokenized words) and store in a member variable

    def process_parts_of_speech_tags(self, tokenized_words_list):
        try:
            for words in tokenized_words_list:
                self.parts_of_speech_tagged_words_list.append(pos_tag(words))
        except Exception as exception:
            print("Exception occurred!!!", str(exception), sep='\n')

    # Return list of (list of parts of speech tagged tokenized words) which
    # was processed by @process_parts_of_speech_tags
    def get_parts_of_speech_tags(self):
        return self.parts_of_speech_tagged_words_list
