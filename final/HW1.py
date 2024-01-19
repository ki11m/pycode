import pandas as pd
import random
import matplotlib.pyplot as plt

# 导入数据
data = pd.read_csv("NBA.csv")

plt.hist(data['age'], bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Player Ages')
plt.show()

top_scorers = data.groupby('season')['pts'].max()
top_scorers = top_scorers.reset_index().merge(data[['season', 'player_name', 'pts']], on=['season', 'pts'], how='left')

for season in top_scorers['season'].unique():
    season_top_scorer = top_scorers[top_scorers['season'] == season]
    print(f"Season {season} Top Scorer: {season_top_scorer['player_name'].values[0]} - {season_top_scorer['pts'].values[0]} points")

filtered_data = data[data['season'].str.startswith('20')].loc[data['season'].str[0:4].astype(int) >= 2010]
random_players = filtered_data.sample(5)
plt.figure(figsize=(10, 6))
plt.bar(random_players['player_name'], random_players['pts'], label='Points')
plt.bar(random_players['player_name'], random_players['reb'], label='Rebounds')
plt.bar(random_players['player_name'], random_players['ast'], label='Assists')
plt.xlabel('Player')
plt.ylabel('Stats')
plt.title('Player Performance Comparison (After 2010): Points, Rebounds, and Assists')
plt.legend()
plt.xticks(rotation=45)
plt.show()

age_groups = [20, 25, 30, 35, 40]
data['age_group'] = pd.cut(data['age'], bins=age_groups, labels=['20-24', '25-29', '30-34', '35-39'])
average_points_by_age_group = data.groupby('age_group')['pts'].mean()
plt.bar(average_points_by_age_group.index, average_points_by_age_group.values)
plt.xlabel('Age Group')
plt.ylabel('Average Points')
plt.title('Average Points by Age Group')
plt.show()

random_player = random.choice(data['player_name'])
player_data = data[data['player_name'] == random_player]
plt.plot(player_data['season'], player_data['pts'], label='Points')
plt.plot(player_data['season'], player_data['reb'], label='Rebounds')
plt.plot(player_data['season'], player_data['ast'], label='Assists')
plt.xlabel('Season')
plt.ylabel('Stats')
plt.title(f'{random_player} Performance Over Time: Points, Rebounds, and Assists')
plt.legend()
plt.xticks(rotation=45)
plt.show()