import requests
import cloudscraper
from fake_useragent import UserAgent
ua = UserAgent()
PROXY_URLS = {
  'http': "http://109.248.7.158:10331",
  'https': "http://109.248.7.158:10331",
}

headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip',
    'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cache-Control':'max-age=0, no-cache',
    'Connection':'keep-alive',
    'Cookie':'u=2t5r96hb.qc2hmr.ix83oxlofp00; buyer_laas_location=623130; _gcl_au=1.1.725826275.1643892381; _ym_uid=1643892381149456966; _ym_d=1643892381; sessid=89582a544d47a7c1965d9e73073d3ab8.1643892519; auth=1; _gcl_aw=GCL.1643898163.CjwKCAiAl-6PBhBCEiwAc2GOVI8ysNNMNWcrs8vmdU18VQp0HTIMSt4Cru3RQl0dzCKprvL9FZM1VhoCdQUQAvD_BwE; _gac_UA-2546784-1=1.1643898163.CjwKCAiAl-6PBhBCEiwAc2GOVI8ysNNMNWcrs8vmdU18VQp0HTIMSt4Cru3RQl0dzCKprvL9FZM1VhoCdQUQAvD_BwE; _ym_isad=1; _gid=GA1.2.1495362433.1646568008; f=5.32e32548b6f3e9784b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36da6d7377b87edb337e7721a3e5d3cdbb46b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8fbcd99d4b9f4cbdabcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adecb8388123cde3fb76071f41cb5de44c02c730c0109b9fbb4b423595c3d740381e19da136a00bf0838f0f5e6e0d2832eb7781c1f2d375ec204a2981599a320d546b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acdffbbf3cc0bbfd9c570752c8d5b2a1842da10fb74cac1eab2da10fb74cac1eab25037f810d2d41a8134ecdeb26beb8b53778cee096b7b985bf37df0d1894b088; ft="HWH0vD5CIh7KbTQyY8ARZKwb8OIZRZ8ngBoN/ETLGgah3LJr+3LtlUMyBOWCqPfhIT/0uo87tgDZUSZP82UOmyPYvTYgx2o/aGjciVIoohg1/bpbKnX7ypB4Wt7PcVeJdGH28n9beWhyNIz11SKrH5MoS2Kx47uukZFYYNqX6q2hw0Hjx/jUFosGCj8mKAfw"; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISmViekx0M3c1Y1hoOEdiK01ueW1kR0VpamwrRVUrWTdzQ0d6ZnFJejlzNzZBTjIycGJSanFMV1J5RXdXRVk0OGhCdTRKTW5tRzZLbFJyVHdHTXJhaHEzT0g0TVF4WXI3UW9GcWNDejBaNjZod0dwWnZ5QVE0ZEtXS0RTNFZtOFlhRzBadUxvZEdhUGUxRUgwckx4cnJ1bEx0NHlxcEQwYlJJSE9kMHhtT05FVEtiTHpxaFNwMkxiTkN3SGZjZnpDWGZoYTVkMXB6NDB2bEpoZ0w4NVBZMmZ4WHB2MDBIZ1pqdzNjSmYrZWRoQjdrYmJEVlVCTTlQN1FVL3BoeUp2N1l5YkZQMk50Rmdnclgydk1iQnExcUQ4QXk1ZUpFOVNRdXREY21NREtFSksxcnpBK1VETlkva2V4N3BvckRFdTgrU1RIcGxjaHFYSFUycnhlMUxicWZnUEtybk9ZWGh2WTJzM04zRzJpUFBYWm9oVTM0TSt5V0NLelNlSEZwY0xOUk5YYWhNeThDNkNPZDljSC9oVkl6a3o2WVBWM1ZtYWNYQWcvUUlGdjBrd09wTlpkSDh4U2xJZHhlejh0MENsVkxTbXQ2WmNnbGtvUjFicEtXUWgzUStyVFlSYTgzcG5Wbitqd2crMGl4MDQ0bW5QbVQzeU9rSVVOZDJrcE9qa3pRUnRkUy8zOWZoRmx4U3VXbDJjVHpsd2pDVUdMdlZoUlJCTUQvSDh0K0h0bXlTUmVvTHpJN2JhTnZZY0RrM3VUc2lKb0hoMWVjKzlsUk5waG9pSlVya1g5aSsrUERxQnpqc3A0NUhNUlhkMmYreTlnbWx0MWxWRTBBM0RSZXR6MkpiVGFzSTlnT3ptQ0Foa3dzbGpudzl1OTBZR1h6azVTWXU0cXQrRVMySUxjYjIwZittdkNEMEdCUG5aaWJzU0UwOXkxY01BMjYwVFlzdmkzYm13RlhwZytQZldmYWp4RFlmWFYxRDNhWTBVQkZ4a1J6dEN0a2tHbjVmOEdqb3B4Q25tRy9MbXlYT0xpWkllVE90azRmVDVtdjN0bWtheVVFNU9DTllGNmF4aHRKU1J3bXJLU3BwMWswdmRBeFdDSU5BbUphdkdlcGdpVk0wZGpyRi81aUJaV2JTRDBEUElMSm02Z2ZoMDhhVU1JZkRXc3YwSHRoeVBSZ1pjRTJqODMwMy9sSkd2YnRvQjNrYjlwWjhjRVZOWVpqQ3p3SmR2RGN4NElyT21PMHdlbFZ0RmdIUnJ0WGVxSVdubE9GWmYycVlMaGZTUlJmcGpKVHFyaGowaS9aZ0pweTZ5RytnbmN4NFRZcjFCZTA5bjlISnJ0akNxRTdJeXpMMitob0svbWxpL2RqaUxQRWUwZWN4ZFZIRzBJUmZ6bjI4THNwUkNMM3JOaThpc2ErdkpDS3hFVkM3dmx3OW9ZZThWWWxaVWFFcE9URDBKSitDbDlYcDEwUEk2WmJtc205VVpxSTRuRnhyZThEcGx5UzBTdzhnUDNvZ0tFekp1NHEwcU9IUmQ4OD0iLCJpYXQiOjE2NDY1NjgwNDgsImV4cCI6MTY0Nzc3NzY0OH0.Lxp5FxDHTk2-Gbyy-XU1FC09m_iafzIZWnGpUaUYr0Q; luri=astrahan; buyer_location_id=623130; lastViewingTime=1646572053867; showedStoryIds=94-92-88-83-80-78-76-71-68; v=1646604024; abp=1; _ym_visorc=b; sx=H4sIAAAAAAAC%2F0zMQW7DIBAF0LvMOgsMw4fxbcIAbSKqGOG6ri3fvatKucA7CQA0B1SBeDCkhFSc5OCNashC80kbzdS4p0ff3LN9vZIZ%2FuPVNQ7%2FHP6%2BfS%2BgGxWaJzAgJrJcN4LYWjkZa7NAxbgkCfUeijOINei%2FLLrEalfef3%2FGoy%2FWaYttcJs%2B1yMf%2B5vsWaZ4XX8BAAD%2F%2F15x5mC1AAAA; _ga_9E363E7BES=GS1.1.1646604004.9.1.1646604428.55; _ga=GA1.1.2108703843.1643892382',
    'Host':'www.avito.ru',
    'Pragma':'no-cache',
    'Referer':'https://www.google.com/',
    'TE':'Trailers',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
url = "https://www.avito.ru/api/1/user/16e563a214f460550d6e8aa538a89336/extended-profile?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir"
# url = "https://www.avito.ru/"
# ---------------------- прямой запрос --------------------------------------
response = requests.get(url=url, 
                        
            
                        
                        
                        )

# ---------------------- вывод данных --------------------------------------
# вывод данных о статусе запроса
print(f'status_code={response.status_code}')
# сохранение в файл для разбора
with open('test_pars.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
