from pytube import YouTube, Channel # type: ignore
import pyperclip # type: ignore
import requests
from bs4 import BeautifulSoup

def get_id(video_url):
    x = YouTube(video_url)
    chid=x.channel_id
    url = x.channel_url
    return url, chid




def fetch_thumbnail(url):
    channel_url = url
    # Send a request to get the HTML content of the channel page
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the link tag with itemprop="thumbnailUrl"
    link_tag = soup.find('link', {'itemprop': 'thumbnailUrl'})

    # Extract the href attribute value
    if link_tag and 'href' in link_tag.attrs:
        thumbnail_url = link_tag['href']
        return thumbnail_url
    else:
        print("Thumbnail URL not found.")




def m3u8gen(url, chid, thumbnail):
    y = Channel(url)
    ch_name = y.channel_name
    stream = f"https://ythls-v3.onrender.com/channel/{chid}.m3u8"
    stream1 = stream
    placeholder = "#EXTINF:-1 tvg-logo="+thumbnail+", "+ch_name+"\n" + stream1
    print(placeholder)
    pyperclip.copy(placeholder)
    print("Copied to clipboard 🎉🎇")





while True:
    video_url = input("✨ Paste video url: ")
    if video_url == '':
        break
    else:
        url,chid = get_id(video_url)
        thumbnail = fetch_thumbnail(url)
        m3u8gen(url,chid,thumbnail)
