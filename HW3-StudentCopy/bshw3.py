# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import re
import webbrowser
import requests
from bs4 import BeautifulSoup
 
base_url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
r = requests.get(base_url) 
soup = BeautifulSoup(r.text, "html.parser")

for thing in soup.find_all(text=re.compile("student")):
	string = str(thing) 
	string = string.replace("student", "AMAZING student")
	thing.replaceWith(string)

# from os.path import basename, splitext
# soup = BeautifulSoup(my_html_string)
# for img in soup.findAll('img'):
#     img['src'] = 'cid:' + splitext(basename(img['src']))[0]
# my_html_string = str(soup)

with open("myBSIpage.html", "wb") as file:
	file.write(str(soup).encode())






