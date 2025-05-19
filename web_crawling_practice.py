import requests
from bs4 import BeautifulSoup

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword=기상청"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

# 실제 데이터셋 목록을 찾아서 처리
datasets = soup.find("div", \
class_="data-set-list linked-data dTypeList") \
.find_all("span",class_="title")[0:]

title = []

for dataset in datasets:
  title.append(dataset.text.strip("span").replace("\n", "").replace(" ", ""))

print("기상청 데이터셋 목록")
num = 1
for str in title:
  print(num, str)
  num += 1
