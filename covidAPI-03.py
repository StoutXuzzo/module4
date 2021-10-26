import requests, json, urllib3

urllib3.disable_warnings()

date = "2021-10-24"
country = "spain"

url = "https://api.covid19tracking.narrativa.com/api/" + date + "/country/" + country
response = requests.request("GET", url, verify=False)
covid = dict(json.loads(response.text))

print("Global Data:")
print("Country ", "|", " Confirmed ", "|", " Today Confirmed ", "|", " Deaths ", "|", " Today Deaths")
print("Spain" ,covid["dates"][date]["countries"]["Spain"]["today_confirmed"], covid["dates"][date]["countries"]["Spain"]["today_new_confirmed"] ,covid["dates"][date]["countries"]["Spain"]["today_deaths"], covid["dates"][date]["countries"]["Spain"]["today_new_deaths"], sep=" | ")
print("World" ,covid["total"]["today_confirmed"], covid["total"]["today_new_confirmed"] ,covid["total"]["today_deaths"], covid["total"]["today_new_deaths"], sep=" | ")
