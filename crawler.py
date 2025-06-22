"""
# 實價登錄資料爬取程式

## 功能說明
此程式用於自動爬取台灣各城市及行政區的不動產實價登錄資料，並將資料以JSON格式儲存。

## 技術背景
考慮以下事實：
 - 實價登錄網站的 API 回傳的資訊較前端頁面擁有更多資訊－比如經緯度。
 - 實價登錄網站使用一加密機制、動態產生查詢網址與參數。

## 處理方法
我們採取以下作法因應、處理：
1. 採用 undetected_chromedriver 至實價登錄網站、藉由網站上前端腳本批次產生我們查詢所需的網址。
2. 將前一步驟網址交由 requests 模組發送 GET 請求，取得 API 回應資料，並儲存為檔案。

## 資料處理流程
1. 讀取城市與行政區配置檔案(cities.json)
2. 啟動 Chrome 瀏覽器並訪問實價登錄網站
3. 執行前端腳本產生查詢網址
4. 從瀏覽器性能日誌中擷取所需的 API 網址
5. 使用 requests 模組發送 GET 請求至每個 API 網址
6. 將獲取的資料儲存至對應的城市和行政區 JSON 檔案中

## 輸出資料
- 資料以 JSON 格式儲存
- 檔案依城市與行政區分類，儲存於 data/{城市名稱}/{行政區名稱}.json

## 相依套件
- datetime, time, json, os: 基本時間、檔案操作與資料處理函式庫
- selenium: 瀏覽器自動化測試框架
- undetected_chromedriver: 防止瀏覽器被偵測為自動化工具
- requests: HTTP 請求函式庫
"""
from datetime import datetime
import time
import json
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc
import requests

SECONDS_DELAY = 5 # 等待網頁載入的秒數
REQUEST_TIMEOUT = 60 # requests 的逾時時間
DIRECTORY = 'data'
PATH_CITIES_FILE = 'cities.json'  # 城市與行政區資料檔案
URL_INDEX = 'https://lvr.land.moi.gov.tw/jsp/list.jsp'

year = datetime.now().year - 1911  # 民國年
month = datetime.now().month

# 讀取城市與行政區資料
with open(PATH_CITIES_FILE, 'r', encoding='utf-8') as f:
    cities = json.load(f)

queries = [{'city': {'id': city.get('id'), 'name': city.get('name')}, 'town': {'id': district.get('id'), 'name': district.get('name')}, 'url': None} for city in cities for district in city['districts']]


# 查詢參數
params = {
    # 型態
    #  1. 房地
    #  2. 房地（車）
    #  3. 土地
    #  4. 建物
    #  5. 車位
    "ptype": "1,2,3,4,5",

    # 查詢起始年
    "starty": "101",

    # 查詢起始月
    "startm": "1",

    # 查詢結束年
    "endy": str(year),

    # 查詢結束月
    "endm": str(month),

    # 查詢類型
    # biz: 「買賣查詢」
    # rent: 「租賃查詢」
    # sale: 「預售屋查詢」
    "qryType": "biz",

    # 城市
    "city": "A", 

    # 行政區
    "town": "A15",

    # 社區名稱
    "p_build": "",

    # 「類型」－公寓、廠房...，僅限「租賃查詢」
    "ftype": "",

    # 租金總額－最低，僅限「租賃查詢」
    "price_s": "",

    # 租金總額－最高
    "price_e": "",

    # 最低單價
    "unit_price_s": "",

    # 最高單價
    "unit_price_e": "",
    
    # 最低面積
    "area_s": "",

    # 最高面積
    "area_e": "",

    "build_s": "",
    "build_e": "",

    # 最低屋齡
    "buildyear_s": "",

    # 最高屋齡
    "buildyear_e": "",

    "doorno": "",
    "pattern": "",
    "community": "",
    "floor": "",
    "rent_type": "",
    "rent_order": "",
    "urban": "",
    "urbantext": "",
    "nurban": "",
    "aa12": "",
    "p_purpose": "",
    "p_unusual_yn": "",
    "p_unusualcode": "",
    "QB41": "",
    "tmoney_unit": "1",

    # 單價單位
    # 1: 萬元
    # 2: 元
    "pmoney_unit": "1",

    # 面積單位
    # 1: 平方公尺
    # 2: 坪,
    "unit": "2"

    # token
    "token": ""
}

params_collection = [dict(params, city=query.get('city').get('id'), town=query.get('town').get('id')) for query in queries]

# ref: https://www.selenium.dev/selenium/docs/api/py/webdriver_chromium/selenium.webdriver.chromium.webdriver.html
# 啟用 Performance Log
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

options = uc.ChromeOptions()
# options.add_argument('--headless') # 可選
driver = uc.Chrome(headless=True,options=options, desired_capabilities=caps)
# 啟用 Network domain 並設定要阻擋的 URL
driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*SERVICE/QueryPrice*"]}) # 阻擋所有包含 /SERVICE/QueryPrice 的 URL

# 開啟實價登錄網站
driver.get(URL_INDEX)
# wait for the page to load
time.sleep(SECONDS_DELAY)

# 執行前端腳本，批次產生查詢網址
script = """
    var params_collection = """ + str(params_collection) + """;
    for (let params of params_collection) {
        window.common.loadQueryPrice2(params);
    }
"""
driver.execute_script(script)

# 自 Network Log 中擷取查詢網址
i = 0
log_entries = driver.get_log("performance")
for entry in log_entries:
    log = entry['message']
    logJson = json.loads(log)
    print(logJson)
    if logJson['message']['method'] == 'Network.requestWillBeSent':
        url = logJson['message']['params']['request']['url']
        if '/SERVICE/QueryPrice' in url:
            queries[i]['url'] = url
            i += 1

driver.quit()
print("queries: ", queries, len(queries))

# 透過 requests 模組發送 GET 請求，並儲存資料
for query in queries:
    CITY_NAME = f"{query['city'].get('name')}"
    DISTRICT_NAME = f"{query['town'].get('name')}"
    dir_path = os.path.join(DIRECTORY, CITY_NAME)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, f'{DISTRICT_NAME}.json')
    
    if os.path.exists(file_path):
        print(f"File already exists for {CITY_NAME} {DISTRICT_NAME}, skipping...")
        continue

    print(f"Query for {query['town']['name']} at URL: {query['url']}")

    try:
        response = requests.get(query['url'], timeout=REQUEST_TIMEOUT)
    except Exception as e:
        print(f"Error fetching data for {CITY_NAME} {DISTRICT_NAME} at URL: {query['url']}, Error: {e}")
        continue


    if response.status_code == 200:
        open(file_path, 'w', encoding='utf-8').write(response.text)
    else:
        raise Exception(f"Failed to fetch data for {DISTRICT_NAME} at URL: {query['url']}, status code: {response.status_code}")

    time.sleep(SECONDS_DELAY)