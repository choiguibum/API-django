from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://naver.com")
bsObject = BeautifulSoup(html, "html.parser")
titlelist = bsObject.select('.PM_CL_realtimeKeyword_rolling')

find_text = str(titlelist[0].find('span',{'class' : 'ah_k'}))
find_text = re.sub('<.+?>','',find_text,0).strip()
print('실시간 1위 :',find_text)