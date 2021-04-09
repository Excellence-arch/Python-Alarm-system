import datetime
import playsound
import time
you = input("Enter your time in the format hh:mm:ss> ")
choice = you.split(":")
# print(choice)
while True:
	realTime = datetime.datetime.now()
	if realTime.strftime('%I') == choice[0] and realTime.strftime('%M') == choice[1] and realTime.strftime('%S') == choice[2]:
		print("It is time")
		playsound.playsound('C:\\Users\\user\\Music\\Dunsin Oyekan_Open Up.mp3')