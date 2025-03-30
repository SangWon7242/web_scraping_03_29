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
