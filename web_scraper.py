import requests
from bs4 import BeautifulSoup

url = input("Enter a website URL (e.g., 'vulnhub.com'): ")

try:
    r = requests.get("http://" + url, timeout=5)  # Adding a timeout to avoid hanging requests
    r.raise_for_status()  # Raise an error for HTTP errors (e.g., 404, 500)
    
    soup = BeautifulSoup(r.text, "html.parser")  # Initialize BeautifulSoup
    title = soup.title.text if soup.title else "No title found"  # Handle missing title
    all_links = soup.find_all("a")  # Find all anchor tags
    
    
    print("Website Title:", title) # Print the title of the website
    print("All Links: ") # Print all links found on the website
    for link in all_links:
        print(link.get("href"))

except requests.exceptions.RequestException as e:
    print("Error:", e)
