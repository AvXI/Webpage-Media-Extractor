import requests
from bs4 import BeautifulSoup
import re

# Set the URL of the web page to extract media from
url = "https://www.example.com"

# Send a GET request to the web page
response = requests.get(url)

# Parse the HTML content of the web page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all media elements from the web page (e.g., images, videos, audio files)
media_elements = soup.find_all(['img', 'video', 'audio'])

# Extract the URLs of all media files from the media elements
media_urls = []
for element in media_elements:
    if element.name == 'img':
        media_urls.append(element['src'])
    elif element.name == 'video':
        media_urls.append(element.find('source')['src'])
    elif element.name == 'audio':
        media_urls.append(element['src'])

# Download all media files to the local file system
for url in media_urls:
    # Send a GET request to the media file URL
    media_response = requests.get(url)

    # Extract the filename of the media file from the URL
    filename = re.findall(r'/([\w_-]+[.](jpg|gif|png|jpeg|mp4|webm|ogg))$', url)[0][0]

    # Save the media file to the local file system
    with open(filename, 'wb') as f:
        f.write(media_response.content)