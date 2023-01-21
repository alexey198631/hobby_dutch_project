from datetime import datetime
from defs import *
from cls import *
from sound import *


def exam_random_sample(list_of_words, n):
    sample = random.choices(list_of_words, weights=None, k=n)
    ln = n
    st = len(set([x.getWord() for x in sample]))
    count = 0
    while ln != st:
        #print('count = ', count, 'len = ', ln, 'set = ', st)
        sample = random.choices(list_of_words, weights=None, k=n)
        st = len(set([x.getWord() for x in sample]))
        count += 1
    return sample


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
    for i in s:
        temp = exam_right_word(i.getWord(), i.getTranslation(), rever)
        if temp[0]:
            print("\nRIGHT!")
            right_ans = right_ans + temp[1]
            print(f'\n{right_ans} from {len(sample_of_words)}')
        else:
            print("\nWRONG!")
            print(f'\n{i}')
            right_ans = right_ans + temp[1]
            print(f'\nStill {right_ans} from {len(sample_of_words)}')

    return right_ans / len(sample_of_words)


def exam_final_creation(words, lesson_df, exam_df, sample, marks, rev, l_w_e):
    try:
        row = exam_df.loc[:, 'n#'][-1:].values[0]
    except:
        row = 0

    exam_df.loc[row, 'n#'] = row + 1
    exam_df.loc[row, 'date'] = datetime.now()
    exam_df.loc[row, 'size'] = len(sample)
    exam_df.loc[row, '%'] = marks * 100
    exam_df.loc[row, 'words'] = l_w_e
    exam_df.loc[row, 'lang'] = rev

    writer = pd.ExcelWriter('data_files/dutch.xlsx', engine='xlsxwriter')
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

    words_exam = words[words['weight'] <= 50.0]
    l_w_e = len(words_exam)

    wordList = loadWords(words_exam, exist)

    sample_size = int(input('Please tell me quantity of words you want to test? (e.g. 10, 25, 50, 75, 100 ) '))
    rev = str(input('Do you want to test Dutch to English mode (type "nl") or English to Dutch (type "en")? '))
    if rev == 'nl':
        rever = 0
    elif rev == 'en':
        rever = 1
    else:
        rever = random.choice([0, 1])
        if rever == 0:
            rev = 'nl'
        else:
            rev = 'en'
        print("I'll decide myself!")

    sample = exam_random_sample(wordList, sample_size)
    marks = exam_cycle(sample, rever)
    exam_final_creation(words, lesson_df, exam_df, sample, marks, rev, l_w_e)
    print(f'{round(marks, 2)*100}%')
    quit()
