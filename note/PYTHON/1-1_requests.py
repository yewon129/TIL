# 웹 사이트의 정보를 가지고 오고 싶다.
import requests
from bs4 import BeautifulSoup
# 1. 요청
## 정보가 있는 사이트 url (주소)
URL = 'https://finance.naver.com/sise/'
## url 요청
# https://docs.python-requests.orgg/en/latest/user/quickstart/#make-a-request
# response (200) <= 성공적으로 가져왔다.
response = requests.get(URL).txt
# print(type(response)) #type : string

# 2-1. BeautifulSoup (text = > 다른 객체)
# Beautiful Soup is Python library for pulling data out of HTML and XML files.

data = BeautifulSoup(response, 'html.parser')
# print(type(data),type(response)) # class'bs4.BeautifulSoup
#2-2 원하는 정보를 뽑아서 출력한다.
#선택자 = selector
kospi = data.select_one('#KOSPI_now')
print(kospi.text)