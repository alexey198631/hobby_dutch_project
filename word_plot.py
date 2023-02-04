# it is going to be replaced by GUI app some day
import matplotlib.pyplot as plt
import random
import numpy as np
from datetime import datetime

def plotting(sample_of_words):  # sample_of_words - object of Class Words

    plt.figure(figsize=(16, 10), dpi=80)
    plt.get_current_fig_manager().set_window_title('Dutch Deluxe')

    vertical = []
    horizontal0 = []
    horizontal1 = []
    horizontal2 = []
    horizontal3 = []
    horizontal4 = []
    horizontal5 = []

    for i in range(0, 26):
        vertical.append(i)
        horizontal0.append(0)
        horizontal1.append(1)
        horizontal2.append(2)
        horizontal3.append(3)
        horizontal4.append(4)
        horizontal5.append(5)

    horizontal = []
    vertical0 = []
    vertical1 = []
    vertical2 = []
    vertical3 = []
    vertical4 = []
    vertical5 = []

    for y in range(0, 6):
        horizontal.append(y)
        vertical0.append(0)
        vertical1.append(5)
        vertical2.append(10)
        vertical3.append(15)
        vertical4.append(20)
        vertical5.append(25)

    plt.plot(vertical, horizontal0, color='grey', alpha=.1)
    plt.plot(vertical, horizontal1, color='grey', alpha=.1)
    plt.plot(vertical, horizontal2, color='grey', alpha=.1)
    plt.plot(vertical, horizontal3, color='grey', alpha=.1)
    plt.plot(vertical, horizontal4, color='grey', alpha=.1)
    plt.plot(vertical, horizontal5, color='grey', alpha=.1)
    plt.plot(vertical0, horizontal, color='grey', alpha=.1)
    plt.plot(vertical1, horizontal, color='grey', alpha=.1)
    plt.plot(vertical2, horizontal, color='grey', alpha=.1)
    plt.plot(vertical3, horizontal, color='grey', alpha=.1)
    plt.plot(vertical4, horizontal, color='grey', alpha=.1)
    plt.plot(vertical5, horizontal, color='grey', alpha=.1)

    plt.ylim(0, 5)
    plt.xlim(0, 25)

    y = [0.6, 1.6, 2.6, 3.6, 4.6]
    x = [1, 6, 11, 16, 21]

    lst = []
    for i in x:
        for j in y:
            lst.append((i, j))

    random.shuffle(sample_of_words)  # it is necessary to change word order at the plot
    random.shuffle(lst)

    for i, (t, k) in enumerate(lst):
        try:
            x = len(sample_of_words[i].getWord())

            plt.text(t + 4 / x, k, sample_of_words[i].getWord(), fontsize=12, color='black')
            plt.text(t + 4 / x, k - 0.2, sample_of_words[i].getTranslation(), fontsize=12, color='blue')
            plt.text(t + 4 / x, k - 0.4, sample_of_words[i].getRussian(), fontsize=10, color='grey')
            if sample_of_words[i].getTyp() is None:
                sample_of_words[i].changeType('-')
                plt.text(t - 0.5, k + 0.2, sample_of_words[i].getTyp(), fontsize=12, color='red')

            else:
                plt.text(t - 0.5, k + 0.2, sample_of_words[i].getTyp(), fontsize=12, color='red')

        except:
            x = 1
            plt.text(t + 5 / x, k, '', fontsize=12, color='green')
            plt.text(t + 5 / x, k - 0.2, '', fontsize=12, color='blue')

    plt.show()


def plotting_verbs(sample_of_words):  # sample_of_words - object of Class Verbs

    plt.figure(figsize=(16, 10), dpi=80)
    plt.get_current_fig_manager().set_window_title('Dutch Irregular Verbs')

    vertical = []
    horizontal0 = []
    horizontal1 = []
    horizontal2 = []
    horizontal3 = []
    horizontal4 = []
    horizontal5 = []

    for i in range(0, 26):
        vertical.append(i)
        horizontal0.append(0)
        horizontal1.append(1)
        horizontal2.append(2)
        horizontal3.append(3)
        horizontal4.append(4)
        horizontal5.append(5)

    horizontal = []
    vertical0 = []
    vertical1 = []
    vertical2 = []
    vertical3 = []
    vertical4 = []
    vertical5 = []

    for y in range(0, 6):
        horizontal.append(y)
        vertical0.append(0)
        vertical1.append(5)
        vertical2.append(10)
        vertical3.append(15)
        vertical4.append(20)
        vertical5.append(25)

    plt.plot(vertical, horizontal0, color='grey', alpha=.1)
    plt.plot(vertical, horizontal1, color='grey', alpha=.1)
    plt.plot(vertical, horizontal2, color='grey', alpha=.1)
    plt.plot(vertical, horizontal3, color='grey', alpha=.1)
    plt.plot(vertical, horizontal4, color='grey', alpha=.1)
    plt.plot(vertical, horizontal5, color='grey', alpha=.1)
    plt.plot(vertical0, horizontal, color='grey', alpha=.1)
    plt.plot(vertical1, horizontal, color='grey', alpha=.1)
    plt.plot(vertical2, horizontal, color='grey', alpha=.1)
    plt.plot(vertical3, horizontal, color='grey', alpha=.1)
    plt.plot(vertical4, horizontal, color='grey', alpha=.1)
    plt.plot(vertical5, horizontal, color='grey', alpha=.1)

    plt.ylim(0, 5)
    plt.xlim(0, 25)

    y_coord = [0.4, 1.4, 2.4, 3.4, 4.4]

    random.shuffle(y_coord)  # it is necessary to change word order at the plot

    for i, y_c in enumerate(y_coord):
        try:
            plt.text(1, y_c,  sample_of_words[i].getTranslation(), fontsize=12, color='blue')
            plt.text(6, y_c, sample_of_words[i].getWord(), fontsize=12, color='black')
            plt.text(11, y_c, sample_of_words[i].getSecond(), fontsize=12, color='black')
            plt.text(16, y_c, sample_of_words[i].getThird(), fontsize=12, color='black')
            plt.text(23, y_c, sample_of_words[i].getWeight(), fontsize=12, color='black')

        except:
            pass

    plt.show()


def lesson_progress(df):

    data_words_lesson_df = df.copy()
    data_words_lesson_df = data_words_lesson_df.loc[:, ['finish', 'points', 'known', 'r']]
    data_words_lesson_df['date'] = data_words_lesson_df['finish'].apply(lambda x: x.strftime("%d.%m.%Y"))
    conseq = data_words_lesson_df[data_words_lesson_df['known'] != 25]
    conseq = conseq.reset_index()
    sort = conseq.sort_values(by='points', ascending=True)
    sort = sort.reset_index()

    # index of the last lesson
    last = int(conseq['r'].values[-1])
    last_sort = int(sort.index[sort['r'] == last].tolist()[0])

    # determine max points lesson
    sort_max_pts = sort['points'].values[-1]
    sort_min_pts = sort['points'].values[0]
    max_pts_ind = int(sort.index[sort['points'] == sort_max_pts].tolist()[0])
    min_pts_ind = int(sort.index[sort['points'] == sort_min_pts].tolist()[0])
    # for conseq dataframe
    max_pts_ind_con = int(conseq.index[conseq['points'] == sort_max_pts].tolist()[0])
    min_pts_ind_con = int(conseq.index[conseq['points'] == sort_min_pts].tolist()[0])

    # plotting results on a graph
    plt.figure(figsize=(16, 10), dpi=80)
    plt.get_current_fig_manager().set_window_title('Points graphs')

    # create the first subplot
    ax = plt.subplot(2, 1, 1)

    # plot the first bar graph
    for i, d in enumerate(conseq['points']):
        color = 'lightgrey'
        if i == last - 1:  # highlight the last bar
            color = 'plum'
        elif i == max_pts_ind_con:
            color = 'gold'
        ax.bar(i, d, color=color)

    for i in range(len(conseq)):
        if i == max_pts_ind_con or i == min_pts_ind_con or i == (len(conseq) - 1):
            plt.text(x=i, y=conseq.loc[i, 'points'] + 10, s=conseq.loc[i, 'points'], ha='center', va='bottom',
                     color='black', size=7, rotation=90)

    plt.grid(linestyle='--', color='lightgrey', alpha=.2)
    plt.legend(['Consequent'], loc="upper left")
    plt.xlabel('lesson#')
    plt.ylabel('points')

    # adding the average
    plt.axhline(y=np.nanmean(conseq['points']), color='blue', linewidth=0.2, label='Avg')
    # trend line
    x = np.array(range(len(conseq)))
    y = np.poly1d(np.polyfit(x, conseq['points'], 1))(x)
    ax.plot(x, y, color='black', alpha=.2)  # linestyle='--'

    # create the second subplot
    ax2 = plt.subplot(2, 1, 2)
    # plot the second bar graph
    for i, d in enumerate(sort['points']):
        color = 'lightblue'
        if i == last_sort:  # highlight the last lesson bar
            color = 'blue'
        ax2.bar(i, d, color=color)

    for i in range(len(sort)):
        if i == max_pts_ind or i == min_pts_ind or i == last_sort:
            plt.text(x=i, y=sort.loc[i, 'points'] + 10, s=sort.loc[i, 'points'], ha='center', va='bottom',
                     color='black', size=7, rotation=90)

    plt.legend(['Sorted'], loc="upper left")
    plt.grid(linestyle='--', color='lightgrey', alpha=.2)
    plt.xticks(rotation=90)
    plt.ylabel('points')

    # show the plot
    current_time = datetime.now().strftime("%d_%m_%Y")
    plt.savefig(f'data_files/lesson_graph/graph_{current_time}_lesson_{last}.png', dpi=300, bbox_inches='tight')
    plt.show()


def words_progress(df):

    lesson = df.copy()
    # extraction necessary information only - date of lesson finish and list of words
    data_words_lesson_df = lesson.loc[:, ['finish', 'list_of_words']]
    data_words_lesson_df['date'] = data_words_lesson_df['finish'].apply(lambda x: x.strftime("%d.%m.%Y"))
    data_words_lesson_df = data_words_lesson_df.loc[:, ['date', 'list_of_words']]
    data_words_lesson_df['total_words'] = 0

    # list for unique learned words
    new_learned_words = list()

    # determination quantity of unique words learned up to date
    for i in range(len(data_words_lesson_df)):
        temp = data_words_lesson_df.loc[i, 'list_of_words'].split(";")
        for cw in temp:
            if cw.strip() not in new_learned_words:
                new_learned_words.append(cw.strip())
        data_words_lesson_df.loc[i, 'total_words'] = len(new_learned_words)

    # extraction necessary information only - date and quantity of unique words, keeping only final number per day
    data_words_lesson_df = data_words_lesson_df.loc[:, ['date', 'total_words']]
    mask = data_words_lesson_df.duplicated(subset='date', keep='last')
    df = data_words_lesson_df[~mask]
    df = df.reset_index()

    # plotting results on a graph
    plt.figure(figsize=(16, 10), dpi=80)
    plt.get_current_fig_manager().set_window_title('Words per Date')
    plt.bar(df['date'], df['total_words'], color='orange')
    plt.grid(linestyle='--', color='blue', alpha=.3)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Words Total')

    # addition values to bars, I add quantity of new words learned day by day
    for i in range(len(df)):
        if i == 0:
            plt.text(x=i, y=df.loc[i, 'total_words'], s=df.loc[i, 'total_words'], ha='center', va='bottom',
                     color='black', size=8)
        else:
            plt.text(x=i, y=df.loc[i, 'total_words'], s=df.loc[i, 'total_words'] - df.loc[i - 1, 'total_words'],
                     ha='center', va='bottom', color='black', size=8)

    current_time = datetime.now().strftime("%d_%m_%Y")

    plt.savefig(f'data_files/words_graph/words_graph_{current_time}.png', dpi=300, bbox_inches='tight')
    plt.show()