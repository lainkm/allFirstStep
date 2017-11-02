import requests

url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
r = requests.get(url)
r.raise_for_status()
print(r.status_code)