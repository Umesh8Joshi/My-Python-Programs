
'''
	Python script to send email anonymous
'''
import mechanicalsoup
import sys

def readfiletostring(file):
	with open(file, 'r') as f:
		return f.read().replace('\n', '')

to = sys.argv[1]
subject = sys.argv[2]
message = readfiletostring(sys.argv[3])
browser = mechanicalsoup.StatefulBrowser()
browser.open('http://anonymouse.org/anonemail.html')
browser.select_form(nr=0)
browser.form['to'] = to
browser.form['subject'] = subject
browser.form['text'] = message
browser.submit_selected()

#displaying results
for link in browser.get_current_page().select('a.result__a'):
	print(link.text, ' ->', link.attrs['href'])

print('Email will be sent within 12 hours')