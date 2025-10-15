import requests

# url = f"https://wttr.in/jeju?format=%C+%t"
# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
url0 = f"https://wttr.in/incheon?&0&Q"
url = f"https://wttr.in/incheon?&1"

response0 = requests.get(url0)
response = requests.get(url)
contesnt = response.text

print('오늘은 우산이 필요할까요?!')
print('두구두구')

print(response0.text.strip())

if 'rain' in contesnt:    
    print("우산을 꼭 챙기세요!")
else:
    print("우산이 필요 없네요~")