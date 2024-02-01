#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import time
import re
import matplotlib.pyplot as plt

#this program gathers data for how many fics were posted/updated each week for a given tag and/or fandom
#you can search both a tag AND and fandom or just one or the other, the weeks is how far back you are searching
#when entering the tag/fandom, you must put it in double quotations, moreover, any spaces in the term are to be replaced with a + sign

#the default example given will track how many Enemies to Lovers, Harry Potter fanfics were posted/updated each week of the past year



fandom = "Harry+Potter+-+J.+K.+Rowling"            #the fandom you are looking at data from 
tag = "Enemies+To+Lovers"            #this is the tag/trope you are seaching
weeks = 52            #this is how many weeks back you are searching


week_list = []
fic_list = []


while weeks > 0:
    week_list.append(weeks)
    weeks = str(weeks)
    url_skeleton = "https://archiveofourown.org/works/search?work_search%5Bquery%5D=&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D="+weeks+"+weeks+ago&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D="+fandom+"&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D="+tag+"&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc&commit=Search"
    results_page = requests.get(url_skeleton)
    ao3_soup = BeautifulSoup(results_page.text, 'html.parser')
    for el in ao3_soup.find_all("h3", class_= "heading"):
        ficsfound_text = el.get_text()
        ficsverifier = [line.strip("\n") for line in ficsfound_text]
        ficsfound = ("".join(filter(str.isdigit, ficsfound_text) ))
        if ficsverifier[0].isdecimal():
            fic_list.append(ficsfound)
            print(weeks+" Weeks ago: "+ficsfound)

    weeks = int(weeks)
    weeks = (weeks - 1)
    time.sleep(3)
    
plt.scatter(week_list, fic_list, c ="blue")
plt.gca().invert_xaxis()
plt.xlabel("weeks ago")
plt.ylabel("fics posted/updated")
plt.show()

    
#note: as some fics are contiously updated weekly/biweekly, you may notice a disproportionate increase in the number of fics posted/updated when looking at stats from 1-4 weeks ago
# In[ ]:





# In[ ]:




