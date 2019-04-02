import sys
import requests
from bs4 import BeautifulSoup
import csv
import asyncio
from collections import Counter


async def request(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    s = soup.find_all('div', attrs={"class": ["comment__head"]})
    return s


async def parsing(url):
    temp = []
    res = []

    s = await request(url)

    for i in enumerate(s):
        temp.append((s[list(i)[0]].find('a')['data-user-login']))

    temp = dict(Counter(temp))
    for key, value in temp.items():
        res.append({"link": url, "username": key, "count_comment": value})

    return sorted(res, key=lambda x: (-x["count_comment"], x['username']))


def form_file(res):
    sorted_res = [j for i in res for j in i.result()]
    sorted_res = sorted(sorted_res, key=lambda x: x['link'])

    with open(filename, "w", newline="") as file:
        columns = ["link", "username", "count_comment"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(sorted_res)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    tasks = []
    loop = asyncio.get_event_loop()
    for link in links:
        tasks.append(loop.create_task(parsing(link)))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    form_file(tasks)
