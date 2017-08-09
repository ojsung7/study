#페이지 소스에 긴 문자열이 있었는데 너무 길어서 파일 입출력으로 함
f=open("challenge2.txt", "r")
s = f.read()
result =""

for c in s:
    if c.isalpha():
        result +=c

print(result)