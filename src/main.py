# 실제 구현 환경

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import openpyxl


# GET 요청 (데이터 조회)
resp = requests.get('https://news.naver.com/section/104')

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
  
# 특정 키워드로 제목 검색  
# title.find(keyword) -> 결과값이 0아니면 -1
# 0인 경우에 내가 원하는 키워드가 존재한다.
# -1인 경우에는 내가 원하는 키워드가 존재하지 않는다.

print("== 키워드로 뉴스 기사 검색 ==")
find_keyword_list = []
keyword = '트럼프'
for i, title in enumerate(news_title_text):
  no = i + 1    
  
  if title.find(keyword) != -1:
    # print(f"{no} : {title}")
    find_keyword_list.append(title)
    
print(find_keyword_list) # 특정 키워드로 걸러진 데이터가 리스트에 저장

# 특정 키워드를 가진 뉴스 기사 제목을 반복문을 이용한 출력
print("== 키워드 뉴스 제목 리스트 순회 ==")
for i, title in enumerate(find_keyword_list):
  print(f"{i + 1} : {title}")
  
# 두 리스트의 길이를 맞춰주기
max_length = max(len(news_title_text), len(find_keyword_list))
news_title_text = news_title_text + [None] * (max_length - len(news_title_text))
find_keyword_list = find_keyword_list + [None] * (max_length - len(find_keyword_list))  

# 엑셀에 데이터를 저장하기 위해서는 딕셔너리가 필수!  
news_list = {
  '뉴스 제목': news_title_text,
  '키워드 뉴스 제목' : find_keyword_list
}  

def save_to_excel(news_list, filename=None):
    # 파일명이 지정되지 않은 경우 현재 날짜로 생성
    if filename is None:
      current_date = datetime.now().strftime('%Y%m%d')
      filename = f'news_data_{current_date}.xlsx'
    
    try:
      # 데이터프레임 생성(추출한 데이터를 엑셀에 저장)
      df = pd.DataFrame(news_list)
      
      save_path = f"C:\work\python_projects\scrap_data\{filename}"
      
      # 엑셀 파일로 저장
      df.to_excel(save_path, index=False, engine='openpyxl')
      
      print(f"데이터가 성공적으로 {filename}에 저장되었습니다.")
      
      # 기본적인 데이터 통계 출력
      print("\n데이터 통계:")
      print(f"총 기사 수: {len(df)}")
        
    except Exception as e:
        print(f"엑셀 저장 중 오류 발생: {e}")  

# 엑셀에 데이터 저장 함수 실행
save_to_excel(news_list)