import requests
from bs4 import BeautifulSoup as bs
from datetime import date

URL = "https://www.imensa.de/freiburg/mensa-flugplatz/{}.html"

print("\n" + "-" * 50)
print("Speiseplan für Mensa Flugplatz:\n")
for i in range(3):
    day = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"][(date.today().weekday() + i) % 7]
    r = requests.get(URL.format(day))
    soup = bs(r.content, 'html.parser')
    meals = soup.find_all("p", class_ = "aw-meal-description")
    print(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"][(date.today().weekday() + i) % 7] + (" (heute):" if i == 0 else ":"))
    if len(meals) == 0: print("    Heute keine Essensausgabe")
    for j, meal in enumerate(meals):
        if (meal.text != "Heute keine Essensausgabe"): print("  Essen " + str(j + 1) + ":")
        print("    " + meal.get_text(separator="\n    "))

print("-" * 50, "\n", sep="")
