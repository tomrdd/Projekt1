

import requests
from datetime import datetime

name = input("Wie heißt du? ")
print(f"Hallo, {name}!")

# Aktuelle Zeit ausgeben
jetzt = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(f"Aktuelle Zeit: {jetzt}")

# Wetter für Innsbruck abfragen
API_KEY = " 12e4adfe072608a1bb603b82e30b7499 "  # Trage hier deinen OpenWeatherMap API-Key ein
url = f"https://api.openweathermap.org/data/2.5/weather?q=Innsbruck,AT&appid={API_KEY}&units=metric&lang=de"
try:
	response = requests.get(url)
	data = response.json()
	if data.get("weather") and data.get("main"):
		wetter = data["weather"][0]["description"]
		temp = data["main"]["temp"]
		print(f"Wetter in Innsbruck: {wetter}, {temp}°C")
		if "coord" in data:
			lat = data["coord"].get("lat")
			lon = data["coord"].get("lon")
			print(f"Koordinaten von Innsbruck: Breite {lat}, Länge {lon}")
		else:
			print("Koordinaten von Innsbruck konnten nicht abgerufen werden.")
		if not (data.get("weather") and data.get("main")):
			print("Konnte Wetterdaten nicht abrufen. Prüfe den API-Key.")
			if "message" in data:
				print(f"Fehlermeldung von OpenWeatherMap: {data['message']}")
except Exception as e:
	print(f"Fehler bei der Wetterabfrage: {e}")

