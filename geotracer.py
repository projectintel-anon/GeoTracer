from tkinter import *
import requests
import json
from PIL import Image
import urllib
import ssl
import io
import os
try:
	class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
	def ipQuit():
		root.destroy()
		print(f"{bcolors.HEADER}Thanks for using GeoTracer.{bcolors.ENDC}")
		print(f"{bcolors.OKCYAN}Credit: The Enigma Project\n\n Twitter: @enigmapr0ject\n GitHub: @projectintel-anon\n Email: theenigmaproject@cyberservices.com\n\n\n {bcolors.BOLD}Stay safe, guardian.{bcolors.ENDC}")
		exit(0)
	def photoHandler():
		url2 = "https://cache.ip-api.com/" + str(results['lon']) + "," + str(results['lat']) + ",10"
		print(url2)
		gcontext = ssl.SSLContext()
		raw_data = urllib.request.urlopen(url2, context=gcontext).read()
		im = Image.open(io.BytesIO(raw_data)).convert('RGB')
		im1 = im.save("temp.png")
		windowImage = PhotoImage(file="temp.png")
		windowImageLabel = Label(resultWindow, image=windowImage)
		windowImageLabel.photo = windowImage
		windowImageLabel.place(x=500,y=0)
		windowCaption = Label(resultWindow, justify=LEFT, text="Geographical map of lat/long. Credit: https://ip-api.com/", fg="blue", bg="white", font="TkFixedFont")
		windowCaption.place(x=500,y=580)
	def nextQuery():
		try:
			if os.path.exists("temp.png"):
				os.remove("temp.png")
		except:
			print("Exception occurred.")
			pass
		resultWindow.destroy()
		mainGUI()
	def ipQuery():
		queryTerm = ipSearch.get()
		if len(queryTerm) < 1:
			emptyMessage = Label(root, justify=LEFT, text="You cannot submit a blank IP.", fg="red", bg="white", font="TkFixedFont")
			emptyMessage.place(x=40, y=150)
		else:
			url = "http://ip-api.com/json/" + queryTerm + "?fields=66846719"
			page = requests.get(url)
			if page.status_code != 200:
				nfMessage = Label(root, justify=LEFT, text="IP not found.", fg="red", bg="white", font="TkFixedFont")
				nfMessage.place(x=40, y=150)
			else:
				global results
				results = json.loads(str(page.text))
				root.destroy()
				global resultWindow
				resultWindow = Tk()
				resultWindow.geometry('1100x700')
				resultWindow.title(queryTerm)
				resultWindow.configure(bg='white')
				nextButton = Button(resultWindow, text="Close", fg="white", bg="red", font="TkFixedFont", command=nextQuery)
				nextButton.place(x=725,y=650)
				header1 = Label(resultWindow, justify=LEFT, text="Results: ", fg="green", bg="white", font="TkFixedFont")
				header1.place(x=10, y=10)
				r1 = "Status: " + results['status']
				r2 = "Continent: " + results['continent']
				r3 = "Continent Code: " + results['continentCode']
				r4 = "Country: " + results['country']
				r5 = "City: " + results['city']
				r6 = "District: " + results['district']
				r7 = "Zip Code: " + results['zip']
				r8 = "Latitude: " + str(results['lat'])
				r9 = "Longitude: " + str(results['lon'])
				r10 = "Timezone: " + results['timezone']
				r11 = "Offset: " + str(results['offset'])
				r12 = "Currency: " + results['currency']
				r13 = "ISP: " + results['isp']
				r14 = "Organization: " + results['org']
				r15 = "AS: " + results['as']
				r16 = "AS Name: " + results['asname']
				r17 = "Reverse DNS Result: " + results['reverse']
				r18 = "Mobile: " + str(results['mobile'])
				r19 = "Proxy: " + str(results['proxy'])
				r20 = "Hosting: " + str(results['hosting'])
				r21 = "Queried IP: " + str(results['query'])
				r21head = Label(resultWindow, justify=LEFT, text=r21, fg="blue", bg="white", font="TkFixedFont")
				r1head = Label(resultWindow, justify=LEFT, text=r1, fg="blue", bg="white", font="TkFixedFont")
				r2head = Label(resultWindow, justify=LEFT, text=r2, fg="blue", bg="white", font="TkFixedFont")
				r3head = Label(resultWindow, justify=LEFT, text=r3, fg="blue", bg="white", font="TkFixedFont")
				r4head = Label(resultWindow, justify=LEFT, text=r4, fg="blue", bg="white", font="TkFixedFont")
				r5head = Label(resultWindow, justify=LEFT, text=r5, fg="blue", bg="white", font="TkFixedFont")
				r6head = Label(resultWindow, justify=LEFT, text=r6, fg="blue", bg="white", font="TkFixedFont")
				r7head = Label(resultWindow, justify=LEFT, text=r7, fg="blue", bg="white", font="TkFixedFont")
				r8head = Label(resultWindow, justify=LEFT, text=r8, fg="blue", bg="white", font="TkFixedFont")
				r9head = Label(resultWindow, justify=LEFT, text=r9, fg="blue", bg="white", font="TkFixedFont")
				r10head = Label(resultWindow, justify=LEFT, text=r10, fg="blue", bg="white", font="TkFixedFont")
				r11head = Label(resultWindow, justify=LEFT, text=r11, fg="blue", bg="white", font="TkFixedFont")
				r12head = Label(resultWindow, justify=LEFT, text=r12, fg="blue", bg="white", font="TkFixedFont")
				r13head = Label(resultWindow, justify=LEFT, text=r13, fg="blue", bg="white", font="TkFixedFont")
				r14head = Label(resultWindow, justify=LEFT, text=r14, fg="blue", bg="white", font="TkFixedFont")
				r15head = Label(resultWindow, justify=LEFT, text=r15, fg="blue", bg="white", font="TkFixedFont")
				r16head = Label(resultWindow, justify=LEFT, text=r16, fg="blue", bg="white", font="TkFixedFont")
				r17head = Label(resultWindow, justify=LEFT, text=r17, fg="blue", bg="white", font="TkFixedFont")
				r18head = Label(resultWindow, justify=LEFT, text=r18, fg="blue", bg="white", font="TkFixedFont")
				r19head = Label(resultWindow, justify=LEFT, text=r19, fg="blue", bg="white", font="TkFixedFont")
				r20head = Label(resultWindow, justify=LEFT, text=r20, fg="blue", bg="white", font="TkFixedFont")
				disclaimerHead = Label(resultWindow, justify=LEFT, text="Location data is very accurate. however does not pinpoint.\n They are within around 10km of actual location.", fg="red", bg="#cfc6c6", font="TkFixedFont")
				licenseHead = Label(resultWindow, justify=LEFT, text="This tool is for education and recon purposes.\n Any illegal activity is your own doing.", fg="orange", bg="#cfc6c6", font="TkFixedFont")
				r21head.place(x=10,y=40)
				r1head.place(x=10,y=60)
				r2head.place(x=10,y=80)
				r3head.place(x=10,y=100)
				r4head.place(x=10,y=120)
				r5head.place(x=10,y=140)
				r6head.place(x=10,y=160)
				r7head.place(x=10,y=180)
				r8head.place(x=10,y=200)
				r9head.place(x=10,y=220)
				r10head.place(x=10,y=240)
				r11head.place(x=10,y=260)
				r12head.place(x=10,y=280)
				r13head.place(x=10,y=300)
				r14head.place(x=10,y=320)
				r15head.place(x=10,y=340)
				r16head.place(x=10,y=360)
				r17head.place(x=10,y=380)
				r18head.place(x=10,y=400)
				r19head.place(x=10,y=420)
				r20head.place(x=10,y=440)
				disclaimerHead.place(x=10,y=500)
				licenseHead.place(x=10,y=550)
				photoHandler()
				resultWindow.update()
				resultWindow.mainloop()
	def mainGUI():
		global root
		root = Tk()
		root.geometry('300x250')
		root.title('GeoTracer')
		root.configure(bg='white')
		global ipSearch
		ipSearch = Entry(root)
		ipLabel = Label(root, justify=LEFT, text="Enter an IP address", fg="blue", bg="white", font="TkFixedFont")
		ipSubmit = Button(root, text="Search", fg="white", bg="red", font="TkFixedFont", command=ipQuery)
		ipClose = Button(root, text="Exit", fg="white", bg="red", font="TkFixedFont", command=ipQuit)
		ipClose.place(x=50,y=150)
		ipLabel.place(x=50, y=10)
		ipSearch.place(x=50, y=50)
		ipSubmit.place(x=50,y=100)
		root.mainloop()
	mainGUI()
except KeyboardInterrupt:
	ipQuit()
except Exception as e:
	print("Exception has occurred. Please contact the developer and quote the following:\n")
	print("**********************\n")
	print(e)
	print("\n**********************")
