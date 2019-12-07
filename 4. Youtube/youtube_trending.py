from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

video_titles=[] #List to store title
durations =[] #List to store duration
channels=[] #List to store channel name
urls = [] #List to store url
views=[] #List to store views
descriptions =[] #List to store decription

res = requests.get('https://www.youtube.com/feed/trending')
soup = BeautifulSoup(res.text, 'html.parser')
allvideos=soup.findAll('div',{'class':"yt-lockup-content"})
#print(allvideos)

for video in allvideos:
    title = video.h3.a.text
    duration = video.find('span', {'class':"accessible-description"}).text
    channel_name = video.find('a', {'class':"yt-uix-sessionlink spf-link"}).text
    view = video.find('ul', {'class':"yt-lockup-meta-info"}).contents[1].text
    url = "https://www.youtube.com"
    url += video.find('a', {'href':re.compile(r'[/]([a-z]|[A-Z])\w+')}).attrs['href']
    description = video.find('div', {'class':"yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2"}).text

    video_titles.append(title)
    durations.append(duration[12:])
    channels.append(channel_name) 
    urls.append(url)
    views.append(view)
    descriptions.append(description)

df = pd.DataFrame({'Title':video_titles, 'Duration':durations, 'Channel':channels, 'Url':urls, 'Description':descriptions}) 
df.to_excel('youtube_trending.xlsx', index=False, encoding='utf-8')