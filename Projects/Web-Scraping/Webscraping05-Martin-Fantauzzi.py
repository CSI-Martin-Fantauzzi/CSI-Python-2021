import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7749&lon=-122.4194#.Yks0di-B1QI")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
#print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
print(period)
desc = tonight.find(class_="short-desc").get_text()
print(desc)
temp = tonight.find(class_="temp-low").get_text()
print(temp)





