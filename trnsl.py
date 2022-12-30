from googletrans import Translator
from defs import *

translator = Translator()

words = pd.read_excel('/Users/aleksejgukov/Desktop/dutch.xlsx', sheet_name='update')
words = words.loc[:, 'word':]
lesson_df = pd.read_excel('/Users/aleksejgukov/Desktop/dutch.xlsx', sheet_name='lesson')
lesson_df = lesson_df.loc[:, 'lesson':]

wordList = loadWords(words, 'yes')

count = 0
final_1 = dict()
for word in wordList:

    try:
        x = translator.translate(word.getTranslation(), src='en', dest='ru')
        final_1[word.getTranslation()] = x.text

    except:
        print('challenge')

    count += 1

    if count % 100 == 0:
        df_1 = pd.DataFrame.from_dict(final_1, orient='index')
        writer = pd.ExcelWriter('/Users/aleksejgukov/Desktop/temp.xlsx', engine='xlsxwriter')
        df_1.to_excel(writer, sheet_name='1')
        writer.save()

    print(count, 'from', len(wordList))


df_1 = pd.DataFrame.from_dict(final_1, orient='index')
#
writer = pd.ExcelWriter('/Users/aleksejgukov/Desktop/final.xlsx', engine='xlsxwriter')
df_1.to_excel(writer, sheet_name='1')
writer.save()