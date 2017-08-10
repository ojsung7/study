#처음에는 대문자3개가 나오는걸 카운트하고 그후에 소문자면 변수에넣고 아니면 카운트를 초기화하는걸로했는데 대문자가 연속으로 4번 5번도 나와서 정규표현식을 사용함
import re

f = open("challenge3.txt", "r")
s = f.read()

a1 = re.compile("[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+")

result = a1.findall(s)

f.close()

print(result)