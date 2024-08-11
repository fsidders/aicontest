from GoogleNews import GoogleNews


def getNews(text, numbers, language="en", region="US", period="2d"):
    googlenews = GoogleNews(lang=language, region=region, period=period)

    googlenews.search(text)

    news = googlenews.get_texts()

    list_news = ""

    i = 0
    for title in news:
        if title:
            list_news = list_news + title + "\n"
            i = i + 1
        if i == numbers:
            break
    return list_news
