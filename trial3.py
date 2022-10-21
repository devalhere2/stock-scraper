import requests

url = "https://india-trending-stock-api.p.rapidapi.com/india_trending_stocks_by_price"

headers = {
	"X-RapidAPI-Key": "a78531cb44msh9ead90ab086ce21p11e444jsn2803a2fa9afb",
	"X-RapidAPI-Host": "india-trending-stock-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)