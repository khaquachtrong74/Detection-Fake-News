#baomoi
import pandas as pd
from newspaper import build
from newspaper import Article
import csv
import requests
from bs4 import BeautifulSoup
# # URL của trang bạn muốn lấy link
# url = 'https://baomoi.com/'

# # Gửi yêu cầu HTTP để lấy nội dung trang
# response = requests.get(url)
# lt = []
# # Kiểm tra xem yêu cầu có thành công không
# if response.status_code == 200:
#     # Phân tích HTML của trang
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Tìm tất cả các thẻ <a> và lấy href
#     links = [a.get('href') for a in soup.find_all('a', href=True)]
    
#     # In ra tất cả các href
#     for link in links:
#         lt.append(link)
# # Define the URL of the news website
# lt = [t for t in lt if "https://" in t]
# print(lt)
cnn_paper = build('https://baomoi.com/',language='vi',memoize_articles=False)
Source =[]
Date=[]
Content=[]
num = 0
# Iterate through the articles
print("So bai viet")
for articles in cnn_paper.articles:#
    article = Article(articles, request_timeout=100,language='vi')
    article.download()
    try:
        article.parse()
        if article.publish_date == None:
            continue
        else:
            num = num + 1
            Source.append(article.url)
            Content.append(article.meta_data['Description'])
            Date.append(article.publish_date)
        print(num)
    except Exception as e:
        pass
df = pd.DataFrame({
    'Date': Date,
    'Content': Content,
    'Source': Source
})
df.to_csv('data_baomoi1.csv',mode='a',header=False,index=False)




