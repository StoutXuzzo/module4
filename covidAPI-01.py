import requests, json,urllib3
urllib3.disable_warnings()

url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
covid = dict(json.loads(response.text))

#print("List of countries:")
#for i in range(len(covid["countries"])):
#    print(covid["countries"][i]["id"], " - " ,covid["countries"][i]["name_es"])

for count in covid["countries"]:
    print(count["id"], " - ", count["name_es"])