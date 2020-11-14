from tkinter import *
import requests
import json
from PIL import Image
import urllib
import ssl
import io
import os
import nmap
import random
import json
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
	def showIP():
		ips = nmapScanner.all_hosts()
		nmapResultWindow = Tk()
		nmapResultWindow.title("Show IPs")
		nmapResultWindow.geometry("200x200")
		nmapResultWindow.configure(bg="black")
		ipsLabel = Label(nmapResultWindow, text=ips, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		ipsSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		ipsLabel.place(x=10,y=10)
		ipsSubmit.place(x=50,y=100)
	def showHost():
		host = nmapScanner[queryTerm].hostname()
		nmapResultWindow = Tk()
		nmapResultWindow.title("Show Hostname")
		nmapResultWindow.geometry("200x200")
		nmapResultWindow.configure(bg="black")
		hostLabel = Label(nmapResultWindow, text=host, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		hostSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		hostLabel.place(x=10,y=10)
		hostSubmit.place(x=50,y=100)
	def scanInfo():
		info = nmapScanner.scaninfo()
		nmapResultWindow = Tk()
		nmapResultWindow.title("Scan Info")
		nmapResultWindow.geometry("450x400")
		nmapResultWindow.configure(bg="black")
		infoLabel = Label(nmapResultWindow, text=json.dumps(info), fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		infoSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		infoLabel.place(x=10,y=10)
		infoSubmit.place(x=50,y=100)
	def state1():
		state = nmapScanner[queryTerm].state()
		nmapResultWindow = Tk()
		nmapResultWindow.title("State")
		nmapResultWindow.geometry("200x200")
		nmapResultWindow.configure(bg="black")
		stateLabel = Label(nmapResultWindow, text=state, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		stateSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		stateLabel.place(x=10,y=10)
		stateSubmit.place(x=50,y=100)
	def protocols():
		protocols = nmapScanner[queryTerm].all_protocols()
		nmapResultWindow = Tk()
		nmapResultWindow.title("Protocols")
		nmapResultWindow.geometry("200x200")
		nmapResultWindow.configure(bg="black")
		protLabel = Label(nmapResultWindow, text=protocols, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		protSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		protLabel.place(x=10,y=10)
		protSubmit.place(x=50,y=100)
	def checkTCP():
		nmapResultWindow = Tk()
		nmapResultWindow.title("Check TCP")
		nmapResultWindow.geometry("300x300")
		nmapResultWindow.configure(bg="black")
		ports1 = nmapScanner[queryTerm]['tcp']
		ports1 = "TCP: " + json.dumps(ports1)
		if len(ports1) > 50:
			fileName = "nmapPorts" + str(random.randint(0,99999))
			with open(fileName, "w") as resultFile:
				resultFile.write(json.dumps(ports1))
				resultFile.close()
			successMessage = "Results have been written to: " + fileName + " in: " + os.getcwd()
			successLabel  = Label(nmapResultWindow, justify=LEFT, text=successMessage, fg="red", bg="black", font="TkFixedFont", wraplength=250)
			successLabel.place(x=10,y=100)
			portSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
			portSubmit.place(x=50,y=250)
		else:
			portLabel1 = Label(nmapResultWindow, text=ports1, wraplength=250, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
			portSubmit = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
			portLabel1.place(x=10,y=10)
			portSubmit.place(x=50,y=250)
	def openPorts():
		nmapResultWindow = Tk()
		nmapResultWindow.title("Open Ports")
		nmapResultWindow.geometry("300x300")
		nmapResultWindow.configure(bg="black")
		ports2 = nmapScanner[queryTerm]['tcp'].keys()
		ports2 = str(ports2)
		ports2 = ports2.replace("dict_keys(", " ")
		ports2 = ports2.replace(")", " ")
		portLabel2 = Label(nmapResultWindow, text=ports2, wraplength=250, fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		portSubmit2 = Button(nmapResultWindow, fg="white", bg="green", text="Close", command=nmapResultWindow.destroy)
		portLabel2.place(x=10,y=10)
		portSubmit2.place(x=50,y=250)
	def checkPort1():
		def portHandle():
			queryPort = nmapPortEntry.get()
			queryPort = int(queryPort)
			ports2 = nmapScanner[queryTerm].has_tcp(queryPort)
			ports=str(ports2)
			queryPort=str(queryPort)
			ports = "Port " + queryPort + " open: " + ports 
			checkedLabel = Label(nmapResultWindow2, text=ports, justify=LEFT, fg="blue", bg="black", font="TkFixedFont")
			checkedLabel.place(x=10,y=160)
			nmapResultWindow2.update()
	def checkPort2():
		def portHandle():
			queryPort = nmapPortEntry2.get()
			queryPort = int(queryPort)
			ports2 = nmapScanner[queryTerm].tcp(queryPort)
			ports=str(ports2) 
			checkedLabel = Label(nmapResultWindow3, text=ports, wraplength=250,justify=LEFT, fg="blue", bg="black", font="TkFixedFont")
			checkedLabel.place(x=10,y=160)
			nmapResultWindow2.update()
		global nmapResultWindow3
		nmapResultWindow3 = Tk()
		nmapResultWindow3.title("Detailed Check")
		nmapResultWindow3.geometry("300x350")
		nmapResultWindow3.configure(bg="black")
		global nmapPortEntry2
		nmapPortEntry2 = Entry(nmapResultWindow3)
		nmapPortSubmitter = Button(nmapResultWindow3, text="Check", fg="white", bg="#00ffff", command=portHandle)
		portLabel2 = Label(nmapResultWindow3, text="Enter a port to check\n service.", fg="white", bg="black", justify=LEFT, font="TkFixedFont")
		portSubmit2 = Button(nmapResultWindow3, fg="white", bg="green", text="Close", command=nmapResultWindow3.destroy)
		portLabel2.place(x=10,y=10)
		nmapPortEntry2.place(x=10,y=60)
		nmapPortSubmitter.place(x=50,y=110)
		portSubmit2.place(x=50,y=300)
	def closeWindow():
		nmapCP.destroy()
	def nmap1():
		def scan():
			prange = nmap1Entry.get()
			if len(prange) < 1:
				errorMessage = Label(nmap1handler, justify=LEFT, text="Cannot scan empty port.", fg="red", bg="black", font="TkFixedFont")
				errorMessage.place(x=10,y=180)
			else:
				nmap1handler.destroy()
				global nmapScanner
				nmapScanner = nmap.PortScanner()
				results = nmapScanner.scan(queryTerm, prange)
				fileName = "nmap" + str(random.randint(0,99999))
				with open(fileName, "w") as resultFile:
					resultFile.write(json.dumps(results))
					resultFile.close()
				global nmapCP
				nmapCP = Tk()
				nmapCP.title("Nmap Control Panel")
				nmapCP.geometry("850x500")
				nmapCP.configure(bg="black")
				nmapCP1 = Button(nmapCP, text="Show IP", height=1, width=5, fg="white", bg="#03fc20", command=showIP)
				nmapCP1.place(x=10,y=10)
				nmapCP2 = Button(nmapCP, text="Show Hostname", height=1, width=10, fg="white", bg="#f71900", command=showHost)
				nmapCP2.place(x=85,y=10)
				nmapCP3 = Button(nmapCP, text="Scan Info", height=1, width=5, fg="white", bg="#00ffff", command=scanInfo)
				nmapCP3.place(x=200,y=10)
				nmapCP4 = Button(nmapCP, text="State", height=1, width=5, fg="white", bg="#f700e7", command=state1)
				nmapCP4.place(x=275,y=10)
				nmapCP5 = Button(nmapCP, text="Protocols", height=1, width=5, fg="white", bg="#f7eb00", command=protocols)
				nmapCP5.place(x=350,y=10)
				nmapCP6 = Button(nmapCP, text="Check TCP", height=1, width=7, fg="white", bg="#fa7d00", command=checkTCP)
				nmapCP6.place(x=425,y=10)
				nmapCP7 = Button(nmapCP, text="Open Ports", height=1, width=7, fg="white", bg="#0288f5", command=openPorts)
				nmapCP7.place(x=515,y=10)
				successMessage = "Results have been written to: " + fileName + " in: " + os.getcwd()
				nmapCP8 = Button(nmapCP, text="Check Port", height=1, width=7, fg="white", bg="#f5025f", command=checkPort1)
				nmapCP8.place(x=605,y=10)
				nmapCP9 = Button(nmapCP, text="Detailed Port Check", height=1, width=15, fg="white", bg="#f50000", command=checkPort2)
				nmapCP9.place(x=695,y=10)
				nmapCP10 = Button(nmapCP, text="Close", height=1, width=15, fg="white", bg="#f50000", command=closeWindow)
				nmapCP10.place(x=10,y=50)
				successMessage = "Results have been written to: " + fileName + " in: " + os.getcwd()
				successLabel  = Label(nmapCP, justify=LEFT, text=successMessage, fg="red", bg="black", font="TkFixedFont")
				successLabel.place(x=10,y=450)
		global nmap1handler
		nmap1handler = Tk()
		nmap1handler.title("Port Scan")
		nmap1handler.geometry("200x200")
		nmap1handler.configure(bg="black")
		global nmap1Entry
		nmap1Entry = Entry(nmap1handler)
		nmap1Submit = Button(nmap1handler, text="Scan port/s", bg="blue", fg="white", command=scan)
		nmap1Label = Label(nmap1handler, justify=LEFT, bg="black", fg="red", text="Enter port/s", font="TkFixedFont")
		nmap1Label.place(x=10,y=0)
		nmap1Entry.place(x=10,y=50)
		nmap1Submit.place(x=10,y=100) 
	def ipQuit():
		root.destroy()
		print(f"{bcolors.HEADER}Thanks for using GeoTracer.{bcolors.ENDC}")
		print(f"{bcolors.OKCYAN}Credit: The Enigma Project\n\n Twitter: @enigmapr0ject\n GitHub: @projectintel-anon\n Email: theenigmaproject@cyberservices.com\n\n\n {bcolors.BOLD}Stay safe, guardian.{bcolors.ENDC}")
		exit(0)
	def photoHandler():
		url2 = "https://cache.ip-api.com/" + str(results['lon']) + "," + str(results['lat']) + ",10"
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
		global queryTerm
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
				nmapButton = Button(resultWindow, text="nmap", fg="white", bg="blue", command=nmap1)
				nmapButton.place(x=825,y=650)
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
		import urllib
		p = urllib.request.urlopen("https://icanhazip.com/", timeout=1)
		ipaddr = p.read()
		p.close()
		ipaddr = str(ipaddr)
		ipaddr = ipaddr.replace("b'", " ")
		ipaddr = ipaddr.replace("'", " ")
		ipaddr = ipaddr.replace("\\n", " ")
		ipaddr = "My IP:\n\n" + str(ipaddr)
		myIP = Label(root, text=ipaddr, justify=LEFT, fg="blue", bg="#c3c4c7", font="TkFixedFont")
		myIP.place(x=150,y=180)
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
