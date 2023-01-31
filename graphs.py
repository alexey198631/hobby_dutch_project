"""
This code determines quantity of learned words to dates.
Then it creates graph x-axis: Date, y-axes: Number of learned words

"""
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# import data from existing leaning file with lesson sheet
lesson_df = pd.read_excel('data_files/dutch.xlsx', sheet_name='lesson')

# extraction necessary information only - date of lesson finish and list of words
data_words_lesson_df = lesson_df.loc[:, ['finish', 'list_of_words']]
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
        plt.text(x=i, y=df.loc[i, 'total_words'], s=df.loc[i, 'total_words'], ha='center', va='bottom', color = 'black', size = 8)
    else:
        plt.text(x=i, y=df.loc[i, 'total_words'], s=df.loc[i, 'total_words'] - df.loc[i - 1, 'total_words'],
                 ha='center', va='bottom', color='black', size=8)

current_time = datetime.now().strftime("%d_%m_%Y")

plt.savefig(f'data_files/graph_{current_time}.png', dpi=300, bbox_inches='tight')
plt.show()
