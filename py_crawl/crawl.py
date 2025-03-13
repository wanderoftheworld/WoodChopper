import requests
from bs4 import BeautifulSoup

def crawl(url):
  """Crawl a website and return a list of URLs in the same domain."""

  # Get the HTML content of the website.
  response = requests.get(url)
  html = response.text

  # Parse the HTML content.
  soup = BeautifulSoup(html, "html.parser")

  # Find all the links in the website.
  links = soup.find_all("a")

  print(links)
  # Extract the URLs from the links.
  urls = [link["href"] for link in links]

  # Filter the URLs to only include those in the same domain.
  filtered_urls = [url for url in urls if url.startswith(url)]

  # Return the list of URLs.
  return filtered_urls

crawl("covariant.ai")
