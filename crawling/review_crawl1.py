import urllib.request
from bs4 import BeautifulSoup as bs
from review import Review
import pandas as pd

def crawl(url):
    data = urllib.request.urlopen(url).read()
    review_list = []
    soup = bs(data, "html.parser")
    # print(soup)
    # soup.select("h3 > a")[0].text
    title = soup.find('h3', class_="h_movie").find('a').text
    div = soup.find("div", class_="score_result")
    data_list = div.select("ul > li")

    # print(data_list)
    for review in data_list:
        star = review.find("div" ,class_="star_score" ).text.strip()
        reply = review.find("div", class_="score_reple")
        comment = reply.find("p").text
        date = reply.select("dt > em")[1].text.strip()
        button = review.find("div", class_="btn_area")
        sympathy = button.select("strong")
        good = sympathy[0].text
        bad = sympathy[1].text
        review_list.append(Review(comment , date, star , good, bad))

    return title , review_list

# title , reiview_list = crawl('https://movie.naver.com/movie/bi/mi/basic.nhn?code=38899')
# print('제목:'+title)
# print(reiview_list[3].star)
# for review in reiview_list:
#     review.show()


def get_summary(review_list):
    star_list=[]
    good_list=[]
    bad_list=[]

    for review in review_list:
        star_list.append(review.star)
        good_list.append(review.good)
        bad_list.append(review.bad)

        star_series = pd.Series(star_list)
        good_series = pd.Series(good_list)
        bad_series = pd.Series(bad_list)

        summary = pd.DataFrame({
            'Star':star_series,
            'Good':good_series,
            'Bad':bad_series,
            'Score':int(good_series)/(int(good_series) + int(bad_series))
        })

        return summary

# reiview_data = crawl('https://movie.naver.com/movie/bi/mi/basic.nhn?code=38899')
# print(reiview_data[1][0])


movie_code_list = [136900 , 167657 , 174321 , 184859, 167391]

review_lists =[]

for i in movie_code_list:
    title, review_list = crawl("https://movie.naver.com/movie/bi/mi/basic.nhn?code="+str(i))
    summary = get_summary(review_list)
    print("[%s]" %(title))
    print(summary)
    review_lists.append((title , review_list))


# print(review_lists)

import matplotlib
