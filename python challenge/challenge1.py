n = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
result = ""

for c in n:
    if(c>='a'and c<='z'):
        if(c>='y'):
            result += chr(ord(c)-24)
        else:
            result += chr(ord(c)+2)
    else:
        result +=c

print(result)