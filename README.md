# youtube-dl

Download any videos from YouTube playlists.

Requirements
============
Python 3
BeautifulSoup4
PyQt
PyQtWebEngine
pytube
pyyoutube
python-decouple

Usage
=====
You will need a YouTube Data API v3 key. Once you have that, create an `.env` file with the following line:

```
API_KEY=[your_api_key]
```

Once that's in place, run the script and paste your playlist ID into the box. For example, if your playlist link is `https://www.youtube.com/playlist?list=PL-ediu19xm1lks-198omxdksj`, you would just paste `PL-ediu19xm1lks-198omxdksj` into the box, and then click the `Get Videos` button. Once the videos have loaded, select the ones you want and click `Download Start`.

When the videos have downloaded, close the window. Done.