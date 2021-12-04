# import requests
#
# response = requests.get(
#     'https://api.thecatapi.com/v1/images/search'
# )
#
# response_data = response.json()
#
# if response.status_code == 200:
#     print(response.status_code)
#     print(response_data)
#     print(response_data[0]['url'])
# else:
#     print("고양이 사진 가져오기 실패!")

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20211203',
                    headers=headers)

#파이썬 문법설명
def minus(a,b)
    return a - b

minus(10,5)
minus(5,10)
munus(b=5,a=10)

#definition 사용할수도 있다
def minus(a,b=10)
munus(100) #90

def munus(a,b, need_print=False)
    if need_print:
        print(a-b)


# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


####

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')



for song in songs:
    a_tag = song.select_one('td.info > a.title.ellipsis')

    if a_tag is not None:
        print(a_tag.text.strip())







