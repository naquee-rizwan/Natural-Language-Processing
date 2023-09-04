from nltkcustom import tokenizer, stop_words, stemmer, parts_of_speech_tagger


class Implementations:

    def __init__(self):
        # Initialization order is as per generic pipeline of natural language processing.
        self.tokenizer = tokenizer.Tokenizer()
        self.stop_words = stop_words.StopWords()
        self.stemmer = stemmer.Stemmer()
        self.part_of_speech_tagger = parts_of_speech_tagger.PartsOfSpeechTagger()


if __name__ == "__main__":
    '''----------------------------------------------------------------------------------------------------'''

    ##################################################
    #            DEVELOPMENT STARTS HERE             #
    ##################################################

    # Create instance of Implementation to initiate different natural language processing techniques
    implementations = Implementations()

    implementations.tokenizer.process_using_punkt_tokenizer()

    # Print tokenized sentences of the corpora
    # print("Tokenized sentences :", implementations.tokenizer.get_tokenized_sentences(), sep='\n', end='\n\n')

    # Print tokenized words of the corpora
    # print("Tokenized words :", implementations.tokenizer.get_tokenized_words(), sep='\n', end='\n\n')

    # Initialize and print a list with stop words removed using Stopwords.py
    # Not carrying out stop words removal as of now.
    # Uncomment the next couple of lines to get list with stop words removed.
    # implementations.stop_words.remove_stop_words(implementations.tokenizer.get_tokenized_word())
    # print(implementations.stop_words.get_stop_words_removed_list())

    # Initialize and print a list of stemmed words for the tokenized input sequence
    # Not carrying out stemming as of now.
    # Uncomment the next couple of lines to get list of tokenized and stemmed words.
    # implementations.stemmer.stem_tokenized_words(implementations.tokenizer.get_tokenized_words())
    # print(implementations.stemmer.get_stemmed_tokenized_list())

    implementations.part_of_speech_tagger.process_parts_of_speech_tags(
        implementations.tokenizer.get_tokenized_words()
    )

    # print(implementations.part_of_speech_tagger.get_parts_of_speech_tags())

    ##################################################
    #             DEVELOPMENT ENDS HERE              #
    ##################################################

    '''----------------------------------------------------------------------------------------------------'''

    ##################################################
    #            TESTING CODE STARTS HERE            #
    ##################################################

    # Assert length equality of tokenized sentences, tokenized words list and words' parts of speech tagged list

    number_of_sentences = len(implementations.tokenizer.get_tokenized_sentences())
    assert (len(implementations.tokenizer.get_tokenized_sentences()) == number_of_sentences)
    assert (len(implementations.tokenizer.get_tokenized_words()) == number_of_sentences)
    assert (len(implementations.part_of_speech_tagger.get_parts_of_speech_tags()) == number_of_sentences)

    # Assert that the words in tokenized words exactly match with first tuple in part of speech tagged words' list

    for sentence_number in range(number_of_sentences):
        for word_index in range(len(implementations.part_of_speech_tagger.get_parts_of_speech_tags()[sentence_number])):
            assert (
                implementations.tokenizer.get_tokenized_words()[sentence_number][word_index] ==
                implementations.part_of_speech_tagger.get_parts_of_speech_tags()[sentence_number][word_index][0]
            )

    ##################################################
    #             TESTING CODE ENDS HERE             #
    ##################################################

    '''----------------------------------------------------------------------------------------------------'''
