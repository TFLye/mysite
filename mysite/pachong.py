import requests
import time

def g():
    url = "https://s.wcd.im/ajax/flyerstatistics.jsp?cmd=flyerStat"

    t = int(time.time())
    payload = "&flyerAid=7979501&fid=102&statType=1&createTime={0}000".format(t)
    headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://s.wcd.im',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://s.wcd.im/v/7jgfdZ36/?qr=',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',

    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


if __name__ == "__main__":
    while 1:
        g()
        time.sleep(1)
