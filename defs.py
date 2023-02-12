# all app logic is here
import pandas as pd
import math
import re
from cls import *
from word_plot import *


def initial_load() -> object:  # load data from init file - xlsx with words
    """

    :rtype: object
    """
    words = pd.read_excel('data_files/init_words.xlsx', sheet_name='words')
    lesson_df = pd.DataFrame()
    exist = 'no'

    return words, lesson_df, exist


def next_load():  # load data from existing file
    words = pd.read_excel('data_files/dutch.xlsx', sheet_name='update')
    words = words.loc[:, 'word':]
    lesson_df = pd.read_excel('data_files/dutch.xlsx', sheet_name='lesson')
    lesson_df = lesson_df.loc[:, 'lesson':]
    verbs_df = pd.read_excel('data_files/dutch.xlsx', sheet_name='verbs')
    verbs_df = verbs_df.loc[:, 'translation':]
    try:
        exam_df = pd.read_excel('data_files/dutch.xlsx', sheet_name='exams')
        exam_df = exam_df.loc[:, 'n#':]

    except:
        exam_df = pd.DataFrame()
        exam_df['n#'] = 0
        exam_df['date'] = 0
        exam_df['size'] = 0
        exam_df['%'] = 0
        exam_df['words'] = 0
        exam_df['lang'] = 0

    exist = 'yes'

    return words, lesson_df, exist, exam_df, verbs_df


def loadWords(df_words, temp):  # data frame from xlsx file with words, it creates list of class Words
    list_of_words = []
    for i in range(len(df_words)):
        if temp == 'yes':
            list_of_words.append(
                Words(df_words.iloc[i, 0], df_words.iloc[i, 1], df_words.iloc[i, 2], df_words.iloc[i, 5],
                      df_words.iloc[i, 3],
                      df_words.iloc[i, 4], df_words.iloc[i, 6], df_words.iloc[i, 7], df_words.iloc[i, 8],
                      df_words.iloc[i, 9],
                      df_words.iloc[i, 10]))
        else:
            list_of_words.append(
                Words(df_words.iloc[i, 0], df_words.iloc[i, 1], df_words.iloc[i, 2], df_words.iloc[i, 5],
                      df_words.iloc[i, 3],
                      df_words.iloc[i, 4], 0, 0, 0, 0, 100))
    return list_of_words


def loadVerbs(df_words):  # data frame from xlsx file with verbs, it creates list of class Verbs
    list_of_words = []
    for i in range(len(df_words)):
        list_of_words.append(
            Verbs(df_words.iloc[i, 1], df_words.iloc[i, 2], df_words.iloc[i, 3], df_words.iloc[i, 0],
                  df_words.iloc[i, 4],
                  df_words.iloc[i, 5], df_words.iloc[i, 6], df_words.iloc[i, 7], df_words.iloc[i, 8], df_words.iloc[i, 9]))
    return list_of_words


def no_space(word):
    lst = []
    for w in word:
        lst.append(w.strip())
    return lst


def translation_with_comma(translation):
    try:
        translation = translation.split(',')
        translation = no_space(translation)
        return translation

    except:
        return [translation]


def help_for_guess(word, r):  # r - number of letters
    list_of_word = list(word)
    copy = list_of_word.copy()
    for j in range(len(list_of_word)):
        if list_of_word[j] == ' ':
            copy.remove(list_of_word[j])

    ls = random.sample(copy, k=r)

    for i in range(len(list_of_word)):
        if list_of_word[i] in ls:
            list_of_word[i] = list_of_word[i]
        else:
            list_of_word[i] = '_'
    back = ' '.join(list_of_word)

    return back


def right_word(word, translation, rever=0):
    point_counter = 0
    if rever == 1:
        while True:
            x = input(f'\nPress "1","2","3" to open 1, 2, 3 letters in the word\n\n {translation}: ')
            if x == word:
                return [True, point_counter]
            elif x == '1' or x == '2' or x == '3':
                print(help_for_guess(word, int(x)))
                point_counter += int(x)
            else:
                return [False, point_counter]

    elif rever == 0:
        translation = translation_with_comma(translation)
        while True:
            x = input(f'\nPress "1","2","3" to open 1, 2, 3 letters in the word\n\n {word}: ')
            if x in translation:
                return [True, point_counter]
            elif x == '1' or x == '2' or x == '3':
                print(help_for_guess(translation[0], int(x)))
                point_counter += int(x)
            else:
                return [False, point_counter]


def cycle(sample_of_words, rever):
    p = 250
    s = sample_of_words.copy()
    while len(s) > 0:
        random.shuffle(s)
        lst_to_delete = []
        for i in s:
            temp = right_word(i.getWord(), i.getTranslation(), rever)
            if temp[0]:
                print("\nRIGHT!")
                p = p - temp[1]
                i.addSuccess()
                if rever == 0:
                    i.addTrials_d()
                else:
                    i.addTrials_r()
                lst_to_delete.append(i)
            else:
                print("\nWRONG!")
                p = p - temp[1]
                p -= 1
                if rever == 0:
                    i.addTrials_d()
                else:
                    i.addTrials_r()
        if len(lst_to_delete) > 0:
            for w in lst_to_delete:
                s.remove(w)
            if len(s) != 0:
                plotting(s)
        else:
            if len(s) != 0:
                plotting(s)
    print(p,'\n')
    return p


def list_to_list(lst):
    st = ''
    for w in lst:
        st = st + w + '; '
    st.strip()
    st = st[0:(len(st) - 2)]
    return st


def lesson_length(list_of_words):
    lesson_length_ = 0
    for w in list_of_words:
        temp = w.getWord()
        temp = temp.replace(' ', '')
        lesson_length_ += len(temp)
    return lesson_length_


def next_lesson(lesson_df):
    s_l = set(lesson_df.r)
    s_l = list(s_l)
    for i in s_l:
        if i == 999:
            s_l.remove(i)
    return s_l, max(s_l) + 1


def random_sample(list_of_words, n):
    sample = random.choices(list_of_words, weights=[w.getWeight() for w in list_of_words], k=n)
    ln = n
    st = len(set([x.getWord() for x in sample]))
    count = 0
    while ln != st:
        #print('count = ', count, 'len = ', ln, 'set = ', st)
        sample = random.choices(list_of_words, weights=[w.getWeight() for w in list_of_words], k=n)
        st = len(set([x.getWord() for x in sample]))
        count += 1
    return sample


def reps(repeat, lesson_df, wordList):
    s_repeat = []
    check_existence = []
    words_from_lesson = lesson_df.list_of_words
    lesson_to_repeat = lesson_df[lesson_df['r'] == repeat].index[0]

    lesson_words = words_from_lesson[lesson_to_repeat].split(";")
    for cw in lesson_words:
        cw = cw.strip()
        for w in wordList:
            if w.getWord() == cw and w.getWord() not in check_existence:
                s_repeat.append(w)
                check_existence.append(w.getWord())
    return s_repeat


def all_learned(lesson_df, wordList):
    allwords = []
    s_repeat = []
    words_from_lesson = lesson_df.list_of_words

    for i in range(len(words_from_lesson)):
        allwords = allwords + words_from_lesson[i].split(";")
    for j in range(len(words_from_lesson)):
        allwords[j] = allwords[j].strip()

    for cw in allwords:
        cw = cw.strip()
        for w in wordList:
            if w.getWord() == cw:
                s_repeat.append(w)

    s_repeat = set(s_repeat)
    s_repeat = list(s_repeat)

    return s_repeat


def for_inter_time(df, lessonNumber):
    ln = lessonNumber.getNumber()
    kt = lessonNumber.getInterTime()
    lessn = df.copy()
    lessn = lessn.assign(inter_pts=lambda x: ((lessn['inter'] - lessn['start'])))
    lessn['points'] = lessn['inter_pts'].apply(lambda x: x.seconds)

    row = lessn.index.values[-1]

    lessn.loc[row, 'lesson'] = ln
    lessn.loc[row, 'start'] = 0
    lessn.loc[row, 'inter'] = 0
    lessn.loc[row, 'finish'] = 0
    lessn.loc[row, 'known'] = 0
    lessn.loc[row, 'points'] = kt
    lessn.loc[row, 'length'] = 0
    lessn.loc[row, 'time'] = 0
    lessn.loc[row, 'list_of_words'] = 0
    lessn.loc[row, 'r'] = ln

    return lessn


def place(df, rep, t=0, cond=0):
    lesson = df.copy()
    if rep == 0:
        mod_lesson = lesson[lesson.known != 25]

    else:
        mod_lesson = lesson[lesson.known == 25]

    if cond == 0:
        last = mod_lesson.loc[:, "r"][-1:].values[0]
        last_points = mod_lesson.loc[:, "points"][-1:].values[0]
        mod_lesson = mod_lesson.sort_values(by='points', ascending=False, ignore_index=True)
        place = mod_lesson[mod_lesson['points'] == last_points].index[0]

        print(f'1. Lesson {mod_lesson.loc[0, "r"]:.0f} - {mod_lesson.loc[0, "points"]:.0f} pts \
              \n2. Lesson {mod_lesson.loc[1, "r"]:.0f} - {mod_lesson.loc[1, "points"]:.0f} pts \
              \n3. Lesson {mod_lesson.loc[2, "r"]:.0f} - {mod_lesson.loc[2, "points"]:.0f} pts \
              \n------------------------ \
              \n{(place + 1):.0f}. Lesson {last:.0f} - {last_points:.0f} pts \
              ')
    elif cond != 0:
        last_points = mod_lesson.loc[:, "points"][-1:].values[0]
        mod_lesson = mod_lesson.sort_values(by='points', ascending=True, ignore_index=True)
        place = mod_lesson[mod_lesson['points'] == last_points].index[0]


        print(f'1. Lesson {mod_lesson.loc[0, "r"]:.0f} - {mod_lesson.loc[0, "points"]:.0f} sec \
                      \n2. Lesson {mod_lesson.loc[1, "r"]:.0f} - {mod_lesson.loc[1, "points"]:.0f} sec \
                      \n3. Lesson {mod_lesson.loc[2, "r"]:.0f} - {mod_lesson.loc[2, "points"]:.0f} sec \
                      \n------------------------ \
                      \n{t} sec, place {(place + 1):.0f}, difference {- int(mod_lesson.loc[0, "points"]) + int(t)} \
                      ')


def final_creation(exist, words, wordList, lessonNumber, lesson_df, sample, exam_df, verbs_df):

    if exist == 'yes':
        dutch = words.copy()

        for i in range(len(dutch)):
            dutch.loc[i, 'appear'] = wordList[i].getAppear()
            dutch.loc[i, 'trial_d'] = wordList[i].getTrials_d()
            dutch.loc[i, 'trial_r'] = wordList[i].getTrials_r()
            dutch.loc[i, 'success'] = wordList[i].getSuccess()
            dutch.loc[i, 'weight'] = wordList[i].getWeight()

        row = lesson_df.loc[:, 'lesson'][-1:].values[0]
        lesson_df.loc[row, 'lesson'] = lesson_df.loc[:, 'lesson'][-1:].values[0] + 1
        lesson_df.loc[row, 'start'] = lessonNumber.getStart()
        lesson_df.loc[row, 'inter'] = lessonNumber.getInter()
        lesson_df.loc[row, 'finish'] = lessonNumber.getFinish()
        lesson_df.loc[row, 'known'] = lessonNumber.getNumber_of_easy()
        lesson_df.loc[row, 'points'] = lessonNumber.getPoints()
        lesson_df.loc[row, 'length'] = lessonNumber.getLength_of_lesson()
        lesson_df.loc[row, 'time'] = lessonNumber.getTime()
        lesson_df.loc[row, 'list_of_words'] = list_to_list(lessonNumber.getList())
        lesson_df.loc[row, 'r'] = lessonNumber.getNumber()

    else:

        dutch = words.copy()

        dutch['appear'] = 0
        dutch['trial_d'] = 0
        dutch['trial_r'] = 0
        dutch['success'] = 0
        dutch['weight'] = 100

        for i in range(len(dutch)):
            dutch.loc[i, 'appear'] = wordList[i].getAppear()
            dutch.loc[i, 'trial_d'] = wordList[i].getTrials_d()
            dutch.loc[i, 'trial_r'] = wordList[i].getTrials_r()
            dutch.loc[i, 'success'] = wordList[i].getSuccess()
            dutch.loc[i, 'weight'] = wordList[i].getWeight()

        lesson_df['lesson'] = 0
        lesson_df['start'] = 0
        lesson_df['inter'] = 0
        lesson_df['finish'] = 0
        lesson_df['known'] = 0
        lesson_df['points'] = 0
        lesson_df['length'] = 0
        lesson_df['time'] = 0
        lesson_df['list_of_words'] = []

        lesson_df.loc[0, 'lesson'] = lessonNumber.getNumber()
        lesson_df.loc[0, 'start'] = lessonNumber.getStart()
        lesson_df.loc[0, 'inter'] = lessonNumber.getInter()
        lesson_df.loc[0, 'finish'] = lessonNumber.getFinish()
        lesson_df.loc[0, 'known'] = lessonNumber.getNumber_of_easy()
        lesson_df.loc[0, 'points'] = lessonNumber.getPoints()
        lesson_df.loc[0, 'length'] = lessonNumber.getLength_of_lesson()
        lesson_df.loc[0, 'time'] = lessonNumber.getTime()
        lesson_df.loc[0, 'list_of_words'] = list_to_list(lessonNumber.getList())
        lesson_df.loc[0, 'r'] = lessonNumber.getNumber()

    writer = pd.ExcelWriter('data_files/dutch.xlsx', engine='xlsxwriter')
    dutch.to_excel(writer, sheet_name='update')
    lesson_df.to_excel(writer, sheet_name='lesson')
    exam_df.to_excel(writer, sheet_name='exams')
    verbs_df.to_excel(writer, sheet_name='verbs')
    writer.save()

    temp = []
    for w in sample:
        try:
            math.isnan(w.getTyp())
            temp.append(w)
        except:
            if re.search(r'de', w.getTyp()) and not re.search(r'het', w.getTyp()):
                print('de', w)
            elif re.search(r'het', w.getTyp()) and not re.search(r'de', w.getTyp()):
                print('het', w)
            elif re.search(r'het', w.getTyp()) and re.search(r'de', w.getTyp()):
                print('de/het', w)
            else:
                print(w)
    for t in temp:
        print(t)

    print('\n', 'EXAMPLES', '\n')

    for w in sample:
        try:
            math.isnan(w.getExample_nl())
        except:
            print(w.getWord(), '->', w.getExample_nl(), '->', w.getExample_en(), '\n')

    print('Lesson #:', lessonNumber.getNumber(), 'time spent:', lessonNumber.getTime(), 'points: ',
          lessonNumber.getPoints(), '\n')


def initial_weight(sample):
    sample_weights = {}
    for w in sample:
        sample_weights[w.getWord()] = w.getWeight()
    print('\n')
    for w in sample:
        print(w.getWord(), '=', round(w.getWeight(), 1))
    print('\n')
    return sample_weights


def nine_nine_nine(sample, sample_weights):
    print('\n')
    count = 0
    for w in sample:
        if round(sample_weights[w.getWord()], 1) > round(w.getWeight(), 1):
            count += 1
        print(w.getWord(), '=', round(sample_weights[w.getWord()], 1), '->', round(w.getWeight(), 1))
    print(f'Progress for {count} words from {len(sample)}. Good job!')


def bottom_five(lesson_df):
    # this function determine the worst lessons 5 which were not repeated
    data_words_lesson_df = lesson_df.copy()
    # keeping necessary columns only and sorting them descending
    data_words_lesson_df = data_words_lesson_df.loc[:, ['points', 'r']]
    data_words_lesson_df = data_words_lesson_df.sort_values(by='points', ascending=False, ignore_index=True)
    mask = data_words_lesson_df.duplicated(subset='r', keep='first')
    # keeping only the worst lessons in rating, anti top 5
    df = data_words_lesson_df[~mask]
    df = df.reset_index(drop=True)
    sml = df.nsmallest(5, columns='points')
    # renaming for printing, to understand how many points each lesson has
    sml.rename(columns={"points": "lesson/points"}, inplace=True)
    # key of the dictionary should be number of the lesson
    sml.set_index("r", inplace=True)
    dct = sml.to_dict()
    return dct
