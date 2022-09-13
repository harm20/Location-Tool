from geoip import geolite2
ip = input("Enter The IP : " )
locator = geolite2.lookup(ip)
if locator is None :
  print("UNKNOWN")
else :
  print(locator.location)
