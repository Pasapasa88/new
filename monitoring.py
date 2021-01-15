import requests, json

def export_data():
    session = requests.Session()
    url2 = 'https://server.bioprom.ua:8090/device/list/detailed/'
    url = 'https://server.bioprom.ua:8090/common/social'
    session.headers['Authorization'] = 'Bearer8dd3430a-5457-44f1-9c51-bfac7b5e8feb'
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    response = session.post(url, verify= False)
    response_data = response.json()
    ff = session.get(url2, json=response_data, verify=False).content
    dd = json.loads(ff.decode('utf-8'))
    status = dd[0]['data']['data']['ACTUAL_STATE']
    ttg = dd[0]['data']['data']['OPTICAL_SENSOR_VALUE']
    online = dd[0]['isOnline']
    session.close()
    return status, ttg, online

