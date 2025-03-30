# 실제 구현 환경

import requests
from bs4 import BeautifulSoup


# GET 요청 (데이터 조회)
resp = requests.get('https://news.naver.com/section/103')

# 상태 코드 확인
print(resp.status_code)  # 200: 성공, 404: 찾을 수 없음, 500: 서버 에러

# 응답 내용 확인
if(resp.status_code == 200):
  # print(resp.url) # url 정보
  # print(resp.json) # json 데이터
  print(resp.text)  # HTML 문서를 가져옴
else:
  print("응답에 실패했습니다.")
  

soup = BeautifulSoup(resp.text, 'html.parser')

# 뉴스기사 제목 검색
news_title = soup.select('.section_latest_article .sa_text_strong')
print(news_title)

news_title_text = []

# 1차 가공 : 뉴스 기사에 제목 텍스트만 추출
for idx, title in enumerate(news_title):  
  title_text = title.get_text(strip=True)
  news_title_text.append(title_text)  
  
# 뉴스 기사 제목 출력
print("== 뉴스 기사 제목 출력 ==")
for i, title in enumerate(news_title_text):
  no = i + 1
  print(f"{no} : {title}")