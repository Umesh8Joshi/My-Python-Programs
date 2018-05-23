# Script Name	: get_youtube_view.py
# Author		: Umesh Joshi
# Created		: 21 December 2016

import time
import webbrowser

print("Enjoy your Time\n" + time.ctime())
for count in range(30):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/")
    
#This will only works when you have less than 300 views.
