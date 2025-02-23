import sys
from bs4 import BeautifulSoup
import csv
import requests


def scrap_house_data(url, output_file):
    response = requests.get(url)
    if (response.status_code != 200):
        print(f"Failed to retrieve data: {response.status_code}")
        return
    soup = BeautifulSoup(response.text, "html5lib")
    table = soup.find("table")
    if not table:
        print("no table found on the page")
        return
    rows = table.find_all("tr")
    data = []

    headers = [th.text.strip() for th in rows[0].find_all("th")]
    data.append(headers)

    for row in rows[1:]:
        cols = [td.text.strip() for td in row.find_all("td")]
        data.append(cols)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Success !")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scrapper.py data.csv")
        sys.exit(1)
    output_file = sys.argv[1]
    url = "https://data.1337ai.org/"

    scrap_house_data(url, output_file)
