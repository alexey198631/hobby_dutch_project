"""
Program addition to learn different form of irregular verbs in Dutch

"""
from datetime import datetime
from defs import *
from word_plot import plotting_verbs


def verb_random_sample(list_of_words):
    sample = random.choices(list_of_words, weights=[w.getWeight() for w in list_of_words], k=5)
    ln = 5
    st = len(set([x.getWord() for x in sample]))
    count = 0
    while ln != st:
        sample = random.choices(list_of_words, weights=[w.getWeight() for w in list_of_words], k=5)
        st = len(set([x.getWord() for x in sample]))
        count += 1
    return sample


def right_verb(word, translation, second, third, rever=0):
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
    elif rever == 2:
        while True:
            x = input(f'\nPress "1","2","3" to open 1, 2, 3 letters in the word\n\n {word}: ')
            if x == second:
                return [True, point_counter]
            elif x == '1' or x == '2' or x == '3':
                print(help_for_guess(second, int(x)))
                point_counter += int(x)
            else:
                return [False, point_counter]
    elif rever == 3:
        while True:
            x = input(f'\nPress "1","2","3" to open 1, 2, 3 letters in the word\n\n {word}: ')
            if x == third:
                return [True, point_counter]
            elif x == '1' or x == '2' or x == '3':
                print(help_for_guess(third, int(x)))
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

def verb_cycle(sample_of_words, rever):
    s = sample_of_words.copy()
    while len(s) > 0:
        random.shuffle(s)
        lst_to_delete = []
        for i in s:
            temp = right_verb(i.getWord(), i.getTranslation(), i.getSecond(), i.getThird(), rever)
            if temp[0]:
                print("\nRIGHT!")
                i.addSuccess()
                if rever == 0:
                    i.addTrials_d()
                else:
                    i.addTrials_r()
                lst_to_delete.append(i)
            else:
                print("\nWRONG!")
                if rever == 0:
                    i.addTrials_d()
                else:
                    i.addTrials_r()
        if len(lst_to_delete) > 0:
            for w in lst_to_delete:
                s.remove(w)
            if len(s) != 0:
                plotting_verbs(s)
        else:
            if len(s) != 0:
                plotting_verbs(s)


def verb_final_creation(verbsList, words, lesson_df, exam_df, verbs_df):

    for i in range(len(verbs_df)):
        verbs_df.loc[i, 'appear'] = verbsList[i].getAppear()
        verbs_df.loc[i, 'trial_d'] = verbsList[i].getTrials_d()
        verbs_df.loc[i, 'trial_r'] = verbsList[i].getTrials_r()
        verbs_df.loc[i, 'success'] = verbsList[i].getSuccess()
        verbs_df.loc[i, 'weight'] = verbsList[i].getWeight()
        verbs_df.loc[i, 'time_spent'] = verbsList[i].getTimeSpend()

    writer = pd.ExcelWriter('data_files/dutch.xlsx', engine='xlsxwriter')
    words.to_excel(writer, sheet_name='update')
    lesson_df.to_excel(writer, sheet_name='lesson')
    exam_df.to_excel(writer, sheet_name='exams')
    verbs_df.to_excel(writer, sheet_name='verbs')
    writer.save()


def verb_mode():
    try:
        words = next_load()[0]
        lesson_df = next_load()[1]
        exam_df = next_load()[3]
        verbs_df = next_load()[4]

    except ValueError:
        print("Oops!  Something wrong with your source file! ")

    verbsList = loadVerbs(verbs_df)
    sample = verb_random_sample(verbsList)
    [x.addAppear() for x in sample]
    time_start = datetime.now()
    plotting_verbs(sample)
    verb_cycle(sample, 0)
    plotting_verbs(sample)
    verb_cycle(sample, 1)
    plotting_verbs(sample)
    verb_cycle(sample, 2)
    plotting_verbs(sample)
    verb_cycle(sample, 3)
    time_finish = datetime.now()
    time_spent = round(int((time_finish - time_start).seconds) / 5 , 0)
    [x.addTimeSpend(time_spent) for x in sample]
    print('start:', time_start, 'finish', time_finish, int(time_spent * 5))
    verb_final_creation(verbsList, words, lesson_df, exam_df, verbs_df)
    quit()