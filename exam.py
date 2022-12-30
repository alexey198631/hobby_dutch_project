from datetime import datetime
from defs import *
from cls import *
from sound import *


def exam_right_word(word, translation, rever=0):
    point_counter = 0
    if rever == 1:
        while True:
            x = input(f'\n {translation}: ')
            if x == word:
                point_counter += 1
                return [True, point_counter]
            else:
                return [False, point_counter]

    elif rever == 0:
        translation = translation_with_comma(translation)
        while True:
            x = input(f'\n {word}: ')
            if x in translation:
                point_counter += 1
                return [True, point_counter]
            else:
                return [False, point_counter]


def exam_cycle(sample_of_words, rever):
    right_ans = 0
    s = sample_of_words.copy()
    while len(s) > 0:
        random.shuffle(s)
        lst_to_delete = []
        for i in s:
            temp = exam_right_word(i.getWord(), i.getTranslation(), rever)
            if temp[0]:
                print("\nRIGHT!")
                right_ans = right_ans + temp[1]
                lst_to_delete.append(i)
            else:
                print("\nWRONG!")
                print(f'\n{i}')
                right_ans = right_ans + temp[1]
                lst_to_delete.append(i)
        if len(lst_to_delete) > 0:
            for w in lst_to_delete:
                s.remove(w)

    #print(f'{right_ans} right from {len(sample_of_words)}')
    return right_ans / len(sample_of_words)


def exam_final_creation(words, lesson_df, exam_df, sample, marks, rev):
    try:
        row = exam_df.loc[:, 'n#'][-1:].values[0]
    except:
        row = 0


    exam_df.loc[row, 'n#'] = row + 1
    exam_df.loc[row, 'date'] = datetime.now()
    exam_df.loc[row, 'size'] = len(sample)
    exam_df.loc[row, 'pts'] = marks * 100
    exam_df.loc[row, 'lang'] = rev

    writer = pd.ExcelWriter('/Users/aleksejgukov/Desktop/dutch.xlsx', engine='xlsxwriter')
    words.to_excel(writer, sheet_name='update')
    lesson_df.to_excel(writer, sheet_name='lesson')
    exam_df.to_excel(writer, sheet_name='exams')
    writer.save()



def exam_mode():
    try:
        words = next_load()[0]
        lesson_df = next_load()[1]
        exist = next_load()[2]
        exam_df = next_load()[3]

    except ValueError:
        print("Oops!  You do not know anything yet! ")

    words_exam = words[words['weight'] <= 35.0]

    wordList = loadWords(words_exam, exist)

    sample_size = int(input('Please tell me quantity of words you want to test? (e.g. 10, 25, 50, 75, 100 ) '))
    rev = str(input('Do you want to test Dutch to English mode (type "nl") or English to Dutch (type "en")? '))
    if rev == 'nl':
        rever = 0
    elif rev == 'en':
        rever = 1
    else:
        rever = random.choice([0,1])
        if rever == 0:
            rev = 'nl'
        else:
            rev = 'en'
        print("I'll decide myself!")

    sample = random_sample(wordList, sample_size)
    marks = exam_cycle(sample, rever)
    exam_final_creation(words, lesson_df, exam_df, sample, marks, rev)
    print(f'{round(marks, 2)*100}%')
    quit()
