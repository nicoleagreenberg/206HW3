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
 
base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = requests.get(base_url) 
soup = BeautifulSoup(r.text, "html.parser")

for thing in soup.find_all(text=re.compile("student")):
	string = str(thing) 
	string = string.replace("student", "AMAZING student")
	thing.replaceWith(string)

for img in soup.findAll('img'):
    img['src'] = 'file:///Users/nicoleackermangreenberg/Documents/F16/SI206/206hw3/HW3-StudentCopy/media/logo.png'
my_html_string = str(soup)


#<a data-flickr-embed="true"  href="https://www.flickr.com/photos/130203562@N04/30655535391/in/dateposted-public/" title="206nicole"><img src="https://c8.staticflickr.com/6/5326/30655535391_6b2bf1c8ac_k.jpg" width="1536" height="2048" alt="206nicole"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
with open("myBSIpage.html", "wb") as file:
	file.write(str(soup).encode())






