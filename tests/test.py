# 테스트 환경

import requests
from bs4 import BeautifulSoup

'''
# GET 요청 (데이터 조회)
resp = requests.get('https://www.naver.com/')

# 상태 코드 확인
print(resp.status_code)  # 200: 성공, 404: 찾을 수 없음, 500: 서버 에러

# 응답 내용 확인
if(resp.status_code == 200):
  # print(resp.url) # url 정보
  # print(resp.json) # json 데이터
  print(resp.text)  # HTML 문서를 가져옴
else:
  print("응답에 실패했습니다.")
'''
  
html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="naver" href="https://www.naver.com">네이버로 이동</a>
      <img src="이미지경로" alt="대체 텍스트">
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')  

# print(soup)

# find, find_all 연습
# 특징 : HTML 태그로만 검색이 가능, 선택자 사용이 불가능
# find() 검색한 결과는 엘리먼트 중에 첫 번째를 찾아서 리턴
print("== find() 검색 ==")
print(f"find 검색1 : {soup.find('li')}")
print(f"find 검색2 : {soup.find('a')}")
print(f"find 검색3 : {soup.find('span')}")

print("== find_all() 검색 ==")
# find_all() 로 검색한 결과는 list로 리턴
find_all_li = soup.find_all('li')
# print(find_all_li)
for i, li in enumerate(find_all_li):
  print(f"{i} : {li}")
  
find_all_a = soup.find_all('a')  
print(find_all_a)
for i, a in enumerate(find_all_a):
  a_txt = a.get_text()
  print(f"{i} : {a_txt}")