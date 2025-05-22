'''
JSON DATA IS REPRESENTED AS KEY, VALUE PAIR, VERY SIMILAR TO DICTIONARY

EXAMPLE
{
    "name": "Kelvin Roman",
    "age": 27,
    "skills": ["Python", "C++", "SQL"],
    "address": {
        "street": "12345 coconut drive",
        "city": "Anywhere, USA"
    }
}
'''

import urllib.request
import json
# https://uselessfacts.jsph.pl/api/v2/facts/today
# https://uselessfacts.jsph.pl/api/v2/facts/random

# open the url
web_url = urllib.request.urlopen(
    "https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Result Code: ", web_url.getcode())

# read the JSON data
data = web_url.read()
print(data)

# this parses json data and turns it into a native python dictionay object
the_json = json.loads(data)
print()
print(the_json["text"])
