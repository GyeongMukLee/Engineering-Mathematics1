# 텍스트의 글자 수를 세는 예제

text = """
Lorem ipsum dolor sit amet, 
vix iuvaret omnesque interpretaris eu, 
agam eligendi vis ne, et pri erat omnis concludaturque. 
Qui an soleat ridens. Quo albucius patrioque honestatis ne, 
ea has ridens admodum, sea ad maiestatis appellantur. 
In modo hendrerit reprehendunt vix, ludus mnesarchum duo at, 
ceteros noluisse assentior ad qui. 
Mollis civibus invenire et pri.
"""

words = text.split()

print([(x.upper(), len(x)) for x in words][:5])
