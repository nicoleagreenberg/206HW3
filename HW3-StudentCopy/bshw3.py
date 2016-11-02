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
#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")

for string in soup.find_all(text=re.compile("student")):
	y = str(string) 
	y = y.replace("student", "AWESOME STUDENT")
	string.replaceWith(y)
print (str(soup))

with open("myBSIpage.html", "wb") as file:
	file.write(str(soup).encode())





