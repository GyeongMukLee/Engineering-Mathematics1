import urllib.request

page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf-8")
print(text[text.find(">$")+2:text.find("</st")])
