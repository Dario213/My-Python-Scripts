from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Untitled')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x80")



# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=CD03D852-56B1-42A9-A486-192A6A4DB9BE


def zipSearch():
	#zip_lbl = Label(root, text = zip.get())
	#zip_lbl.grid(row = 1, column = 0, columnspan = 2)

	try:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=CD03D852-56B1-42A9-A486-192A6A4DB9BE")
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color = "#00E400"
		elif category == "Moderate":
			weather_color = "#ffff00"
		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff7e00"
		elif category == "Unhealthy":
			weather_color = "#ff0000"
		elif category == "Very Unhealthy":
			weather_color = "#8F3F97"
		elif category == "Hazardous":
			weather_color = "#7E0023"


		root.configure(background = weather_color)

		my_lbl = Label(root, text = city + " Air Quality: " + str(quality) + ", " + category, font = ("Helvetica", 20), background = weather_color)
		my_lbl.grid(row = 1, column = 0, columnspan = 2)

	except Exception as e:
		api = "Error..."




zip = Entry(root)
zip.grid(row = 0, column = 0, stick = W+E+N+S)

zipBtn = Button(root, text = "Search zipcode", command = zipSearch)
zipBtn.grid(row = 0, column = 1, stick = W+E+N+S)


root.mainloop()
