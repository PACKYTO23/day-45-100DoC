from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")
empire_website = response.text
soup = BeautifulSoup(empire_website, "html.parser")
titles_data = soup.find_all(name="h3", class_="title")
titles_list = []

for titles_text in titles_data:
    titles = titles_text.getText()
    titles_list.append(titles)

with open("movies.txt", "w") as file:
    for movie_title in titles_list[::-1]:
        file.write(f"{movie_title}\n")
