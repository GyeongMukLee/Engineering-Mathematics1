import urllib.request
import time

price = 5.0
page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")

while price < 6.2:
    time.sleep(1)
    text = page.read().decode("utf-8")
    price = float(text[text.find(">$")+2:text.find("</st")])
    print(price)

print("커피 가격 인상")
