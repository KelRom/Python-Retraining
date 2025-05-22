import urllib.request

web_url = urllib.request.urlopen(
    "http://www.example.com")  # this is a real website
print("Result code: ", web_url.getcode())

data = web_url.read()
print(data)
