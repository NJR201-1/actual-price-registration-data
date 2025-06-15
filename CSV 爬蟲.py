#先保留 zipfile，應該有可以更輕鬆處理的做法，而不是下載的東西一個一個弄
import zipfile

import pandas as pd
import numpy as np
import os

#台中歷年資料 101-113直到6月初  (檔案中lvr_A 是土地買賣，B是租賃查詢，C是預售屋))，有些沒有資料，就沒有放
#檔名前面的字體 A:台北 B:台中 C:基隆 
#已登記日期為主，跟網站上的好像報的是不同日期 
#114_1 = 發布日期20250401 (登記日期 114年3月11日至 114年3月20日之買賣案件，及訂約日期 114年2月11日至 114年2月20日之租賃案件，及交易日期114年2月11日至 114年2月20日之預售屋案件
#114_2 = 發布日期20250411 (登記日期 114年3月21日至 114年3月31日之買賣案件，及訂約日期 114年2月21日至 114年2月28日之租賃案件，及交易日期114年2月21日至 114年2月28日之預售屋案件
#114_3 = 發布日期20250421 (登記日期 114年4月1日至 114年4月10日之買賣案件，及訂約日期 114年3月1日至 114年3月10日之租賃案件，及交易日期114年3月1日至 114年3月10日之預售屋案件
#114_4 = 發布日期20250501 (登記日期 114年4月11日至 114年4月20日之買賣案件，及訂約日期 114年3月11日至 114年3月20日之租賃案件，及交易日期114年3月11日至 114年3月20日之預售屋案件
#114_5 = 發布日期20250511 (登記日期 114年4月21日至 114年4月30日之買賣案件，及訂約日期 114年3月21日至 114年3月31日之租賃案件，及交易日期114年3月21日至 114年3月31日之預售屋案件
#114_6 = 發布日期20250521 (登記日期 114年5月1日至 114年5月10日之買賣案件，及訂約日期 114年4月1日至 114年4月10日之租賃案件，及交易日期114年4月1日至 114年4月10日之預售屋案件
#114_7 = [本期] 發布日期114年6月1日 (登記日期 114年5月11日至 114年5月20日之買賣案件，及訂約日期 114年4月11日至 114年4月20日之租賃案件，及交易日期114年4月11日至 114年4月20日之預售屋案件)

df_101c=pd.read_csv('台中csv/B_lvr_land_A/101_3.csv',low_memory=False)
# df_101d=pd.read_csv('台中csv/B_lvr_land_A/101_4.csv',low_memory=False)
# df_102a=pd.read_csv('台中csv/B_lvr_land_A/102_1.csv',low_memory=False)
# df_102b=pd.read_csv('台中csv/B_lvr_land_A/102_2.csv',low_memory=False)
# df_102c=pd.read_csv('台中csv/B_lvr_land_A/102_3.csv',low_memory=False)
# df_102d=pd.read_csv('台中csv/B_lvr_land_A/102_4.csv',low_memory=False)
# df_103a=pd.read_csv('台中csv/B_lvr_land_A/103_1.csv',low_memory=False)
# df_103b=pd.read_csv('台中csv/B_lvr_land_A/103_2.csv',low_memory=False)
# df_103c=pd.read_csv('台中csv/B_lvr_land_A/103_3.csv',low_memory=False)
# df_103d=pd.read_csv('台中csv/B_lvr_land_A/103_4.csv',low_memory=False)
# df_104a=pd.read_csv('台中csv/B_lvr_land_A/104_1.csv',low_memory=False)
# df_104b=pd.read_csv('台中csv/B_lvr_land_A/104_2.csv',low_memory=False)
# df_104c=pd.read_csv('台中csv/B_lvr_land_A/104_3.csv',low_memory=False)
# df_104d=pd.read_csv('台中csv/B_lvr_land_A/104_4.csv',low_memory=False)
# df_105a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/105_1.csv',low_memory=False)
# df_105b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/105_2.csv',low_memory=False)
# df_105c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/105_3.csv',low_memory=False)
# df_105d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/105_4.csv',low_memory=False)
# df_106a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/106_1.csv',low_memory=False)
# df_106b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/106_2.csv',low_memory=False)
# df_106c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/106_3.csv',low_memory=False)
# df_106d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/106_4.csv',low_memory=False)
# df_107a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/107_1.csv',low_memory=False)
# df_107b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/107_2.csv',low_memory=False)
# df_107c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/107_3.csv',low_memory=False)
# df_107d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/107_4.csv',low_memory=False)
# df_108a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/108_1.csv',low_memory=False)
# df_108b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/108_2.csv',low_memory=False)
# df_108c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/108_3.csv',low_memory=False)
# df_108d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/108_4.csv',low_memory=False)
# df_109a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/109_1.csv',low_memory=False)
# df_109b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/109_2.csv',low_memory=False)
# df_109c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/109_3.csv',low_memory=False)
# df_109d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/109_4.csv',low_memory=False)
# df_110a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/110_1.csv',low_memory=False)
# df_110b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/110_2.csv',low_memory=False)
# df_110c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/110_3.csv',low_memory=False)
# df_110d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/110_4.csv',low_memory=False)
# df_111a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/111_1.csv',low_memory=False)
# df_111b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/111_2.csv',low_memory=False)
# df_111c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/111_3.csv',low_memory=False)
# df_111d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/111_4.csv',low_memory=False)
# df_112a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/112_1.csv',low_memory=False)
# df_112b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/112_2.csv',low_memory=False)
# df_112c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/112_3.csv',low_memory=False)
# df_112d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/112_4.csv',low_memory=False)
# df_113a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/113_1.csv',low_memory=False)
# df_113b=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/113_2.csv',low_memory=False)
# df_113c=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/113_3.csv',low_memory=False)
# df_113d=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/113_4.csv',low_memory=False)
# df_114a=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_1.csv',low_memory=False)
# df_1141=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_a.csv',low_memory=False)
# df_1142=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_b.csv',low_memory=False)
# df_1143=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_c.csv',low_memory=False)
# df_1144=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_d.csv',low_memory=False)
# df_1145=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_e.csv',low_memory=False)
# df_1146=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_f.csv',low_memory=False)
# df_1147=pd.read_csv('C:/Users/Lenovo/Dropbox/我的電腦 (LAPTOP-Q9TLJPT7)/Desktop/Tibame DE 養成/房地產專案/台中csv/B_lvr_land_A/114_g.csv',low_memory=False)

# #2.刪除csv中第二列英文翻譯，The villages and towns urban district,transaction sign,land sector position building sector house number plate,land shifting total area square meter,....
# df_101c = df_101c.drop([0])
# df_101d = df_101d.drop([0])
# df_102a = df_102a.drop([0])
# df_102b = df_102b.drop([0])
# df_102c = df_102c.drop([0])
# df_102d = df_102d.drop([0])
# df_103a = df_102a.drop([0])
# df_103b = df_102a.drop([0])
# df_103c = df_102a.drop([0])
# df_103d = df_102a.drop([0])
# df_104a = df_102a.drop([0])
# df_104b = df_102a.drop([0])
# df_104c = df_102a.drop([0])
# df_104d = df_102a.drop([0])
# df_105a = df_102a.drop([0])
# df_105b = df_102a.drop([0])
# df_105c = df_102a.drop([0])
# df_105d = df_105d.drop([0])
# df_104a = df_102a.drop([0])
# df_104b = df_102a.drop([0])
# df_104c = df_102a.drop([0])
# df_104d = df_102a.drop([0])

