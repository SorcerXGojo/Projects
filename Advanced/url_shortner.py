from urllib.parse import urlencode  
from urllib.request import urlopen
import contextlib

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')
    
url = input("Enter the URL: ")
make_mini = make_tiny(url)
print("Shortened URL: ", make_mini)
