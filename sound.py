from gtts import gTTS


def listening_lesson(lesson_number, word, translation):
    number = ['één', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf',
              'dertien', 'veertien', 'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien', 'twintig',
              'eenentwintig', 'tweeëntwintig', 'drieëntwintig', 'vierentwintig', 'vijfentwintig']
    list_of_words = word
    list_of_translations = translation
    combo = []

    for i in range(len(list_of_words)):
        combo.append(number[i])
        combo.append(list_of_words[i])

    speak_word = []
    speak_translation = []
    nums = []

    text_nl = " . ".join(combo)
    first_speak = gTTS(text=text_nl, lang='nl', slow=True)

    for num in number:
        nums.append(gTTS(text=num, lang='nl', slow=True))

    for word in list_of_words:
        speak_word.append(gTTS(text=word, lang='nl', slow=True))

    for translation in list_of_translations:
        speak_translation.append(gTTS(text=translation, lang='en', slow=True))

    with open(f'data_files/Lessons/Lesson_{lesson_number}_auto.mp3', 'wb') as f:
        first_speak.write_to_fp(f)
        for j in range(len(speak_word)):
            nums[j].write_to_fp(f)
            speak_word[j].write_to_fp(f)
            speak_translation[j].write_to_fp(f)

    print('You can find the sound of the last lesson in Lessons/')