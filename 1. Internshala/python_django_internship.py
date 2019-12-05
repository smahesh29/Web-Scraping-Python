from bs4 import BeautifulSoup
import pandas as pd
import requests

job_title = []
company_name=[]
location=[]
start_date=[]
duration=[]
stipends=[]
posted_on=[]
apply_by=[]

res = requests.get('https://internshala.com/internships/python%2Fdjango-internship')
soup = BeautifulSoup(res.text, 'html.parser')
allposts=soup.findAll(True,{'class':"internship_meta"})

for post in allposts:
    job_title.append(post.find('h4',{'title':True}).text.strip())
    company_name.append(post.find('a',{'class':'link_display_like_text'}).text.strip())
    location.append(post.find('a',{'class':'location_link'}).text.strip())

    table=post.find('table')
    
    tds=table.findAll('td')
    
    start_date.append(tds[0].text.strip())
    duration.append(tds[1].text.strip())
    stipends.append(tds[2].text.strip())
    posted_on.append(tds[3].text.strip())
    apply_by.append(tds[4].text.strip())


df = pd.DataFrame({'Job title':job_title,'Company name':company_name,'loaction':location,'start date':start_date,'Duration':duration,'stipends':stipends,'posted on':posted_on,'apply by':apply_by}) 
df.to_excel('python_django_intership.xlsx',index =False, encoding='utf-8')