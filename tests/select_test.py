import requests
from bs4 import BeautifulSoup
  
html = """
<nav class="menu-box-1" id="menu-box">
  <ul class="menu">
    <li class="menu-item">
      <a class="link naver" href="https://www.naver.com">
        네이버로 이동
      </a>      
    </li>
    <li class="menu-item">
      <a class="link google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li class="menu-item">
      <a class="link daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')  

# print(soup)

# select_one, select 연습
# 특징 : 선택자 검색이 가능
# select_one() : 검색한 엘리먼트 중에 첫 번째 요소르 리턴
# print(soup.select_one('li'))
print("== select_one() 검색 ==")
print(soup.select_one('.menu-item'))
print(soup.select_one('.menu-item > a'))

print("== select() 검색 ==")
# print(soup.select('li'))
print(soup.select('.menu-item'))
print(soup.select_one('#menu-box'))

print(soup.select('.menu-item > a'))

for a_el in soup.select('.menu-item > a'):
  # print(a_el.get_text(strip=True)) # strip=True : 텍스트 좌우 공백 제거
  # print(a_el.text) # 텍스트만 출력하는 경우
  print(a_el.get('href')) # 속성명이 href인 엘리먼트의 값 출력
  