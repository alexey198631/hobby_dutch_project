# this code is not necessary for the app. I created it just to create sound files after some time.
from sound import *
from defs import *

words = pd.read_excel('data_files/dutch.xlsx', sheet_name='update')
words = words.loc[:, 'word':]
lesson_df = pd.read_excel('data_files/dutch.xlsx', sheet_name='lesson')
lesson_df = lesson_df.loc[:, 'lesson':]

wordList = loadWords(words, 'yes')

repeats = list(lesson_df.r)
set(repeats).remove(999)
repeats = [123]


def reps_sound(repeat, lesson_df, wordList):
    counter = 0
    s_repeat = []
    t_repeat = []
    words_from_lesson = lesson_df.list_of_words
    lesson_to_repeat = repeat
    lesson_words = words_from_lesson[lesson_to_repeat].split(";")
    print(lesson_words)
    for cw in lesson_words:
        cw = cw.strip()
        for w in wordList:
            if w.getWord() == cw and counter < 25:
                s_repeat.append(w.getWord())
                t_repeat.append(w.getTranslation())
                counter += 1
    return s_repeat, t_repeat


for les in repeats:
    print(les)
    rest = reps_sound(les, lesson_df, wordList)
    listening_lesson(les - 6, rest[0], rest[1])
