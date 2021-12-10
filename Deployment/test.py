import requests

BASE = "http://127.0.0.1:5000/"
price = '123325'
zestimate = '1245895'
rent_zestimate = '125600'
zipcode = '95134'

# response = requests.get(BASE + "predictInvestment/{0}/{1}".format('price', 'zestimate'))
response = requests.get(BASE + "predictInvestment/{0}/{1}/{2}/{3}".format(price, zestimate, rent_zestimate, zipcode))
response.headers.add("Access-Control-Allow-Origin", "*")
print(response.json())
