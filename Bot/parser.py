import requests
from bs4 import BeautifulSoup


html = requests.get("https://vc.ru").text
soup = BeautifulSoup(html, 'html5lib')

times_list = []
times = soup.find_all(class_='time')

for time in times:
    time = time.get('title')
    times_list.append(time)


one=times_list[0]
two=times_list[0]
for i in range(1,len(times_list)):
    if times_list[i]>one:
        two=one
        one=times_list[i]
    elif times_list[i]>two:
            two=times_list[i]
    else:
        pass
index_second_max_time = times_list.index(two)
index_first_max_time = times_list.index(one)


def get_first_news():
    news = soup.find_all(class_= "content-title content-title--short l-island-a")
    return news[index_first_max_time].text

print( get_first_news())

def get_second_news():
    news = soup.find_all(class_= "content-title content-title--short l-island-a")
    return news[index_second_max_time ].text

print( get_second_news())