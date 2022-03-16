import requests 
res = requests.get("https://www.gutenberg.org/cache/epub/67635/pg67635.txt")
res.raise_for_status()
playFile = open("Hendrik.text", "wb")
for chunk in res.iter_content(20000):
    playFile.write(chunk)
playFile.close()

