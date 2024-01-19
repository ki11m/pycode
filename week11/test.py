import requests
from bs4 import BeautifulSoup
import csv

# 设置豆瓣电影页面的URL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://movie.douban.com/subject/1292722/reviews'

# 发送HTTP请求获取页面内容
response=requests.get(url,headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("无法访问网页")
    exit()

data = []

# 查找评论元素
reviews = soup.find_all('div', class_='review-item')

# 遍历评论元素并提取信息
for review in reviews:
    reviewer = review.find('a', class_='name').text.strip()
    rating = review.find('span', class_='main-title-rating')
    if rating:
        rating = rating.text.strip()
    else:
        rating = '未评分'
    content = review.find('div', class_='short-content').text.strip()

    # 将提取的信息添加到数据列表中
    data.append([reviewer, rating, content])

# 将数据保存到CSV文件
with open('titanic_reviews.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['评论者', '评分', '评论内容'])  # 写入CSV文件头
    csv_writer.writerows(data)  # 写入数据行

print("数据已成功抓取并保存为CSV文件：titanic_reviews.csv")