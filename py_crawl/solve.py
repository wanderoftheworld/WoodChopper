def count_unique_words(url):
  import requests
  request = requests.get(url)
  text=request.text.lower()
  print(text)
  words = text.split()
  unique_words = frozenset(words)
  return len(unique_words)

print(count_unique_words('http://example.com'))
