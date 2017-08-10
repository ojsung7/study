import requests
import re

count = 0
result = 0
source = ""

for c in range(0,100):
    if(count==0):
        t = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
        source = t.text
        a = re.compile("[0-9]")
        result = a.findall(source) #리스트로 저장됨
        result = "".join(result) #join 함수를 통해서 리스트를 문자열로 바꿔줌
        print(result)
        count=1
    else:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        t = requests.get(url+result)
        source = t.text
        a = re.compile("[0-9]")
        result = a.findall(source) #리스트로 저장됨
        result = "".join(result) #join 함수를 통해서 리스트를 문자열로 바꿔줌
        print(result)