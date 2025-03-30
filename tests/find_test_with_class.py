import requests
from bs4 import BeautifulSoup
  
html = """
<nav class="menu-box-1" id="menu-box">
  <ul class="menu">
    <li class="menu-item">
      <a class="link naver" href="https://www.naver.com">네이버로 이동</a>      
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

# find, find_all 연습
print("== find() 검색 ==")
print("-- id 검색 --")
menu_box = soup.find('nav', id="menu-box")
print(menu_box)

print("-- class 검색 --")
menu_item = soup.find('li', class_="menu-item")
print(menu_item)

print("== find_all() 검색 ==")
menu_items = soup.find_all('li', class_="menu-item")
print(menu_items)

links = soup.find_all('a', class_="link")
print(links)

for a_el in links:
  print(a_el.get_text())