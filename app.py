from datetime import datetime
from defs import *
from cls import *
from sound import *
from exam import *
from werkwoorden import *


exm = str(input('Is it time to have an exam or werkwoorden? - enter "yes" for exam and "verb" for irregula verbs! '))

if exm == 'yes':
    exam_mode()
elif exm == 'verb':
    verb_mode()


try:
    words = next_load()[0]
    lesson_df = next_load()[1]
    exist = next_load()[2]
    exam_df = next_load()[3]
    verbs_df = next_load()[4]

except:

    words = initial_load()[0]
    lesson_df = initial_load()[1]
    exist = initial_load()[2]


wordList = loadWords(words, exist)

try:
    ran = [i for i in range(1, (lesson_df.loc[:, 'lesson'][-1:].values[0]) + 1)]
    passed_lessons = next_lesson(lesson_df)[0]  # [1,2,3,4,....]
    repeat = 0

    anti_top_5 = bottom_five(lesson_df)
    repeat = int(input(
        f"Do you want to repeat one from passed lessons, if yes type 1 - {next_lesson(lesson_df)[1] - 1}, 999 - random choice from all learned words \n Anti TOP5 {anti_top_5}\n "))


except:
    pass

try:
    # lessonNumber = Lesson((lesson_df.loc[:, 'lesson'][-1:].values[0]) + 1)
    if repeat in ran:
        lessonNumber = Lesson(repeat)
        sample = reps(repeat, lesson_df, wordList)
        save = sample.copy()
    elif repeat == 999:
        lessonNumber = Lesson(999)
        sample = random_sample(all_learned(lesson_df, wordList), 25)
        save = sample.copy()
        sample_weights = initial_weight(save)
    else:
        lessonNumber = Lesson(next_lesson(lesson_df)[1])
        sample = random_sample(wordList, 25)
        save = sample.copy()

except:

    lessonNumber = Lesson(1)
    sample = random_sample(wordList, 25)
    save = sample.copy()

print('Lesson #:', lessonNumber.getNumber())

[x.addAppear() for x in sample]
lessonNumber.wlist([x.getWord() for x in save])
lessonNumber.length_of_lesson(lesson_length(sample))
lessonNumber.start(datetime.now())
plotting(sample)
known = int(input('How many words do I know? '))
lessonNumber.number_of_easy(known)
print('special characters: [à ë ï é è ç ’]')
lessonNumber.points(cycle(sample, rever=0))
lessonNumber.inter(datetime.now())
place(for_inter_time(lesson_df, lessonNumber, known), repeat, lessonNumber.getInterTime(), 1)
plotting(sample)
lessonNumber.add_pts(cycle(sample, rever=1))
lessonNumber.finish(datetime.now())
final_creation(exist, words, wordList, lessonNumber, lesson_df, save, exam_df, verbs_df)
place(lesson_df, repeat)
if repeat == 0:
    lesson_progress(lesson_df)
    words_progress(lesson_df)
    listening_lesson(lessonNumber.getNumber(), [x.getWord() for x in save], [x.getTranslation() for x in save])
elif repeat == 999:
    nine_nine_nine(sample, sample_weights)
    print('\n')
else:
    print('Goodbay!')
