import requests as rq
from datetime import *
from time import gmtime, strftime
from colorama import *
import os, sys
from time import sleep
def menu():
	print(Fore.BLUE+"="*10, Fore.LIGHTGREEN_EX+"WEATHER ",Fore.BLUE+ "="*10)
	print(Fore.GREEN+"[1]. Thoi tiet hom nay")
	print(Fore.GREEN+"[2]. Thoi tiet 8 ngay sau")
def dtbs():
	url= "https://openweathermap.org/data/2.5/weather?id=1580578&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"
	headers= {
	"Host": "openweathermap.org",
	"Connection": "keep-alive",
	"Accept": r"application/json, text/plain, */*",
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://openweathermap.org/city/1580578",
	"Cookie": "units=metric; _ga=GA1.2.1167238679.1618550676; _gid=GA1.2.410173752.1618550676; stick-footer-panel=false; cityid=1580578; october_session=eyJpdiI6IkNUeXhteU11Vkc2SWMyN3ZpTFlEYWc9PSIsInZhbHVlIjoiZVwvazhuSWpLNlwvZVFaaGpObVZwNDlkVmU4SWpcL2twZ1ZHVzFCbEpEUkd3TEdoRlhSMXhhTlNTVU1FaHdrbjl2ZzVNNVZXamZhS25HaDZnY1lNMURKbXc9PSIsIm1hYyI6IjU5NDFiYTIzM2RiNDZiZTUzMWVmOGJhN2MzMTJjMzk2ZTZiMWRiMTdhNDMxOWQzNjg3Y2UwY2Q3ZmU2NTZmOGQifQ%3D%3D"}
	response= rq.get(url=url, headers=headers)
	return response
def dtbs1():
	url="https://openweathermap.org/data/2.5/onecall?lat=10.8333&lon=106.6667&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02"
	headers={
	"Host": "openweathermap.org",
	"Connection": "keep-alive",
	"Accept": r"application/json, text/plain, */*",
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://openweathermap.org/city/1580578"
	}
	response1=rq.get(url=url, headers=headers)
	return response1
def xu_li1(response1):
	print(Fore.GREEN+"="*10,Fore.CYAN+"DU BAO 8 NGAY", Fore.GREEN+"="*10)
	today=date.today()
	for i in range(0,8):
		sleep(1)
		khu_vuc=(response1.json()["timezone"])
		feel_like=response1.json()["daily"][i]["feels_like"]["day"]
		night=response1.json()["daily"][i]["feels_like"]["night"]
		eve=response1.json()["daily"][i]["feels_like"]["eve"]
		morn=response1.json()["daily"][0]["feels_like"]["morn"]
		ap_suat=response1.json()["daily"][i]["pressure"]
		do_am=response1.json()["daily"][i]["humidity"]
		dew_point=response1.json()["daily"][i]["dew_point"]
		wind_speed=response1.json()["daily"][0]["wind_speed"]
		wind_deg=response1.json()["daily"][i]["wind_deg"]
		wind_gust=response1.json()["daily"][i]["wind_gust"]
		print(Fore.GREEN+"="*20)
		print(Fore.YELLOW+f"Ngay {today.day+i} thang {today.month} nam {today.year}")
		print(Fore.RED+f"Khu vuc: {khu_vuc}\nBan ngay: {feel_like} °c\nBan dem: {night} °c")
		print(Fore.LIGHTBLUE_EX+f"Dem truoc: {eve} °c\nSang: {morn} °c")
		print(Fore.LIGHTBLUE_EX+f"Ap suat: {ap_suat} hPa\nDo am: {do_am} %")
		print(Fore.LIGHTBLUE_EX+f"Diem suong: {dew_point} °c\nToc do gio: {wind_speed} m\s")
		print(Fore.LIGHTBLUE_EX+f"Huong gio: {wind_deg} °\nWind gust: {wind_gust}")
		print(Fore.GREEN+"="*20)
def xu_li(response):
	today=date.today()
	times=datetime.now().time()
	tp= response.json()["name"]
	vitri= response.json()["sys"]["country"]
	nhiet_do= response.json()["main"]["temp"]
	do_am= response.json()["main"]["humidity"]
	hpa= response.json()["main"]["pressure"]
	feel_like= response.json()["main"]["feels_like"]
	hjen_thi= response.json()["visibility"]
	tocdo= response.json()["wind"]["speed"]
	huong= response.json()["wind"]["deg"]
	local=response.json()["coord"]["lon"]
	local1=response.json()["coord"]["lat"]
	print(Fore.GREEN+"="*10,Fore.RED+ "WEATHER TODAY",Fore.GREEN+ "="*10)
	print(Fore.YELLOW+"BAY GIO LA: ", times)
	print(Fore.YELLOW+f"Ngay {today.day} thang {today.month} nam {today.year} ")
	print(Fore.RED+f"Quoc gia: {vitri}\nThanh pho: {tp}")
	print(Fore.LIGHTBLUE_EX+f"Nhiet do hien tai: {nhiet_do} °c\nDo am: {do_am} %")
	print(Fore.LIGHTBLUE_EX+f"Ap suat: {hpa} hPa\nCam giac nhu: {feel_like} °c")
	print(Fore.LIGHTBLUE_EX+f"Tam nhin: {hjen_thi} m\nToc do gio: {tocdo} m\s")
	print(Fore.LIGHTBLUE_EX+f"Huong gio: {huong} °")
	print(Fore.LIGHTBLUE_EX+f"lon: {local}\nlat: {local1}")
	print(Fore.GREEN+"="*10,Fore.CYAN+ "HAHA", Fore.GREEN+"="*10)
def main():
	menu()
	choice=int(input(Fore.YELLOW+"Nhap lua chon: " ))
	sleep(2)
	os.system("clear")
	print(Fore.RED+"Dang tai du lieu...")
	if choice==1:
		x=dtbs()
		xu_li(x)
	elif choice== 2:
		x=dtbs1()
		xu_li1(x)
	else:
		sys.exit()
if __name__=='__main__':
	main() 