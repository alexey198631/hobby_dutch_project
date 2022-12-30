import matplotlib.pyplot as plt
import random


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