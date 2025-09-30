import random

with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = file.readlines()

quote = random.choice(quotes).strip()

with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

start = "<!--QUOTE_START-->"
end = "<!--QUOTE_END-->"

newContent = content.split(start)[0] + start + "\n" + quote + "\n" + end + content.split(end)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(newContent)
