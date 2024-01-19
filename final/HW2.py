import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

df = pd.read_csv('NBA.csv')
df.head()
df.drop(columns='Unnamed: 0',inplace = True)
numerical_data = df.select_dtypes(include = np.number).columns.to_list()
catogrical_data = df.select_dtypes(exclude= np.number).columns.to_list()
for label in enumerate(catogrical_data):
    print(label)

df.describe().round()
df.info()
df.isnull().sum()

df["college"] = df["college"].fillna("DNE")
df.isnull().sum()

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,5))

plt.suptitle("Distribution of height and weight")

# 身高分布
ax1.hist(df["player_height"],color='#9E96CF')
ax1.axvline(df["player_height"].mean(),color='#EF3D58',label="mean")
ax1.set_xlabel("Height")
ax1.set_ylabel("Count")
# 体重分布
ax2.hist(df["player_weight"],color='#9E96CF')
ax2.axvline(df["player_weight"].mean(),color='#EF3D58',label="mean")
ax2.set_xlabel("Weight")
ax2.set_ylabel("Count")

plt.legend()
plt.show()

# 使用 Plotly 绘制身高与体重的散点图
data = go.Scatter(
    x=df['player_height'],
    y=df['player_weight'],
    mode='markers',
    marker=dict(color='#4A4C76')
)
layout = go.Layout(height=750,
                   width=950,
                   title={
                       'text': "Height vs Weight",
                       'x': 0.4,
                       'y': 0.93,
                       'xanchor': 'center',
                       'yanchor': 'top'
                   },
                   xaxis={'title': 'Height'},
                   yaxis=dict(title='Weight'),
                   template='plotly_white')
fig = go.Figure(data = data , layout = layout)
fig.show()

sns.regplot(df,x='player_height',y='player_weight',color='#2E0D49')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

sns.lineplot(df,x='age',y='gp',errorbar=("se", 0.5))
plt.title("Distribution of age per game play")
plt.xlabel("Age")
plt.ylabel("Game Play")
plt.show()

season_group = df.groupby(df['season']).agg({'age':'mean','player_height':'mean','player_weight':'mean'})
season_group.reset_index(inplace=True)

fig,ax = plt.subplots(1,2,figsize=(12,5))
sns.axes_style()
sns.regplot(season_group,x='age',y='player_height',line_kws={'color':'#e07a5f'},color='#0d3b66',ax=ax[0])
sns.regplot(season_group,x='age',y='player_weight',line_kws={'color':'#e07a5f'},color='#0d3b66',ax=ax[1])
plt.show()

fig,ax = plt.subplots(figsize=(8, 6))

# 年龄
ax.plot(season_group['season'],season_group['age'],color='#ed6a5a')
ax.set_xlabel('Season',labelpad=30,fontsize=15,fontname='Arial')
ax.set_ylabel('Age',labelpad=20,fontsize=13,fontname='Arial')
# 身高
ax_right = plt.twinx()
ax_right.plot(season_group['season'],season_group['player_height'], color='#9bc1bc',label='Height per season')
ax_right.set_ylabel('Height',fontsize=13,labelpad=20)
ax_right.legend()

ax.set_xticklabels(season_group['season'],rotation='vertical')
plt.show()

fig,ax = plt.subplots(figsize =(8, 6))

# 身高
ax.plot(season_group['season'],season_group['age'],color='#0d3b66',label='Age per season')
ax.set_xlabel('Season',labelpad=30,fontsize=15,fontname='Arial')
ax.set_ylabel('Age',labelpad=20,fontsize=13,fontname='Arial')
ax.legend()
# 体重
ax_right = plt.twinx()
ax_right.plot(season_group['season'],season_group['player_weight'], color='#f4d35e')
ax_right.set_ylabel('Weight',fontsize=13,labelpad=20)

ax.set_xticklabels(season_group['season'],rotation='vertical')
plt.show()

teamGroup = df.groupby("team_abbreviation").aggregate({'age':'mean','player_height':'mean','player_weight':'mean'})
teamGroup.reset_index(inplace = True)

fig , (ax1,ax2,ax3)=plt.subplots(1,3,figsize=(19,7))

sns.axes_style()
sns.set_theme(style='white')
# 年龄
sns.histplot(teamGroup,x='age',kde=True,stat="probability",ax=ax1,color='#3E001F')
ax1.set_xlabel('Age',fontsize=17,labelpad=20)
ax1.set_ylabel('Probability',fontsize=17,labelpad=20)
# 身高
sns.histplot(teamGroup,x='player_height',stat="probability",kde=True,ax=ax2,color='#557C55')
ax2.set_xlabel('Height',fontsize=17,labelpad=20)
ax2.set_ylabel('Probability',fontsize=17,labelpad=5)
# 体重
sns.histplot(teamGroup,x='player_weight',stat="probability",kde=True,ax=ax3,color='#7D0A0A')
ax3.set_xlabel('Weight',fontsize=17,labelpad=20)
ax3.set_ylabel('Probability',fontsize=17,labelpad=5)

plt.show()