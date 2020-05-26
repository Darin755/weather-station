import requests
import subprocess
import os

p = subprocess.Popen("/root/weather/bitlashScripts/getTemp", stdout=subprocess.PIPE, shell=True)
 
(output, err) = p.communicate()

tempf = int(output)

p = subprocess.Popen("/root/weather/bitlashScripts/getHumidity", stdout=subprocess.PIPE, shell=True)
 
(output, err) = p.communicate()

humidity = int(output)

#print("temp is: " + str(tempf))
#print("Humidity is: " + str(humidity))

# create a string to hold the first part of the URL
WUurl = "https://weatherstation.wunderground.com/weatherstation\
/updateweatherstation.php?"
WU_station_id = "KCOCOLOR1467" # Replace XXXX with your PWS ID
WU_station_pwd = "tkPQQHul" # Replace YYYY with your Password
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

humidity_str = "{0:.2f}".format(humidity)
temp_str = "{0:.2f}".format(tempf)

r= requests.get(
    WUurl +
    WUcreds +
    date_str +
    "&humidity=" + humidity_str + "&tempf=" + temp_str +
    action_str)
#print("Received " + str(r.status_code) + " " + str(r.text))

log1 = '"'+'<'+date_str+' temp='+temp_str+' Humidity='+humidity_str+' status='+str(r.status_code) + ' ' + str(r.text)+'>'+'"'
log2 = "echo "+log1+" >> "+"/root/weather/log"
os.system(log2)
