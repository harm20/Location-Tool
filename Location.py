from geoip import geolite2 
print("WELCOME HARM TOOL")
ip = input("Enter The IP : " )
locator = geolite2.loockup(ip)
if locator is None :
  print("UNKNOWN")
else :
  print(locator.location)
