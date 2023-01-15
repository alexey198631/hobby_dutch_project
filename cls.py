# two main classes for the app
class Words(object):

    """The class for all words from dictionary. Each word a type, a translation, an example,
    a translation of an example, a translation to Russian, also additional parameters which would be created after
    the first run (quantity of appearances in lessons, trials of direct and indirect translation,
    success attempts, also weight, more weight - more often words appear"""

    def __init__(self, word, typ, translation, russian, example, example_translation, appear, trial_d, trial_r, success,
                 weight):
        self.word = word
        self.typ = typ
        self.translation = translation
        self.example = example
        self.example_translation = example_translation
        self.russian = russian
        self.appear = appear
        self.trial_d = trial_d
        self.trial_r = trial_r
        self.success = success
        self.weight = weight

    def getWord(self):
        return self.word

    def getTyp(self):
        return self.typ

    def getTranslation(self):
        return self.translation

    def getRussian(self):
        return self.russian

    def changeType(self, new):
        self.typ = new

    def getTrials_d(self):
        return self.trial_d

    def getTrials_r(self):
        return self.trial_r

    def addTrials_d(self):
        self.trial_d += 1

    def addTrials_r(self):
        self.trial_r += 1

    def getAppear(self):
        return self.appear

    def addAppear(self):
        self.appear += 1
        return self.appear

    def addSuccess(self):
        self.success += 1
        return self.success

    def getSuccess(self):
        return self.success

    def getExample_nl(self):
        return self.example

    def getExample_en(self):
        return self.example_translation

    def getWeight(self):
        if self.trial_d == 0 and self.trial_r == 0:
            return self.weight
        else:
            return 100 - (self.success / (self.trial_d + self.trial_r)) * 100

    def __len__(self):
        return len(f'{self.word} -> {self.translation}')

    def __repr__(self):
        return f'{self.word}: {self.appear}, {self.trial_d + self.trial_r} / {self.success}'

    def __str__(self):
        return f'{self.word} : {self.translation}'


class Lesson(object):
    """The class is creating after any start of the program and fix all its parameters:
    lesson length in time and symbols, lesson points and, of course, lesson number
    """
    lol: object
    list_of_words: object
    pts: object
    easy: object
    finish: object
    inter: object
    start: object

    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def start(self, start):
        self.start = start

    def getStart(self):
        return self.start

    def inter(self, inter):
        self.inter = inter

    def getInter(self):
        return self.inter

    def finish(self, finish):
        self.finish = finish

    def getFinish(self):
        return self.finish

    def number_of_easy(self, easy):
        self.easy = easy

    def getNumber_of_easy(self):
        return self.easy

    def points(self, pts):
        self.pts = pts

    def add_pts(self, a_pts):
        self.pts += a_pts

    def getTime(self):
        return int((self.finish - self.start).seconds)

    def getPoints(self):
        return self.pts + 1500 - int((self.finish - self.start).seconds)

    def getInterTime(self):
        return int((self.inter - self.start).seconds)

    def wlist(self, list_of_words):
        self.list_of_words = list_of_words

    def getList(self):
        return self.list_of_words

    def length_of_lesson(self, lol):
        self.lol = lol

    def getLength_of_lesson(self):
        return self.lol