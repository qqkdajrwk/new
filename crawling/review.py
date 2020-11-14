import urllib.request

class Review:
    def __init__(self,comment,date,star,good,bad):
        self.comment = comment
        self.date = date
        self.star = star
        self.good = good
        self.bad = bad

    def show(self):
        print('내용 : ' +self.comment + 
               '\n 날짜:'+self.date +
               '\n 별점:'+self.star+
               '\n 좋아요:'+self.good+
               '\n 싫어요:'+self.bad
               )

# review=Review('날씨굿','2020','다섯개','100','20')
# review.show()