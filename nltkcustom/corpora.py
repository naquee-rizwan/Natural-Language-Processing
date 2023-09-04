from nltk.corpus import state_union


class Corpora:
    """
    Initialize all the corpora required here itself.
    Kindly note not to import any other redundant packages / modules as it may violate SOLID principles.
    """
    def __init__(self):
        self.train_text = state_union.raw("2005-GWBush.txt")
        self.test_text = state_union.raw("2006-GWBush.txt")
