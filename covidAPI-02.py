import requests, json, urllib3

urllib3.disable_warnings()

country = input("Insert the id of the country you want: ")
url = "https://api.covid19tracking.narrativa.com/api/countries/" + country + "/regions"
response = requests.request("GET", url, verify=False)
covid = dict(json.loads(response.text))

for elem in covid["countries"][0][country]:
    print(elem["id"], " - ", elem["name_es"])