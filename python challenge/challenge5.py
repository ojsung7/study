#텍스트파일을 네트워크로 전송할때 직렬화 시켜줘야함, 파이썬에서 pickle모듈로 직렬화 역직렬화 가능
#튜플 개념 확인해야하는 문제
import pickle

f = open("banner.p","rb")
d= pickle.load(f)
result = ""

for x in range (0, len(d)):
    for y in range (0, len(d[x])):
        result += d[x][y][0] * d[x][y][1]
    result += "\n"

print(result)