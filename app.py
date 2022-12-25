from flask import Flask, render_template
from newsapi import NewsApiClient
import datetime

app = Flask(__name__)

def Rept_Insrt(ctg):

    newsapi = NewsApiClient(api_key = "36a0b041abac466fa22bae146381b424")

    topheadlines = newsapi.get_top_headlines(category=ctg)
    
    articles = topheadlines['articles']

    img, title, author, source, publishedAt, url, desc = [],[],[],[],[],[],[]


    for i in range(len(articles)):
        myarticles = articles[i]
        Url_image, Title, Author, Source, PublishedAt, Url  = myarticles['urlToImage'], myarticles['title'], myarticles['author'], myarticles['source']['id'], myarticles['publishedAt'][0:10], myarticles['url']
        Content = myarticles['content']
        if Content == None:        
            desc.append("-")
        else :
            desc.append(Content[0:200])

        if Url_image != None:
            img.append(Url_image)
            title.append(Title)
            publishedAt.append(myarticles['publishedAt'][0:10]+" At " +myarticles['publishedAt'][11:16]+ " UTC")
            url.append(Url)
            author.append(Author)
            source.append(Source)

    mylist = zip(img, title, author, source, publishedAt, url, desc)

    return mylist


@app.route('/')
def Index():
    return render_template('index.html', context = Rept_Insrt("general"))



@app.route('/Business')
def Business():
    return render_template('Business.html', context = Rept_Insrt("business"))


@app.route('/Entertainment')
def Entertainment():
    return render_template('Entertainment.html', context =  Rept_Insrt("entertainment"))

@app.route('/Health')
def Health():
    return render_template('Health.html', context = Rept_Insrt("health"))

@app.route('/Science')
def Science():
    return render_template('Science.html', context = Rept_Insrt("science"))

@app.route('/Sports')
def Sports():
    return render_template('Sports.html', context = Rept_Insrt("sports"))

@app.route('/Technology')
def Technology():
    return render_template('Technology.html', context = Rept_Insrt("technology"))


if __name__ == "__main__":
    app.run(debug=True)
