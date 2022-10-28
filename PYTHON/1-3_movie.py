import requests

# 1. URL 및 요청변수 설정
BASE_URL = 'httpl://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key' : '8854669b886a6c07c12ea947bcc2311d',
    'region' : 'KR',
    'languge' : 'ko'
}
# 2. 유청 보낸 결과 저장
response = requests.get(BASE_URL+path, params = params)
print(response.status_code, response.url)
data = response.json
# 3. 조작
# print(response)

print(type(data))
print(data.keys())
print(type(data.get('results'))) # list
print(data.get('results')[0]) # list 첫번째 구조
print(type(data.get('results')[0])) # dict
print(len(data.get('results'))) # 20개