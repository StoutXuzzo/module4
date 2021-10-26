import requests, json, urllib3, datetime

urllib3.disable_warnings()

date = str(datetime.date.today() - datetime.timedelta(days=1))
country = "spain"

url = "https://api.covid19tracking.narrativa.com/api/" + date + "/country/" + country
response = requests.request("GET", url, verify=False)
covid = dict(json.loads(response.text))

print("Spain Data:")
print("Country ", "|", " Today Confirmed ", "|", " Confirmed ", "|", " Deaths ", "|", " Today Deaths")
for elem in covid["dates"][date]["countries"]["Spain"]["regions"]:
    print(elem["name"], elem["today_new_confirmed"], elem["today_confirmed"],elem["today_deaths"], elem["today_new_deaths"], sep=" | ")