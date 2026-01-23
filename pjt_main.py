import requests
from pprint import pprint


# 1. 응답 데이터에서 Key 값들만 따로 추출하여 출력

# 대한민국 서울특별시 중구 지역
lat = 37.56
lon = 126.97
appid = "입력해야 합니다"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"
response = requests.get(url).json()
key_response = response.keys()
# print(key_response)


# 2. 특정 데이터(main, weather)만 추출하여 딕셔너리로 구성하여 출력
specific_data_dict = {}
specific_data_dict['main'] = response['main']
specific_data_dict['weather'] = response['weather']
# pprint(specific_data_dict)

# 3. Key 값들을 모두 한글로 변환
'''
{'base': 'stations',
 'clouds': {'all': 0},
 'cod': 200,
 'coord': {'lat': 37.56, 'lon': 126.97},
 'dt': 1769138430,
 'id': 1835848,
 'main': {'feels_like': 270.03,
          'grnd_level': 1017,
          'humidity': 24,
          'pressure': 1027,
          'sea_level': 1027,
          'temp': 270.03,
          'temp_max': 270.03,
          'temp_min': 269.05},
 'name': 'Seoul',
 'sys': {'country': 'KR',
         'id': 8105,
         'sunrise': 1769121744,
         'sunset': 1769157894,
         'type': 1},
 'timezone': 32400,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 120, 'speed': 1.03}}
'''
korean_data_dict = {}
for res in response:
    if res == 'base':
        korean_data_dict['기본'] = response[res]
    if res == 'clouds':
        korean_data_dict['구름'] = {'구름량': response[res]['all']}
    if res == 'cod':
        korean_data_dict['응답 코드'] = response[res]    
    if res == 'coord':
        korean_data_dict['좌표'] = {'위도': response[res]['lat'], '경도': response[res]['lon']} 
    if res == 'dt':
        korean_data_dict['관측 시각'] = response[res]    
    if res == 'id':
        korean_data_dict['도시 ID'] = response[res]    
    if res == 'main':
        korean_data_dict['주요 정보'] = {
            '체감 온도' : response[res]['feels_like'] ,
            '지면 기압' : response[res]['grnd_level'],
            '습도' :response[res]['humidity'],
            '기압' : response[res]['pressure'],
            '해수면 기압' : response[res]['sea_level'],
            '온도' : response[res]['temp'],
            '최고 온도' : response[res]['temp_max'],
            '최저 온도' : response[res]['temp_min'],
        }    
    if res == 'name':
        korean_data_dict['지역명'] = response[res]    
    if res == 'sys':
        korean_data_dict['시스템 정보'] = {
            '국가': response[res]['country'],
            '아이디': response[res]['id'],
            '일출 시각': response[res]['sunrise'],
            '일몰 시각' : response[res]['sunset'],
            '유형' : response[res]['type'],
        }    
    if res == 'timezone':
        korean_data_dict['시간대'] = response[res]    
    if res == 'visibility':
        korean_data_dict['가시거리'] = response[res]    
    if res == 'weather':
        korean_data_dict['날씨'] = [{
            '상세 설명': response[res][0]['description'],
            '아이콘': response[res][0]['icon'],
            '식별 ID': response[res][0]['id'],
            '주요 상태' : response[res][0]['main'],
        }]       
    if res == 'wind':
        korean_data_dict['바람'] = {
            '풍향': response[res]['deg'], 
            '풍속': response[res]['speed'], 
        }    
# pprint(korean_data_dict)

# 4. 데이터 가공 (섭씨 온도 추가)
# 섭씨(C) = 켈빈(K) - 273.15
korean_data_dict['주요 정보']['온도(섭씨)'] = round(korean_data_dict['주요 정보']['온도'] - 273.15, 2)
korean_data_dict['주요 정보']['체감 온도(섭씨)'] = round(korean_data_dict['주요 정보']['체감 온도'] - 273.15, 2)
korean_data_dict['주요 정보']['최고 온도(섭씨)'] = round(korean_data_dict['주요 정보']['최고 온도'] - 273.15, 2)
korean_data_dict['주요 정보']['최저 온도(섭씨)'] = round(korean_data_dict['주요 정보']['최저 온도'] - 273.15, 2)
# pprint(korean_data_dict)

# 5. 생성형 AI 활용하기
'''
- F105.md에 작성
- F105에 대한 프롬프트(https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221wD3gRi6O2CBzXbgiiYPY35aaK_T_KJTo%22%5D,%22action%22:%22open%22,%22userId%22:%22114430171400724300673%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)

# 1. 한국 서울의 3일 후 날씨 요청
그렇게 할 순 없다

# 2. 현재 한국 부산의 날씨 요청
url = f"https://api.openweathermap.org/data/2.5/weather?lat=35.1796&lon=129.0756&appid={appid}&lang=kr"
response = requests.get(url).json()
pprint(response)

# 3. 1000년 후의 뉴욕 날씨 요청
그렇게 할 순 없다

# 4. 서울 반대편에 있는 나라의 수도 날씨 요청
url = f"https://api.openweathermap.org/data/2.5/weather?lat=-34.9011&lon=-56.1645&appid={appid}&lang=kr"
response = requests.get(url).json()
pprint(response)
'''
