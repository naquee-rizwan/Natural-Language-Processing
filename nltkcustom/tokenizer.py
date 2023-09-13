from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltkcustom.corpora import Corpora


class Tokenizer:
    """
    Tokenizer - Word tokenizer and sentence tokenizer
    1. Word tokenizer - Separates by words
    2. Sentence tokenizer - Separates by sentences

    Lexicon and Corpora
    1. Corpora - Body of text. Eg - Medical journals, Plays of Shakespeare
    2. Lexicon - Words and their meanings

    Example :
    Investor speaks vs Regular speaks
    Investor spoken 'bull' = "Someone who is positive about the market."
    Regular spoken 'bull' = "A black animal. Wife of a cow."
    """

    def __init__(self):
        self.corpora = Corpora()
        self.tokenized_words = []
        self.tokenized_sentences = []

    # Word tokenizer getter @get_tokenized_word
    def get_tokenized_words(self):
        return self.tokenized_words

    # Sentence tokenizer getter @get_tokenized_sentence
    def get_tokenized_sentences(self):
        return self.tokenized_sentences

    # Punkt sentence tokenizer  implementation @apply_punkt_sentence_tokenizer and @get_punkt_tokenized_sentences
    def process_using_punkt_tokenizer(self):
        sentence_tokenizer = PunktSentenceTokenizer(self.corpora.train_text)
        self.tokenized_sentences = sentence_tokenizer.tokenize(self.corpora.test_text)
        for index, sentence in enumerate(self.tokenized_sentences):
            self.tokenized_words.append(word_tokenize(sentence))
