# import
import newspaper
import json
import nltk 
# nltk.download('punkt_tab')

def save_htm(article : newspaper.Article) -> dict:
    article.download()
    article.parse()
    data = {
        "url": article.url,
        "title": article.title,
        "text": article.text,
        "authors": article.authors,
        "publish_date": str(article.publish_date)
    }
    return data

def extract_htm(url : str) -> dict:
    article = newspaper.Article(url)
    article.download()
    article.parse()
    article.nlp()
    return {
        "summary": article.summary,
        "keywords": article.keywords
    }

if __name__ == '__main__':
    output_dir = "./data/data.json"
    output_extract_dir = './data/extract_data.json'

    with open(output_dir, "r", encoding='utf-8') as f:
        datas = json.load(f) 
    with open(output_extract_dir, "r", encoding='utf-8') as f:
        data_extract = json.load(f) 

    with open("./data/env.json", "r") as file:
        json_data = json.load(file)    
        print(json_data['newspaper_url'])
        for url in json_data['newspaper_url']:
            print(f'Đọc báo: {url}')
            papers = newspaper.build(url)
            for article in papers.articles:
                data = save_htm(article=article)
                datas.append(data)
                data_extract.append(extract_htm(url=data['url']))



    with open(output_dir, "w", encoding='utf-8') as f:
        json.dump(datas,f, indent=4, ensure_ascii=False)

    with open(output_extract_dir, "w", encoding='utf-8') as f:
        json.dump(data_extract, f, indent=4, ensure_ascii=False)