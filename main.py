from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(class_="titleline")
article_texts = []
articles_links = []
link_count = 0

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = f"{article_tag.get('href')}{link_count}"
    articles_links.append(link)
    link_count += 1

article_up_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_value = max(article_up_votes)
max_value_index = article_up_votes.index(max_value)

print(f"{article_texts[max_value_index]}\n"
      f"{articles_links[max_value_index]}\n"
      f"{article_up_votes[max_value_index]}\n"
      f"{max_value_index}")


# import lxml-----------------------------------------------------------------------------------------------------------

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")

# print(heading)

# section_heading = soup.find(name="h3", class_="heading")

# print(section_heading)

# name = soup.select_one(selector="#name")

# print(name)

# headings = soup.select(".heading")

# print(headings)-------------------------------------------------------------------------------------------------------
