import json
import random
import re
import requests
import pprint
import requests
import time
import pandas as pd
import smtplib  # SMTP 사용을 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
from email.mime.application import MIMEApplication
import datetime
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
import os
import math
import datetime
import pymysql


import difflib

def find_brand_style_id(data):
    if isinstance(data, list):
        for item in data:
            result = find_brand_style_id(item)
            if result is not None:
                return result
    elif isinstance(data, dict):
        if "brandStyleId" in data:
            return data["brandStyleId"]
        for key, value in data.items():
            result = find_brand_style_id(value)
            if result is not None:
                return result
    return None

def compare(A,B):
    # 두 문자열 A와 B를 정의합니다.
    # A = "A08FW735-BLACK"
    # B = "A08FW735"

    # 두 문자열 간의 차이를 계산합니다.
    differ = difflib.Differ()
    differences = list(differ.compare(A, B))

    # 차이를 기반으로 유사도를 계산합니다.
    # 차이가 적을수록 유사도가 높다고 가정합니다.
    similarity = 1 - (len([d for d in differences if d[0] != ' ']) / max(len(A), len(B)))
    print("유사도:", similarity)
    return similarity



def find_dicts_with_key(data, key):
    if isinstance(data, dict):
        if key in data:
            yield data
        for value in data.values():
            yield from find_dicts_with_key(value, key)
    elif isinstance(data, list):
        for item in data:
            yield from find_dicts_with_key(item, key)

def GetPrice(resultElem):
    cookies = {
        'BIcookieID': 'c60834c2-f7f4-496f-8489-59d38ae8b2a2',
        'ckm-ctx-sf': '%2Fkr',
        'ffcp': 'a.1.0_f.1.0_p.1.0_c.1.0',
        'ub': '50CAC614848E6A27CBC86CA9829B46A4',
        'checkoutType2': '4',
        'session-1': '1d857b14-251c-a990-5d26-a9a722e39fbc',
        '_gcl_au': '1.1.1214513334.1697718438',
        '_cs_c': '0',
        'rskxRunCookie': '0',
        'rCookie': 'h2dnap67k8559xxaw7lelglnx5q2xg',
        'FPID': 'FPID2.3.cyi3LmVHaBGhOCm%2FzeGzoHitfSCxJJfuhl8Km%2F7tXZw%3D.1697718438',
        'FPAU': '1.1.1214513334.1697718438',
        'fita.sid.farfetch': 'wYKdEalgrFvLLfNHxsA46IaFCJRYc9H6',
        '__gads': 'ID=9960b2fb34665e90:T=1697761589:RT=1697761589:S=ALNI_MawjjQ8IAnky1XHea5e5wpDuWE-Ag',
        '__gpi': 'UID=00000c6934cff480:T=1697761589:RT=1697761589:S=ALNI_MbHBE_SWzQGe8iP6vOz6bQ0QwtfPA',
        '_gid': 'GA1.2.174695207.1698045856',
        'g_state': '{"i_p":1698132282329,"i_l":2}',
        'BISessionId': '3e703fd1-32e6-74f0-c3fc-dd017482b235',
        'ff_navroot_history': '141259',
        'ABProduct': '',
        'ABListing': '',
        'ABGeneral': '',
        'ABLanding': '',
        'ABCheckout': '',
        'ABRecommendations': '',
        'ABReturns': '',
        'ABWishlist': '',
        '__Host-CSRF-TOKEN': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T7NNGoJavWqcF45p6AkohVvVkwSVvZf3UfgDqtYavLMWK47X42m50q0v8mbaszcYdiV3PS2IyC64PFVyB1ebkWNmBV5YkvtNq9mVai77tZ9ww-zQtZQeuL-ApIF_dPKGdI',
        '__Host-FF.AppSession': 'CfDJ8BZV7bSK%2FgVKoJ5%2FtFR15T6BykTflz7yVR0gbR1s5yty%2BAexanhvHBrOmrzXgFfnWadMv5C36%2BrAG51PCNI4MFkY4Gh8ly%2FNEItuhmwVGrftHBUYmAyHHAa%2BMn0Lom1572hkvzskCVZyx%2FLRl5BWfMHrf9gJkIYPxVESShATHvPQ',
        'AkamaiFeatureToggle': '02a57c.1_0357f7.1_04154b.1_0a3efc.1_1d8e03.1_20b92f.1_20f499.-1_247006.-1_26ddb8.1_286534.1_2ba087.1_361eee.0_3aa8d2.0_4247d8.-210644093_425ded.1_45dc7d.1_48259b.1_4d76c8.2_56f7db.-1_5836e0.-1_590a92.1_5a000f.1_5a745a.-1_5dbd1a.1_5edc51.-1959550240_613a9b.-416292886_64d19c.1_67486d.-1_678f94.0_687752.-1_6f0973.1103883728_729a35.1_751ef1.-1_8c3210.-1_8c4007.-1_931982.1_945679.1_999fce.2_9a710c.1_9ebcf7.1_9f0eda.-1_a00510.1148090917_a54601.1_ac992b.1_ae134f.1_ae71cc.-1531679491_b45ee1.1_b833c7.535845473_b8833c.1_b8e9db.0_b90715.0_bf110c.-1_c06844.-1_c0ba66.-900375819_c2155c.1_cfc1ba.1_d052f2.909416419_d26d24.1_d47781.-1_d59758.1_da4cdf.1_dab09d.632075632_db79f1.2_dd19ed.1_deb641.-1_dec9f3.1_df039e.-1_df93a0.1_e7eec4.1_e89c2a.2_ed07fa.0_ed8d9e.1_f220ef.4_f3db94.1_f5969a.1_f8c66b.1_fb2b96.1_fbf4d6.1_fdbb7a.0_fdd39e.-1',
        'ExperimentsGeneral': 'b6cf98.3',
        '_abck': 'C08A897D9AF9F29B3E5979384D798B0F~0~YAAQLGHKF5/OKWCLAQAAVUcxYAqMEbVsuLZKv1Wbjl2GE2zdPmnIM9JepicoIALGTGt5kFjzNvAIux3sffVtmtGzGmij5PXeYDb081q9GNMtgJQeNfkGBuy088vz/c9aZ5MSf7jxx659cLK4ozoMZE8gFnNzsIiiwHziKHYJroMYun60KWp2ew1Z5Xs4j2UNb2w8idXGCtke8oA4Sc+DguOzzqvz1s9Nghswq1IpsMFOhQNYkePK9bUTo5fupDhE+olsYHiJ4hu/dhGOiG1L/kQz6doGVB71dJJv5L7F3a92VbLJw0NOZJ3Y2npQqXeyMJCko09soJ2NxHokgJtCNJHDpnBU4gqGP/xbQlyQtKogX31tBMdB8VIJUpjxoxXYKNnJPVeHYojMjtMuIM1eMMH3X96kW4/qzug=~-1~-1~-1',
        'bm_sz': '5B5BC83341B4FF5E5C6380BBEED519FC~YAAQLGHKF6LOKWCLAQAAVUcxYBW+XQMWWNy4V88P72Y71OqNN8T2Hla6t1xl2Qze+0OAS49ciUMX8YlppSrlrPxhoPsHUbaHUP1V3goY/EDqHhgz0tcAQS6DwSlocS4fMXvw5SK+q3TlzmQ/M2XowJmSImhsd+0W+ptHIi7W1Xp4mfEVlhPR3UA7/vOo7bZ/05/gXTrqd6mv/DGJ83/wreGmIPSIJ0ZI5NURff8/y/AlhZNMYq6qZ/Z2GIPcm2vXc0YYBZ8C3CuCwJ+sC7gpBaUGLbOz7v05lpjNRY6EqKyEO9XnpQ==~3556149~3753537',
        'ff_newsletter_pv': '1',
        '__cuid': '85e78c95cc654bf0bb909ec05fd16a64',
        '_cs_mk': '0.9064752943577206_1698125927575',
        '_cs_id': '2627bd8a-bf78-a342-9776-ddabfae3a2c9.1697718437.5.1698125927.1698125927.1.1731882437842',
        '_cs_s': '1.0.0.1698127727833',
        '_ga': 'GA1.1.663371548.1697718438',
        '_uetsid': '2c2d1090717511ee989c156eb33b67c9',
        '_uetvid': 'd79975106e7a11eeaf1c895a21f2d376',
        'cto_bundle': 'At1DgF8yMExsUTlvNWNoZlhkJTJCVmpISGt4WXo5UmRvc2Rzc0ZLMzFJSkNpOW1SVnAyZFQwN0tHWHVqbTA5Z3FXOFElMkJFdUtnd2tRYjFEWXFkc3lvMEVGV1duN0o2NTNZd2h6MEl4ZmhPdllWb3drd01EdzlwRGdBYW9adVhDcEhkOHdPVDZ6T3BuJTJGa2ZxUE9IT3g3QU80QnZqVEg2WEhQWkJQeXNrdkY1RWZYZWtiNzAlM0Q',
        'FPLC': 'wMx1%2F9iZz1hSmFgooF7t%2BU6Yy84ZfDnWwL2OBUe%2FKZsMaaxthHNQHsYO2zzmMRQduhUmA9CU3tED4wTK09CNw8bIha%2BlLjbdrpoBtqN8oJKBnIakw7TFDVwtXlSN%2Bg%3D%3D',
        'ftr_blst_1h': '1698125928353',
        'lastRskxRun': '1698125928581',
        'forterToken': '7be195e88478413faf6966cf8dbe11d8_1698125927519__UDF43-m4_11ck_',
        'bm_mi': 'F686E5C46A23EE416FE9F7A5ED7E57F0~YAAQLGHKF/pyKmCLAQAAgugyYBVs27SU69yhKxbwciaddZ6Qmo8owKVkUABcCEJN12ovDdyqds8pZ8ra6YQM/YS18vgS22qBGKm/2hHjBsg0mSS0iEEFdeKcls1PDUOq7ir8aBHNgI9+GGZuyCA1ZpXTfRo8toR3zZM/EskYAdrrRslVz0culqE8fw+w8Yf1jXwmNx7+hOvDqKgG57JVCSsY79VBP8DrME6vObuEDZ/1XrDMndN3h6xvNfSeS/gvXsDjcMmKH7Fw8VuomvRllCm8t37+s1kGrGCuyq15pfpDNvCulY56Vlh8M1AHL82krP/cEaFX9gp4AZKswDzZVrVxj4Gm4w0c+3mogvL8V6weYHPr7REYNg+R1A==~1',
        'bm_sv': 'A923FC09DA3D5D4636EAB47046F34085~YAAQLGHKF/tyKmCLAQAAgugyYBW2Y48pMe8mB1fWP2SkTFxgwNNrVBUpg0MLVJusE8rbZOLdsivTohQ4U1tsRb3QnbUk1YXUR9FRHeJqTP6eEHvNrgCl8w6oZ8K6as/3xCOAxFpXWo0a4jmT1hKyAVc9I/+UaTe7WMW+aD56VvIwJIxt1mjMiVWy4GYIbiX9h+quNoLES+Fyq7qF+yUDNmkMicFQ6ntcCzW4FVd4MNylQ1vxEbgHGmvbsqUsLoIpKrY=~1',
        '_ga_CEF7PMN9HX': 'GS1.1.1698125927.5.1.1698126031.60.0.0',
        '_ga_HLS8C90D41': 'GS1.1.1698125927.5.1.1698126031.0.0.0',
        'ak_bmsc': '9D16AB3F4845D9028AD25994D87579D4~000000000000000000000000000000~YAAQLGHKFyJzKmCLAQAA6egyYBU4FISGYm7L2Y1SBXsR7wzvhVoAM27ISYZlrYPIZyA8+WAeZWdQSTFzjBbApAUqmO37qNjEugTQl2YOh+SArySAxdfpQv++uDR0xPKxeCvw/2untIjtxlHHlUEtd+Y+5C4VuGIs20wd7le+GDx4kwmwf9PR5E2w/nP8TznYz8680lniE3MT7YDt9vWLeoDBTPbOf8asDDDVcPFOEVmj1EGjupGpYhqar+kKqLhU6BmWbZ+0ygAHjkbNEzZV9U9B+V2gEcsKHJ+jlpmY7jJ9uVI+6j3tcXr/Gr/iKAr/8pq52AAQFFTfNGPMp6NDlrD4ARc0LmwEma1eh6/j+PtgBLzVStMWk89oaBhQP2t3nx479nA1yH5x1mAWOT1YlBQhojZiRDAyHe0VfAAYeVoGVjtAroIRbJtMsFc5Qtp1C/t7p+Td5U0NJvkYp4Vp03Wa8jcUMrxUWanY8NSIBl6iW0QpROBm7gsRh9E+QKCvEt8ssoI3C0rgyCJbXIsmo+1h+VBWsKg9nHouxF/sgTetxBDfVtUyxR/os1+JQnTdFk31LVQw',
        'RT': '"z=1&dm=www.farfetch.com&si=53e936ca-303c-4db2-a7a5-7338426bc4c8&ss=lo3wbw5u&sl=1&tt=3bl&rl=1"',
        '__Host-CSRF-REQUEST-TOKEN': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T491wPTevNT0mBFfUUP5q7c5L-4IunNmwUwRsXYEbFmpD_nklNaCLZDd2W4RtPNs_PrcYKT4w-_ZArv6oYf5iwsts0WuWIoYkLlGKlDbqerDTPhtd2gIMc-289l1M8uzU_aAq95qFQlASyCT8LQqoq9FqLAv6Y0YXVDRBiXdSSxEA',
        '__Host-FF.AppCookie': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T68KbkWzfTthS7_-Led2BFmvKALdY6HyMhTdThs1lNB3EXKW9mzw9uAsVBE2CqSeh-jLEV_btgI2n9UzQtSbNoPIfToybMc8I8mokw7XPIcHpd8mRfg15L3sSfv1LZthcLx9Kn71SpcB5I7rLJ92JZZsU8cQT_pj5julfbNNmvpC--NB-bWYXkb8NsFr5gthyCXn6rjYL4u05vEe755q8k-E0SYW6jT3dHRQE37hxmmGJLbdYHXL_8AfEUx4inyi394WzMfZZom9yxAqi5Eec6x',
    }

    headers = {
        'authority': 'www.farfetch.com',
        'accept': '*/*',
        'accept-language': 'ko-KR',
        'content-type': 'application/json',
        # 'cookie': 'BIcookieID=c60834c2-f7f4-496f-8489-59d38ae8b2a2; ckm-ctx-sf=%2Fkr; ffcp=a.1.0_f.1.0_p.1.0_c.1.0; ub=50CAC614848E6A27CBC86CA9829B46A4; checkoutType2=4; session-1=1d857b14-251c-a990-5d26-a9a722e39fbc; _gcl_au=1.1.1214513334.1697718438; _cs_c=0; rskxRunCookie=0; rCookie=h2dnap67k8559xxaw7lelglnx5q2xg; FPID=FPID2.3.cyi3LmVHaBGhOCm%2FzeGzoHitfSCxJJfuhl8Km%2F7tXZw%3D.1697718438; FPAU=1.1.1214513334.1697718438; fita.sid.farfetch=wYKdEalgrFvLLfNHxsA46IaFCJRYc9H6; __gads=ID=9960b2fb34665e90:T=1697761589:RT=1697761589:S=ALNI_MawjjQ8IAnky1XHea5e5wpDuWE-Ag; __gpi=UID=00000c6934cff480:T=1697761589:RT=1697761589:S=ALNI_MbHBE_SWzQGe8iP6vOz6bQ0QwtfPA; _gid=GA1.2.174695207.1698045856; g_state={"i_p":1698132282329,"i_l":2}; BISessionId=3e703fd1-32e6-74f0-c3fc-dd017482b235; ff_navroot_history=141259; ABProduct=; ABListing=; ABGeneral=; ABLanding=; ABCheckout=; ABRecommendations=; ABReturns=; ABWishlist=; __Host-CSRF-TOKEN=CfDJ8BZV7bSK_gVKoJ5_tFR15T7NNGoJavWqcF45p6AkohVvVkwSVvZf3UfgDqtYavLMWK47X42m50q0v8mbaszcYdiV3PS2IyC64PFVyB1ebkWNmBV5YkvtNq9mVai77tZ9ww-zQtZQeuL-ApIF_dPKGdI; __Host-FF.AppSession=CfDJ8BZV7bSK%2FgVKoJ5%2FtFR15T6BykTflz7yVR0gbR1s5yty%2BAexanhvHBrOmrzXgFfnWadMv5C36%2BrAG51PCNI4MFkY4Gh8ly%2FNEItuhmwVGrftHBUYmAyHHAa%2BMn0Lom1572hkvzskCVZyx%2FLRl5BWfMHrf9gJkIYPxVESShATHvPQ; AkamaiFeatureToggle=02a57c.1_0357f7.1_04154b.1_0a3efc.1_1d8e03.1_20b92f.1_20f499.-1_247006.-1_26ddb8.1_286534.1_2ba087.1_361eee.0_3aa8d2.0_4247d8.-210644093_425ded.1_45dc7d.1_48259b.1_4d76c8.2_56f7db.-1_5836e0.-1_590a92.1_5a000f.1_5a745a.-1_5dbd1a.1_5edc51.-1959550240_613a9b.-416292886_64d19c.1_67486d.-1_678f94.0_687752.-1_6f0973.1103883728_729a35.1_751ef1.-1_8c3210.-1_8c4007.-1_931982.1_945679.1_999fce.2_9a710c.1_9ebcf7.1_9f0eda.-1_a00510.1148090917_a54601.1_ac992b.1_ae134f.1_ae71cc.-1531679491_b45ee1.1_b833c7.535845473_b8833c.1_b8e9db.0_b90715.0_bf110c.-1_c06844.-1_c0ba66.-900375819_c2155c.1_cfc1ba.1_d052f2.909416419_d26d24.1_d47781.-1_d59758.1_da4cdf.1_dab09d.632075632_db79f1.2_dd19ed.1_deb641.-1_dec9f3.1_df039e.-1_df93a0.1_e7eec4.1_e89c2a.2_ed07fa.0_ed8d9e.1_f220ef.4_f3db94.1_f5969a.1_f8c66b.1_fb2b96.1_fbf4d6.1_fdbb7a.0_fdd39e.-1; ExperimentsGeneral=b6cf98.3; _abck=C08A897D9AF9F29B3E5979384D798B0F~0~YAAQLGHKF5/OKWCLAQAAVUcxYAqMEbVsuLZKv1Wbjl2GE2zdPmnIM9JepicoIALGTGt5kFjzNvAIux3sffVtmtGzGmij5PXeYDb081q9GNMtgJQeNfkGBuy088vz/c9aZ5MSf7jxx659cLK4ozoMZE8gFnNzsIiiwHziKHYJroMYun60KWp2ew1Z5Xs4j2UNb2w8idXGCtke8oA4Sc+DguOzzqvz1s9Nghswq1IpsMFOhQNYkePK9bUTo5fupDhE+olsYHiJ4hu/dhGOiG1L/kQz6doGVB71dJJv5L7F3a92VbLJw0NOZJ3Y2npQqXeyMJCko09soJ2NxHokgJtCNJHDpnBU4gqGP/xbQlyQtKogX31tBMdB8VIJUpjxoxXYKNnJPVeHYojMjtMuIM1eMMH3X96kW4/qzug=~-1~-1~-1; bm_sz=5B5BC83341B4FF5E5C6380BBEED519FC~YAAQLGHKF6LOKWCLAQAAVUcxYBW+XQMWWNy4V88P72Y71OqNN8T2Hla6t1xl2Qze+0OAS49ciUMX8YlppSrlrPxhoPsHUbaHUP1V3goY/EDqHhgz0tcAQS6DwSlocS4fMXvw5SK+q3TlzmQ/M2XowJmSImhsd+0W+ptHIi7W1Xp4mfEVlhPR3UA7/vOo7bZ/05/gXTrqd6mv/DGJ83/wreGmIPSIJ0ZI5NURff8/y/AlhZNMYq6qZ/Z2GIPcm2vXc0YYBZ8C3CuCwJ+sC7gpBaUGLbOz7v05lpjNRY6EqKyEO9XnpQ==~3556149~3753537; ff_newsletter_pv=1; __cuid=85e78c95cc654bf0bb909ec05fd16a64; _cs_mk=0.9064752943577206_1698125927575; _cs_id=2627bd8a-bf78-a342-9776-ddabfae3a2c9.1697718437.5.1698125927.1698125927.1.1731882437842; _cs_s=1.0.0.1698127727833; _ga=GA1.1.663371548.1697718438; _uetsid=2c2d1090717511ee989c156eb33b67c9; _uetvid=d79975106e7a11eeaf1c895a21f2d376; cto_bundle=At1DgF8yMExsUTlvNWNoZlhkJTJCVmpISGt4WXo5UmRvc2Rzc0ZLMzFJSkNpOW1SVnAyZFQwN0tHWHVqbTA5Z3FXOFElMkJFdUtnd2tRYjFEWXFkc3lvMEVGV1duN0o2NTNZd2h6MEl4ZmhPdllWb3drd01EdzlwRGdBYW9adVhDcEhkOHdPVDZ6T3BuJTJGa2ZxUE9IT3g3QU80QnZqVEg2WEhQWkJQeXNrdkY1RWZYZWtiNzAlM0Q; FPLC=wMx1%2F9iZz1hSmFgooF7t%2BU6Yy84ZfDnWwL2OBUe%2FKZsMaaxthHNQHsYO2zzmMRQduhUmA9CU3tED4wTK09CNw8bIha%2BlLjbdrpoBtqN8oJKBnIakw7TFDVwtXlSN%2Bg%3D%3D; ftr_blst_1h=1698125928353; lastRskxRun=1698125928581; forterToken=7be195e88478413faf6966cf8dbe11d8_1698125927519__UDF43-m4_11ck_; bm_mi=F686E5C46A23EE416FE9F7A5ED7E57F0~YAAQLGHKF/pyKmCLAQAAgugyYBVs27SU69yhKxbwciaddZ6Qmo8owKVkUABcCEJN12ovDdyqds8pZ8ra6YQM/YS18vgS22qBGKm/2hHjBsg0mSS0iEEFdeKcls1PDUOq7ir8aBHNgI9+GGZuyCA1ZpXTfRo8toR3zZM/EskYAdrrRslVz0culqE8fw+w8Yf1jXwmNx7+hOvDqKgG57JVCSsY79VBP8DrME6vObuEDZ/1XrDMndN3h6xvNfSeS/gvXsDjcMmKH7Fw8VuomvRllCm8t37+s1kGrGCuyq15pfpDNvCulY56Vlh8M1AHL82krP/cEaFX9gp4AZKswDzZVrVxj4Gm4w0c+3mogvL8V6weYHPr7REYNg+R1A==~1; bm_sv=A923FC09DA3D5D4636EAB47046F34085~YAAQLGHKF/tyKmCLAQAAgugyYBW2Y48pMe8mB1fWP2SkTFxgwNNrVBUpg0MLVJusE8rbZOLdsivTohQ4U1tsRb3QnbUk1YXUR9FRHeJqTP6eEHvNrgCl8w6oZ8K6as/3xCOAxFpXWo0a4jmT1hKyAVc9I/+UaTe7WMW+aD56VvIwJIxt1mjMiVWy4GYIbiX9h+quNoLES+Fyq7qF+yUDNmkMicFQ6ntcCzW4FVd4MNylQ1vxEbgHGmvbsqUsLoIpKrY=~1; _ga_CEF7PMN9HX=GS1.1.1698125927.5.1.1698126031.60.0.0; _ga_HLS8C90D41=GS1.1.1698125927.5.1.1698126031.0.0.0; ak_bmsc=9D16AB3F4845D9028AD25994D87579D4~000000000000000000000000000000~YAAQLGHKFyJzKmCLAQAA6egyYBU4FISGYm7L2Y1SBXsR7wzvhVoAM27ISYZlrYPIZyA8+WAeZWdQSTFzjBbApAUqmO37qNjEugTQl2YOh+SArySAxdfpQv++uDR0xPKxeCvw/2untIjtxlHHlUEtd+Y+5C4VuGIs20wd7le+GDx4kwmwf9PR5E2w/nP8TznYz8680lniE3MT7YDt9vWLeoDBTPbOf8asDDDVcPFOEVmj1EGjupGpYhqar+kKqLhU6BmWbZ+0ygAHjkbNEzZV9U9B+V2gEcsKHJ+jlpmY7jJ9uVI+6j3tcXr/Gr/iKAr/8pq52AAQFFTfNGPMp6NDlrD4ARc0LmwEma1eh6/j+PtgBLzVStMWk89oaBhQP2t3nx479nA1yH5x1mAWOT1YlBQhojZiRDAyHe0VfAAYeVoGVjtAroIRbJtMsFc5Qtp1C/t7p+Td5U0NJvkYp4Vp03Wa8jcUMrxUWanY8NSIBl6iW0QpROBm7gsRh9E+QKCvEt8ssoI3C0rgyCJbXIsmo+1h+VBWsKg9nHouxF/sgTetxBDfVtUyxR/os1+JQnTdFk31LVQw; RT="z=1&dm=www.farfetch.com&si=53e936ca-303c-4db2-a7a5-7338426bc4c8&ss=lo3wbw5u&sl=1&tt=3bl&rl=1"; __Host-CSRF-REQUEST-TOKEN=CfDJ8BZV7bSK_gVKoJ5_tFR15T491wPTevNT0mBFfUUP5q7c5L-4IunNmwUwRsXYEbFmpD_nklNaCLZDd2W4RtPNs_PrcYKT4w-_ZArv6oYf5iwsts0WuWIoYkLlGKlDbqerDTPhtd2gIMc-289l1M8uzU_aAq95qFQlASyCT8LQqoq9FqLAv6Y0YXVDRBiXdSSxEA; __Host-FF.AppCookie=CfDJ8BZV7bSK_gVKoJ5_tFR15T68KbkWzfTthS7_-Led2BFmvKALdY6HyMhTdThs1lNB3EXKW9mzw9uAsVBE2CqSeh-jLEV_btgI2n9UzQtSbNoPIfToybMc8I8mokw7XPIcHpd8mRfg15L3sSfv1LZthcLx9Kn71SpcB5I7rLJ92JZZsU8cQT_pj5julfbNNmvpC--NB-bWYXkb8NsFr5gthyCXn6rjYL4u05vEe755q8k-E0SYW6jT3dHRQE37hxmmGJLbdYHXL_8AfEUx4inyi394WzMfZZom9yxAqi5Eec6x',
        'origin': 'https://www.farfetch.com',
        'referer': 'https://www.farfetch.com/kr/shopping/men/asics-14-item-20767916.aspx',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.89", "Google Chrome";v="118.0.5993.89", "Not=A?Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-client-flow': 'async',
        'x-ff-gql-c': 'true',
        'x-subfolder': '/kr',
    }

    productId=resultElem['url'].split("-")[-1].replace(".aspx","")
    regex=re.compile('\d+')
    productId=regex.findall(productId)[0]
    print("productId:",productId)
    print("url:",resultElem['url'])

    json_data = {
        'operationName': 'SizeAndFitData',
        'variables': {
            # 'productId': '20767916',
            'productId': productId,
        },
        'query': 'query SizeAndFitData($productId: ID!, $merchantId: ID) {\n  user {\n    id\n    preference {\n      unitSystem\n      __typename\n    }\n    __typename\n  }\n  product(id: $productId, merchantId: $merchantId) {\n    ... on Product {\n      id\n      scale {\n        id\n        abbreviation\n        isOneSize\n        __typename\n      }\n      variations {\n        edges {\n          node {\n            ... on Variation {\n              id\n              price {\n                value {\n                  raw\n                  formatted\n                  __typename\n                }\n                __typename\n              }\n              images {\n                order\n                size1000 {\n                  url\n                  alt\n                  __typename\n                }\n                modelVariationSize\n                modelMeasurement {\n                  height {\n                    type\n                    name\n                    imperial {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    metric {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    __typename\n                  }\n                  bodyMeasurements {\n                    type\n                    name\n                    imperial {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    metric {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    __typename\n                  }\n                  __typename\n                }\n                __typename\n              }\n              fitting {\n                type\n                description\n                __typename\n              }\n              measurements {\n                type\n                name\n                imperial {\n                  raw\n                  formatted\n                  __typename\n                }\n                metric {\n                  raw\n                  formatted\n                  __typename\n                }\n                __typename\n              }\n              variationProperties {\n                ... on ScaledSizeVariationProperty {\n                  order\n                  values {\n                    id\n                    order\n                    description\n                    scale {\n                      id\n                      __typename\n                    }\n                    __typename\n                  }\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            ... on VariationUnavailable {\n              product {\n                id\n                __typename\n              }\n              images {\n                order\n                size1000 {\n                  url\n                  alt\n                  __typename\n                }\n                modelVariationSize\n                modelMeasurement {\n                  height {\n                    type\n                    name\n                    imperial {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    metric {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    __typename\n                  }\n                  bodyMeasurements {\n                    type\n                    name\n                    imperial {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    metric {\n                      raw\n                      formatted\n                      __typename\n                    }\n                    __typename\n                  }\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://www.farfetch.com/kr/experience-gateway', cookies=cookies, headers=headers, json=json_data)
    # pprint.pprint(json.loads(response.text))
    results=json.loads(response.text)['data']['product']['variations']['edges']
    # pprint.pprint(results)

    try:
        dataList=[]
        for result in results:
            pprint.pprint(result)
            price=result['node']['price']['value']['raw']
            name=result['node']['images'][0]['size1000']['alt']
            size=result['node']['variationProperties'][0]['values'][0]['description']
            order=result['node']['variationProperties'][0]['order']
            data={'size':size,'price':price,'name':name,'order':order}
            pprint.pprint(data)
            dataList.append(data)
            print("========================")
    except:
        print("페이지 문제 있음")
        return []

    resultList = []
    #============계산하기
    checkList=resultElem['price']
    for checkElem in checkList:
        # print("checkElem:",checkElem,"/ checkElem_TYPE:",type(checkElem),len(checkElem))

        for index,dataElem in enumerate(dataList):
            if str(checkElem[0]) ==dataElem['size']:
                print("일치사이즈:",dataElem['size'])
                currentPrice=dataElem['price']
                targetPrice=checkElem[1]
                if currentPrice<=targetPrice:
                    print("==========================")
                    print("name:",name)
                    print('size:',dataElem['size'])
                    print("currentPrice:",currentPrice,'targetPrice:',targetPrice)
                    print("찾았다!",resultElem['url'])
                    data=[name,dataElem['size'],currentPrice,resultElem['url']]
                    resultList.append(data)
                    print("==========================")
                    break
                else:
                    break

    return resultList

def GetExcel(fname):
    df=pd.read_excel(fname)
    df=df.values.tolist()
    # pprint.pprint(df)

    result_list = []  # 결과를 저장할 리스트 초기화

    # 중복을 체크할 딕셔너리 초기화
    seen_urls = {}

    for item in df:
        url = item[1]  # 두 번째 요소를 URL로 사용
        if url not in seen_urls:
            seen_urls[url] = []  # URL을 처음 보는 경우 빈 리스트를 초기화
        seen_urls[url].append([item[2], item[3]])  # 3번째와 4번째 요소를 리스트로 묶어서 추가

    # 딕셔너리를 리스트 형태로 변환하여 결과 리스트에 추가
    for url, price_list in seen_urls.items():
        result = {'url': url, 'price': price_list}
        result_list.append(result)

    # pprint.pprint(result_list)
    return result_list

def SendMail(checkResultList,email):
    smtp_server = 'smtp.naver.com'
    smtp_port = 587

    # 네이버 이메일 계정 정보
    username = 'wsgt18@naver.com'  # 클라이언트 정보 입력
    password = 'dnrglvotl0*'  # 클라이언트 정보 입력

    receiver=email
    # username = 'hellfir2@naver.com'  # 클라이언트 정보 입력
    # password = 'dlwndwo1!'  # 클라이언트 정보 입력
    # =================커스터마이징
    try:
        to_mail = receiver
    except:
        print("메일주소없음")
        return

    # =================

    # 메일 수신자 정보
    to_email = receiver

    # 참조자 정보
    cc_email = 'ljj3347@naver.com'

    # 메일 본문 및 제목 설정

    # content = '''
    # <html>
    #     <body>
    #     <p>반갑습니다~~</p>
    #
    #     </body>
    # </html>
    # '''
    contentList=[]
    # items=[
    #     {'name':'모자','size':'M','price':'10000','url':'https://www.naver.com'},
    #     {'name': '신발', 'size': '250', 'price': '20000','url':'https://www.naver.com'},
    #     {'name': '하의', 'size': 'L', 'price': '30000','url':'https://www.naver.com'}
    # ]
    for index,checkResult in enumerate(checkResultList):
        data='{}. 이름 : {} / 사이즈 : {} / 가격 : {} / 주소 : {}'.format(index+1,checkResult[0],checkResult[1],checkResult[2],checkResult[3])
        contentList.append(data)

    content="\n".join(contentList)

    # MIMEMultipart 객체 생성
    timeNow=datetime.datetime.now().strftime("%Y년%m월%d일 %H시%M분%S초")
    msg = MIMEMultipart('alternative')
    msg["Subject"] = "[가격알림]FARFETCH 상품가격 알림 메일_{}".format(timeNow)  # 메일 제목
    msg['From'] = username
    msg['To'] = to_email
    msg['Cc'] = cc_email  # 참조 이메일 주소 추가
    msg.attach(MIMEText(content, 'plain'))

    # SMTP 서버 연결 및 로그인
    server = smtplib.SMTP(smtp_server, smtp_port)
    # print(server)
    server.starttls()
    server.login(username, password)
    # 이메일 전송 (수신자와 참조자 모두에게 전송)
    to_and_cc_emails = [to_email] + [cc_email]
    server.sendmail(username, to_and_cc_emails, msg.as_string())
    # SMTP 서버 연결 종료
    server.quit()
    print("전송완료")

def GetDB(daysAgo):
    # MySQL 연결 정보 설정
    host = 'database-2.crbwjwvrwwze.ap-northeast-2.rds.amazonaws.com'
    user = 'admin'
    password = 'dlwndwo2'
    database = 'information'

    # MySQL 연결
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    try:
        # 어제의 00:00:00과 오늘의 00:00:00 계산

        today = datetime.datetime.now().date()
        yesterday_start = datetime.datetime(today.year, today.month, today.day) - datetime.timedelta(days=daysAgo)
        yesterday_end = datetime.datetime(today.year, today.month, today.day) - datetime.timedelta(days=daysAgo-1)
        print("yesterday_start:",yesterday_start,"/ yesterday_start_TYPE:",type(yesterday_start))
        print("yesterday_end:",yesterday_end,"/ yesterday_end_TYPE:",type(yesterday_end))
        # 어제와 오늘의 시작 시간을 UNIX 타임스탬프로 변환
        yesterday_start_unix = int(yesterday_start.timestamp())
        yesterday_end_unix = int(yesterday_end.timestamp())



        with connection.cursor() as cursor:
            # SQL 쿼리 작성
            sql = "SELECT * FROM kream WHERE CAST(regiTimestamp AS SIGNED) >= {} AND CAST(regiTimestamp AS SIGNED) <= {}".format(yesterday_start_unix,yesterday_end_unix)

            # 쿼리 실행
            cursor.execute(sql)

            # 결과 가져오기
            result = cursor.fetchall()

            # 결과를 dict 리스트로 저장
            data_list = []
            column_names = [i[0] for i in cursor.description]  # 열 이름 가져오기

            for row in result:
                data_dict = {}
                for i, value in enumerate(row):
                    column_name = column_names[i]
                    data_dict[column_name] = value
                data_list.append(data_dict)
            # pprint.pprint(data_list)
        print("yesterday_start_unix:",yesterday_start_unix,"/ yesterday_start_unix_TYPE:",type(yesterday_start_unix))
        print("yesterday_end_unix:",yesterday_end_unix,"/ yesterday_end_unix_TYPE:",type(yesterday_end_unix))
    finally:
        # 연결 닫기
        connection.close()
    pprint.pprint(data_list)
    df=pd.read_excel('exception.xlsx')

    # DataFrame을 dict로 변환
    exceptionList = df.to_dict(orient='records')
    print("exceptionList:",exceptionList,"/ exceptionList_TYPE:",type(exceptionList))
    newList=[]
    for data_elem in data_list:
        findFlag=False
        for exception in exceptionList:
            try:
                if data_elem['productName'].find(exception['productName'])>=0:
                    findFlag=True
            except:
                # print("없음")
                pass
        if findFlag==False:
            try:
                data_elem['modelNumber']=data_elem['modelNumber'].replace("-","")
            except:
                data_elem['modelNumber']=""
            newList.append(data_elem)

    # modelNumber를 키로 하고 productName을 값으로 하는 딕셔너리 생성
    model_product_dict = {item['modelNumber']: item['productName'] for item in newList}

    # 딕셔너리를 리스트로 변환
    model_product_list = [{'modelNumber': k, 'productName': v} for k, v in model_product_dict.items()]

    print(model_product_list)

    return newList,model_product_list

def FindProduct(searchKeyword,productName,inputList,mappingTable):
    cookies = {
        'BIcookieID': 'b90efa7b-dda2-44d2-a923-1d8f0dfb0d16',
        'ckm-ctx-sf': '%2Fkr',
        'ffcp': 'a.1.0_f.1.0_p.1.0_c.1.0',
        'ub': '50CAC614848E6A27CBC86CA9829B46A4',
        'ff_navroot_history': '141259',
        'checkoutType2': '4',
        'session-1': 'a34320b7-f603-9c2e-ed15-ecbb319df93d',
        '_gcl_au': '1.1.2009181326.1702527535',
        '_cs_c': '0',
        'fita.sid.farfetch': 'csVLcpbY9MacxD5oQwH0sakbszrL8xes',
        'rskxRunCookie': '0',
        'rCookie': 'dk319jmjfv5y3iutkyol7lq4oxpud',
        'FPID': 'FPID2.3.2bNz%2BZUfcYF%2Fgg%2BCBTLVamfbX4QC5%2F8vAAWLGaCPeIQ%3D.1702527535',
        'FPAU': '1.1.2009181326.1702527535',
        '_gid': 'GA1.2.212746181.1703053000',
        'g_state': '{"i_p":1703157106838,"i_l":2}',
        '_abck': 'D92E8D7F27247B71A4C70ACA1FC18787~0~YAAQJCPJF1mGSW2MAQAA9n0TiwuLgl+J+3aBtCE2pUcrOczf9fC+cglkjAVBBwomXJHDBosV4IDUu0FW90zTNQe6+9+hqLx7LNPUtARun4O7b4L7L6qI5Cx84GmX6+hPnVq4+bZfxEeowecWS+F13I4ReK6AWMfDbJ0zns+/zfFTjflhI6FGWaPR//NFgQQLRZydYBy6N63E9Ym6cSphoxZivCRFcn6hII0Vi9NfJfr8pL+8s+shQYsYvHMS/WwodmyjKW8z8FhEv8hAiWGhXyZRps6uUDzSHV2S8atS4Pdy/m+Xbq/K8kD9Kj7FB4b8HTvNFLix4Om3Ff5DAfb/2RJOBa6EEUV1OjIHpGN8HK7fBZnYkXhedUD4VJXDGd4MOuVgKUi/DwUuuRC/VUD35vsmPwuX9ZC9XPk=~-1~-1~-1',
        'bm_sz': 'EB422CF4C043C331D6D8AC7FD9A06530~YAAQJCPJF1qGSW2MAQAA9n0TixbcdaZEQcQbJieh/JPsZGSk86Y+1kLQPUg6zYFI8VHGWuEVdtF5o03auxny9BTKGy1vXg/HtUVlXF8TxPi4pRcF+HdArfZmsq9fCTno3LVwf36D/NmaN4u7cdPb77/3/HMb5/X+1ZSJROdtEkhQFAKaIE2KTkLQjNJA8A3BvgkIRbX7PZPE3eWuDRcNAupYlHVuJRMfsaweG/n/ylBiAXfcj0pS6jPLnewSXX58yWETXJ+Qp/i8RNtM5I0pBjv7ARt95QxPOD2hFBqydPDYJjjyIQ==~3617337~3686708',
        '__Host-FF.AppSession': 'CfDJ8BZV7bSK%2FgVKoJ5%2FtFR15T49T04bmYVLP7oBbiTV%2B82e7MLO8ve7EshECrdU3AMKyetdNHIFg5BCFB3cqaVfnRcNTan0QA1Fu7oRroixufOP3QqEkSFtfJDWL2VtYQf%2FFti6ZAHJfv7ISm6WdWLIxBl6wSvGggqZG5u%2FDwOhIObb',
        'BISessionId': '9df9ff98-7779-0893-fd79-00dea471c1d5',
        '__Host-FF.AppCookie': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T5lznba-nTLa2Uce9SOjMBXb00l9xccvYVyFzvhdKncaka8Skx4GZhdOwjHO8VmwaRiM896VAYy5J4szZbLrmScBEx9I5mpaGtyEHeeftLYB4VkgmsCmLOKH5MNaVaQ3__qEkYTwPq7E0DQTaFvqQ0MHuYqyrs_3qThcKaiIs9jYesV3IeHifhC0lBig_d2lP1reWocsxiDOvZu8bHFGjekmlbNzJIvzu0isPZox4gIj8mrocUZibYcbv69caDSHvp15KwSfzsd84GwSJSQ7DAY',
        '_l': '0',
        'ABProduct': '',
        'ABListing': '',
        'ABGeneral': '',
        'ABLanding': '',
        'ABCheckout': '',
        'ABRecommendations': '',
        'ABReturns': '',
        'ABWishlist': '',
        '__Host-CSRF-TOKEN': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T5qv5BWocaF8exlTVxdT-C9U2durgU26jugFUCeoEGKtFvS1tSY2BHFD-chWp9kyqKQwH1VCpgonMUyRxglTIZCpX3IkCpkoCNSkf4InkPlG-bmzdLcXBw-BLD2_9rDLnY',
        'ff_newsletter_pv': '1',
        '__gads': 'ID=29dad16bf55ff3d9:T=1703070686:RT=1703140376:S=ALNI_MZmk3KgGzsUgv0_Ypwltw0YgBediw',
        '__gpi': 'UID=00000cb7c9501f47:T=1703070686:RT=1703140376:S=ALNI_Mbmb6m_ayOVIIue0J1fBncpYRnFTw',
        '__utmz': 'other',
        '_gcl_aw': 'GCL.1703140377.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE',
        '_cs_mk': '0.20466605386481151_1703140377062',
        '_gac_UA-3819811-6': '1.1703140377.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE',
        'ftr_blst_1h': '1703140377277',
        'FPLC': 'e2%2Fy8vDUqg3fLHnqygeSZSSJspgmn%2BuuBoSB8waEso89r4PZLCrVuVQlaGP4ZMD2dNxNUMUL9e%2BQVo3bVXvhfpQa%2FZD%2BxmWrMp68Lrw7XQLU9CVojFIgnDNDCnUb3g%3D%3D',
        'FPGCLAW': 'GCL.1703140378.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE',
        'AkamaiFeatureToggle': '02a57c.1_0357f7.1_04154b.1_0a3efc.1_1b443f.1171797472_1d8e03.1_20b92f.1_20f499.-1_247006.-1_26ddb8.1_286534.1_2ba087.1_317bfa.-1_34cea2.1_361eee.2_3aa8d2.0_3c8089.2_4247d8.-210644093_425ded.1_45dc7d.1_48259b.1_4b57a6.-1_4d76c8.2_56f7db.-1_5836e0.-1_590a92.1_5a000f.1_5a745a.-1_5dbd1a.1_5edc51.-1959550240_613a9b.-416292886_64d19c.1_67486d.-1_677d5c.351382932_678f94.0_687752.-1_6f0973.-1_729a35.1_751ef1.-1_7cf0c5.-1_81160a.-1_8c3210.-1_8c4007.-1_931982.1_945679.1_999fce.2_9a710c.1_9ebcf7.1_9f0eda.-1_a00510.1148090917_a27c87.-1_a54601.1_a7e49d.351382932_ac992b.2_ae134f.1_b45ee1.1_b833c7.535845473_b8833c.1_b8e9db.-1_b90715.0_bf110c.-1_bfc591.1_c06844.-1_c0ba66.-900375819_c2155c.1_c5e8eb.351382932_c6215a.-1_ca47d2.-1_cfc1ba.1_d052f2.909416419_d26d24.1_d47781.-1_d59758.1_da4cdf.1_dab09d.632075632_db79f1.2_dd19ed.1_deb641.-1_dec9f3.1_df039e.-1_df93a0.1_e7eec4.1_e89c2a.2_ed07fa.0_ed8d9e.1_f220ef.4_f3db94.1_f5969a.1_f8c66b.1_fb273c.-1_fb2b96.1_fb99aa.-1_fbf4d6.1_fdbb7a.0_fdd39e.-1',
        'bm_mi': '4A8D35878E4D1121663302F4FFFACD96~YAAQJCPJF+FXSm2MAQAA5G4VixYXoxuKIETzRvJWoUE8wY8OU/9sQ2b2PrqvxSta2Bdji+MC1URaod9W1uzC9wIO26B59edBKgZayvLYkqTHuhGcRkang7MoZqqFSNbWYZOE8W48CBqdsE8iJRUGyUzySkPauYQv1B3DYDzIzgPgJCDBYr0/oZXCeEFy6umqgzeNSSLMaycIAAvTntNh3pDQJTmMX+RDQe8Felfp48e3jNER4O3WbLldU4gOkHLVrKRKzPUpHrpo3vMnFFU2A+VEySrBHxUltdeS1ncyfRUGKhkAq4EZ47wFlY23N/HcgkV/8JBUqkPFKIMk59O/OqN+guGbtq72+FZNMRnpsyD5aoiKq6UIJPr5yA==~1',
        'ak_bmsc': '4B9E9A6B333DE887713592B8C9788C64~000000000000000000000000000000~YAAQJCPJF5RbSm2MAQAAeHQVixZyT4VbUKf8Q2D8ARRmS8ez0jidXSTrsOymxVT1ODOwJSbqHAcdfg6p+WxqCl9QAbo0a3I9dCYOqgAYNwxHFNDQlWBnYFsCeI4bkW792aa+70qQfTSgetyqYfhacxpgdo+2ZCNf5vvQH9y8y4UUVXN44ALxtG/rE9DOMmcgI/Cf8/n15YTJICDo4j6c1e4df4j+tF2+mF2xZNHry5LSv1sjyvXcdbh+N5JjiwyF6guEJAN9crEZFTe0/Hhdf+ZoF7qYIKlNhGgkOFJuukhpdHBiJ8CLnyxyKb6MQXnhmxVLjrgcE6g4hWk0DcfZcVakmaV7Y9nGDos4aG0LkEUU+T0EO8S5vZwQd9qFuApTFqrgTNY13ksAj6uYhTCvtmLJi6Wp4GCDian7rPv+6zPEKa5nMuBD5EclzMhJDCI3lIv96nPZTR83JmQYOiXup4KZ5EpqnVicq9fJev+D3XsivbaIQ/TyxbZnQSm8GA61K+OGRcode5gcM9GCSIw/0TPq4rY3q9qv6Hr06hPJzx0OKWTEymQyjLvpt4zteJHE17HFlJwIGHo0IGkVubU7',
        '__cuid': '85e78c95cc654bf0bb909ec05fd16a64',
        'lastRskxRun': '1703140493163',
        '_ga_CEF7PMN9HX': 'GS1.1.1703140377.8.1.1703140493.28.0.0',
        '_ga': 'GA1.1.366628483.1702527535',
        '_uetsid': '565a18409eff11eeb14eff7f4c8dfadf',
        '_uetvid': 'd79975106e7a11eeaf1c895a21f2d376',
        '_cs_id': '464c9063-732f-a1d9-98c6-443172eb2580.1702527534.7.1703140493.1703140377.1.1736691534721',
        '_cs_s': '4.0.0.1703142293448',
        'cto_bundle': 'Hhrwel8yMExsUTlvNWNoZlhkJTJCVmpISGt4WThRUWw5VTdxYmNUJTJCNmV1aHdQUUElMkJ6bXF6R2tLOWpNM1RKUjY1a0NIbW1odmJxSnBZRXRmelhUUjczbVV5NWhoUWxWVDVUVVhyVVN0dzJ5dTAwUFNFV2JjVmElMkIzWE43UGFPMEpGNUZCclpJdUh6dWNNZSUyRkMlMkZtd1dVSlhVUDI4UVlNdTNMSTRpMnhqaWVYbEE1JTJGaXc4NVp0OUVoMiUyQkFCMU10dVlTaSUyRkh6YUdDdUdQWU5mUThpZTh2YWpIcXpaTXRpVkZ1eU5GeHRFeVJqU0FmeVdJU0oxQ2FwdWdlVmdvNGxSa01iRDY4QnczOU9aaWZ3Zlh6bTNxSWRmYkZMT1NvZyUzRCUzRA',
        'forterToken': '7be195e88478413faf6966cf8dbe11d8_1703140492404__UDF43-m4_11ck_',
        '_ga_HLS8C90D41': 'GS1.1.1703140377.8.0.1703140565.0.0.0',
        '__Host-CSRF-REQUEST-TOKEN': 'CfDJ8BZV7bSK_gVKoJ5_tFR15T57C0bw_Q-NYLklsuRrXiI2DygbniAwAZWexzbWKrA2h13APuGbaZrpXfug0xrsh23oNvScrWmr9DWyqLmfNLbCd3UD-M_5SfSoLygLPEb52FwFqBITODaEweBpu9Mn6ZjrsDaQDPzQDQNIobFg69tI6lnLR66jtSG0knpH9_JCFw',
        'bm_sv': 'C591F1E11B3C76563BD23696C316FA78~YAAQJCPJF4XaSm2MAQAAHqQWixaie18aAY93KpYwbd0l+bEVRCSEjCTJvbLQtdmWq2qO6OOh41acVjD88f5ufNn8CBvtTl7oLCN7/5dq+d/jHJdBgOscEn8cA3G0yJyG+Z30wdtIxe3BhbwlcY2eAAlHQsoKUQ72Fr/yMg2vplYz+HT8eiTJWFFXwrf6Rqk4W6OdbBpHnBFPmZQa0gIyxKiabAcUqpMMn2TMXc3ENy9NTLW8Tsg6nZZl6o9Z1FTwUHiE~1',
        'RT': '"z=1&dm=www.farfetch.com&si=e64de64e-60a5-4e71-b930-0ccafd507e24&ss=lqetsorv&sl=4&tt=f79&obo=2&rl=1&ld=4qfr&r=jdnbz45&ul=4qfr"',
    }

    headers = {
        'authority': 'www.farfetch.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'BIcookieID=b90efa7b-dda2-44d2-a923-1d8f0dfb0d16; ckm-ctx-sf=%2Fkr; ffcp=a.1.0_f.1.0_p.1.0_c.1.0; ub=50CAC614848E6A27CBC86CA9829B46A4; ff_navroot_history=141259; checkoutType2=4; session-1=a34320b7-f603-9c2e-ed15-ecbb319df93d; _gcl_au=1.1.2009181326.1702527535; _cs_c=0; fita.sid.farfetch=csVLcpbY9MacxD5oQwH0sakbszrL8xes; rskxRunCookie=0; rCookie=dk319jmjfv5y3iutkyol7lq4oxpud; FPID=FPID2.3.2bNz%2BZUfcYF%2Fgg%2BCBTLVamfbX4QC5%2F8vAAWLGaCPeIQ%3D.1702527535; FPAU=1.1.2009181326.1702527535; _gid=GA1.2.212746181.1703053000; g_state={"i_p":1703157106838,"i_l":2}; _abck=D92E8D7F27247B71A4C70ACA1FC18787~0~YAAQJCPJF1mGSW2MAQAA9n0TiwuLgl+J+3aBtCE2pUcrOczf9fC+cglkjAVBBwomXJHDBosV4IDUu0FW90zTNQe6+9+hqLx7LNPUtARun4O7b4L7L6qI5Cx84GmX6+hPnVq4+bZfxEeowecWS+F13I4ReK6AWMfDbJ0zns+/zfFTjflhI6FGWaPR//NFgQQLRZydYBy6N63E9Ym6cSphoxZivCRFcn6hII0Vi9NfJfr8pL+8s+shQYsYvHMS/WwodmyjKW8z8FhEv8hAiWGhXyZRps6uUDzSHV2S8atS4Pdy/m+Xbq/K8kD9Kj7FB4b8HTvNFLix4Om3Ff5DAfb/2RJOBa6EEUV1OjIHpGN8HK7fBZnYkXhedUD4VJXDGd4MOuVgKUi/DwUuuRC/VUD35vsmPwuX9ZC9XPk=~-1~-1~-1; bm_sz=EB422CF4C043C331D6D8AC7FD9A06530~YAAQJCPJF1qGSW2MAQAA9n0TixbcdaZEQcQbJieh/JPsZGSk86Y+1kLQPUg6zYFI8VHGWuEVdtF5o03auxny9BTKGy1vXg/HtUVlXF8TxPi4pRcF+HdArfZmsq9fCTno3LVwf36D/NmaN4u7cdPb77/3/HMb5/X+1ZSJROdtEkhQFAKaIE2KTkLQjNJA8A3BvgkIRbX7PZPE3eWuDRcNAupYlHVuJRMfsaweG/n/ylBiAXfcj0pS6jPLnewSXX58yWETXJ+Qp/i8RNtM5I0pBjv7ARt95QxPOD2hFBqydPDYJjjyIQ==~3617337~3686708; __Host-FF.AppSession=CfDJ8BZV7bSK%2FgVKoJ5%2FtFR15T49T04bmYVLP7oBbiTV%2B82e7MLO8ve7EshECrdU3AMKyetdNHIFg5BCFB3cqaVfnRcNTan0QA1Fu7oRroixufOP3QqEkSFtfJDWL2VtYQf%2FFti6ZAHJfv7ISm6WdWLIxBl6wSvGggqZG5u%2FDwOhIObb; BISessionId=9df9ff98-7779-0893-fd79-00dea471c1d5; __Host-FF.AppCookie=CfDJ8BZV7bSK_gVKoJ5_tFR15T5lznba-nTLa2Uce9SOjMBXb00l9xccvYVyFzvhdKncaka8Skx4GZhdOwjHO8VmwaRiM896VAYy5J4szZbLrmScBEx9I5mpaGtyEHeeftLYB4VkgmsCmLOKH5MNaVaQ3__qEkYTwPq7E0DQTaFvqQ0MHuYqyrs_3qThcKaiIs9jYesV3IeHifhC0lBig_d2lP1reWocsxiDOvZu8bHFGjekmlbNzJIvzu0isPZox4gIj8mrocUZibYcbv69caDSHvp15KwSfzsd84GwSJSQ7DAY; _l=0; ABProduct=; ABListing=; ABGeneral=; ABLanding=; ABCheckout=; ABRecommendations=; ABReturns=; ABWishlist=; __Host-CSRF-TOKEN=CfDJ8BZV7bSK_gVKoJ5_tFR15T5qv5BWocaF8exlTVxdT-C9U2durgU26jugFUCeoEGKtFvS1tSY2BHFD-chWp9kyqKQwH1VCpgonMUyRxglTIZCpX3IkCpkoCNSkf4InkPlG-bmzdLcXBw-BLD2_9rDLnY; ff_newsletter_pv=1; __gads=ID=29dad16bf55ff3d9:T=1703070686:RT=1703140376:S=ALNI_MZmk3KgGzsUgv0_Ypwltw0YgBediw; __gpi=UID=00000cb7c9501f47:T=1703070686:RT=1703140376:S=ALNI_Mbmb6m_ayOVIIue0J1fBncpYRnFTw; __utmz=other; _gcl_aw=GCL.1703140377.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE; _cs_mk=0.20466605386481151_1703140377062; _gac_UA-3819811-6=1.1703140377.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE; ftr_blst_1h=1703140377277; FPLC=e2%2Fy8vDUqg3fLHnqygeSZSSJspgmn%2BuuBoSB8waEso89r4PZLCrVuVQlaGP4ZMD2dNxNUMUL9e%2BQVo3bVXvhfpQa%2FZD%2BxmWrMp68Lrw7XQLU9CVojFIgnDNDCnUb3g%3D%3D; FPGCLAW=GCL.1703140378.CjwKCAiAvoqsBhB9EiwA9XTWGTV1OABvfiI2S4_YwduYpUWAzgGMz26ycm3LNBH6297Lp_zd6CKUSRoCWykQAvD_BwE; AkamaiFeatureToggle=02a57c.1_0357f7.1_04154b.1_0a3efc.1_1b443f.1171797472_1d8e03.1_20b92f.1_20f499.-1_247006.-1_26ddb8.1_286534.1_2ba087.1_317bfa.-1_34cea2.1_361eee.2_3aa8d2.0_3c8089.2_4247d8.-210644093_425ded.1_45dc7d.1_48259b.1_4b57a6.-1_4d76c8.2_56f7db.-1_5836e0.-1_590a92.1_5a000f.1_5a745a.-1_5dbd1a.1_5edc51.-1959550240_613a9b.-416292886_64d19c.1_67486d.-1_677d5c.351382932_678f94.0_687752.-1_6f0973.-1_729a35.1_751ef1.-1_7cf0c5.-1_81160a.-1_8c3210.-1_8c4007.-1_931982.1_945679.1_999fce.2_9a710c.1_9ebcf7.1_9f0eda.-1_a00510.1148090917_a27c87.-1_a54601.1_a7e49d.351382932_ac992b.2_ae134f.1_b45ee1.1_b833c7.535845473_b8833c.1_b8e9db.-1_b90715.0_bf110c.-1_bfc591.1_c06844.-1_c0ba66.-900375819_c2155c.1_c5e8eb.351382932_c6215a.-1_ca47d2.-1_cfc1ba.1_d052f2.909416419_d26d24.1_d47781.-1_d59758.1_da4cdf.1_dab09d.632075632_db79f1.2_dd19ed.1_deb641.-1_dec9f3.1_df039e.-1_df93a0.1_e7eec4.1_e89c2a.2_ed07fa.0_ed8d9e.1_f220ef.4_f3db94.1_f5969a.1_f8c66b.1_fb273c.-1_fb2b96.1_fb99aa.-1_fbf4d6.1_fdbb7a.0_fdd39e.-1; bm_mi=4A8D35878E4D1121663302F4FFFACD96~YAAQJCPJF+FXSm2MAQAA5G4VixYXoxuKIETzRvJWoUE8wY8OU/9sQ2b2PrqvxSta2Bdji+MC1URaod9W1uzC9wIO26B59edBKgZayvLYkqTHuhGcRkang7MoZqqFSNbWYZOE8W48CBqdsE8iJRUGyUzySkPauYQv1B3DYDzIzgPgJCDBYr0/oZXCeEFy6umqgzeNSSLMaycIAAvTntNh3pDQJTmMX+RDQe8Felfp48e3jNER4O3WbLldU4gOkHLVrKRKzPUpHrpo3vMnFFU2A+VEySrBHxUltdeS1ncyfRUGKhkAq4EZ47wFlY23N/HcgkV/8JBUqkPFKIMk59O/OqN+guGbtq72+FZNMRnpsyD5aoiKq6UIJPr5yA==~1; ak_bmsc=4B9E9A6B333DE887713592B8C9788C64~000000000000000000000000000000~YAAQJCPJF5RbSm2MAQAAeHQVixZyT4VbUKf8Q2D8ARRmS8ez0jidXSTrsOymxVT1ODOwJSbqHAcdfg6p+WxqCl9QAbo0a3I9dCYOqgAYNwxHFNDQlWBnYFsCeI4bkW792aa+70qQfTSgetyqYfhacxpgdo+2ZCNf5vvQH9y8y4UUVXN44ALxtG/rE9DOMmcgI/Cf8/n15YTJICDo4j6c1e4df4j+tF2+mF2xZNHry5LSv1sjyvXcdbh+N5JjiwyF6guEJAN9crEZFTe0/Hhdf+ZoF7qYIKlNhGgkOFJuukhpdHBiJ8CLnyxyKb6MQXnhmxVLjrgcE6g4hWk0DcfZcVakmaV7Y9nGDos4aG0LkEUU+T0EO8S5vZwQd9qFuApTFqrgTNY13ksAj6uYhTCvtmLJi6Wp4GCDian7rPv+6zPEKa5nMuBD5EclzMhJDCI3lIv96nPZTR83JmQYOiXup4KZ5EpqnVicq9fJev+D3XsivbaIQ/TyxbZnQSm8GA61K+OGRcode5gcM9GCSIw/0TPq4rY3q9qv6Hr06hPJzx0OKWTEymQyjLvpt4zteJHE17HFlJwIGHo0IGkVubU7; __cuid=85e78c95cc654bf0bb909ec05fd16a64; lastRskxRun=1703140493163; _ga_CEF7PMN9HX=GS1.1.1703140377.8.1.1703140493.28.0.0; _ga=GA1.1.366628483.1702527535; _uetsid=565a18409eff11eeb14eff7f4c8dfadf; _uetvid=d79975106e7a11eeaf1c895a21f2d376; _cs_id=464c9063-732f-a1d9-98c6-443172eb2580.1702527534.7.1703140493.1703140377.1.1736691534721; _cs_s=4.0.0.1703142293448; cto_bundle=Hhrwel8yMExsUTlvNWNoZlhkJTJCVmpISGt4WThRUWw5VTdxYmNUJTJCNmV1aHdQUUElMkJ6bXF6R2tLOWpNM1RKUjY1a0NIbW1odmJxSnBZRXRmelhUUjczbVV5NWhoUWxWVDVUVVhyVVN0dzJ5dTAwUFNFV2JjVmElMkIzWE43UGFPMEpGNUZCclpJdUh6dWNNZSUyRkMlMkZtd1dVSlhVUDI4UVlNdTNMSTRpMnhqaWVYbEE1JTJGaXc4NVp0OUVoMiUyQkFCMU10dVlTaSUyRkh6YUdDdUdQWU5mUThpZTh2YWpIcXpaTXRpVkZ1eU5GeHRFeVJqU0FmeVdJU0oxQ2FwdWdlVmdvNGxSa01iRDY4QnczOU9aaWZ3Zlh6bTNxSWRmYkZMT1NvZyUzRCUzRA; forterToken=7be195e88478413faf6966cf8dbe11d8_1703140492404__UDF43-m4_11ck_; _ga_HLS8C90D41=GS1.1.1703140377.8.0.1703140565.0.0.0; __Host-CSRF-REQUEST-TOKEN=CfDJ8BZV7bSK_gVKoJ5_tFR15T57C0bw_Q-NYLklsuRrXiI2DygbniAwAZWexzbWKrA2h13APuGbaZrpXfug0xrsh23oNvScrWmr9DWyqLmfNLbCd3UD-M_5SfSoLygLPEb52FwFqBITODaEweBpu9Mn6ZjrsDaQDPzQDQNIobFg69tI6lnLR66jtSG0knpH9_JCFw; bm_sv=C591F1E11B3C76563BD23696C316FA78~YAAQJCPJF4XaSm2MAQAAHqQWixaie18aAY93KpYwbd0l+bEVRCSEjCTJvbLQtdmWq2qO6OOh41acVjD88f5ufNn8CBvtTl7oLCN7/5dq+d/jHJdBgOscEn8cA3G0yJyG+Z30wdtIxe3BhbwlcY2eAAlHQsoKUQ72Fr/yMg2vplYz+HT8eiTJWFFXwrf6Rqk4W6OdbBpHnBFPmZQa0gIyxKiabAcUqpMMn2TMXc3ENy9NTLW8Tsg6nZZl6o9Z1FTwUHiE~1; RT="z=1&dm=www.farfetch.com&si=e64de64e-60a5-4e71-b930-0ccafd507e24&ss=lqetsorv&sl=4&tt=f79&obo=2&rl=1&ld=4qfr&r=jdnbz45&ul=4qfr"',
        'referer': 'https://www.farfetch.com/kr/shopping/men/items.aspx',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.111", "Google Chrome";v="120.0.6099.111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    params = {
        'q': searchKeyword,
        # 'rc': '141259',
    }

    response = requests.get('https://www.farfetch.com/kr/search', params=params, cookies=cookies, headers=headers)
    response=response.content.decode('utf-8')
    soup=BeautifulSoup(response,'lxml')
    
    try:
        url=soup.find("meta",attrs={'property':'og:url'})['content']
    except:
        url=""
    print("url:",url,"/ url_TYPE:",type(url))
    if len(url)==0:
        print("URL없음")
        data=[]
        return data

    styleId=soup.find("span",attrs={'class':'ltr-4y8w0i-Body'}).get_text()
    
    scripts=soup.find_all("script")
    result=""
    for script in scripts:
        if script.text.find("apolloInitialState")>=0:
            # print(script.text)
            result=str(script)
    positionFr=result.find('"')
    positionRr = result.rfind('"')
    data=result[positionFr:positionRr+1]
    result=json.loads(json.loads(data))['apolloInitialState']

    brandStyleId=find_brand_style_id(result)

    compareRatio=compare(searchKeyword,brandStyleId)
    if compareRatio>=0.4:
        print("비슷함")
    else:
        print("비슷하지않음")
        dataList=[]
        return dataList

    # "availableIn" 키를 포함하는 모든 딕셔너리 찾기
    found_dicts = list(find_dicts_with_key(result, 'availableIn'))
    # 결과 출력
    # 새로운 리스트 생성
    new_list = []

    # 반복문을 사용하여 "id"와 "description" 값을 추출하고 새로운 리스트에 추가
    for item in found_dicts:
        new_item = {
            'id': item['id'],
            'description': item['description']
        }
        new_list.append(new_item)
    # 결과 출력
    # print(new_list) ## 단위 환산 표

    dataList=[]
    # 'Variation:'으로 시작하는 키(key) 값을 가지는 항목들을 찾아서 리스트로 저장합니다.
    variation_values = [value for key, value in result.items() if key.startswith('Variation:')]
    for variation in variation_values:
        # pprint.pprint(variation)
        if variation['quantity']>=1:
            price=variation['price']['value']['formatted'].replace(",","")
            regex=re.compile('\d+')
            price=regex.findall(price)[0]
            # print("price:",price,"/ price_TYPE:",type(price))
            idRaw=variation['variationProperties'][0]['values'][0]['__ref']

            # JSON 부분 추출
            json_part = idRaw.split(':', 1)[1]  # 'ScaledSizeVariationPropertyValue:'를 제거하고 JSON 부분 추출
            # JSON 파싱
            data = json.loads(json_part)
            # 'id' 값 추출
            id_value = str(data.get('id'))
            size=""
            for new_elem in new_list:
                if str(new_elem['id'])==str(id_value):
                    size=new_elem['description']
            # print("size:",size,"/ size_TYPE:",type(size))

            data={'modelName':searchKeyword,'price':price,'size':size,'productName':productName}
            # print("data:",data,"/ data_TYPE:",type(data))
            for inputElem in inputList:
                inputModelName=inputElem['modelNumber'].replace("-","")
                if inputModelName.find("/")>=0:
                    inputModelName=inputModelName.split("/")[-1]
                if inputModelName==searchKeyword:
                    for mappingData in mappingTable:
                        if mappingData['AND 키워드'].find("NOT")>=0:
                            if productName.find(mappingData['포함 키워드']) >= 0 and productName.find(
                                mappingData['AND 키워드'].replace("NOT ","")) < 0 and str(size)==str(mappingData['SIZE_FF']):
                                resultSize=mappingData['SIZE_KR']
                                print("inputModelName:",inputModelName,"/ inputModelName_TYPE:",type(inputModelName))
                                try:
                                    comparePrice=int(inputElem['avgX'])*float(inputElem['avg3PeravgX'])
                                except:
                                    comparePrice=1

                                print("comparePrice:",comparePrice,"realPrice:",price,'size:',size,'case1')
                                if (str(resultSize)==str(inputElem['size']) or size=="원사이즈") and int(price)<int(comparePrice):
                                    #이름,사이즈,가격,주소
                                    data=[productName,size,price,url]
                                    print("data:",data,"/ data_TYPE:",type(data))
                                    dataList.append(data)
                                    break

                            else:
                                resultSize=size
                                # print("resultSize:",resultSize,"/ resultSize_TYPE:",type(resultSize))
                                try:
                                    comparePrice=int(inputElem['avgX'])*float(inputElem['avg3PeravgX'])
                                except:
                                    comparePrice=1
                                print("comparePrice:", comparePrice, "realPrice:", price,'case2')
                                if str(resultSize)==str(size) and int(price)<int(comparePrice):
                                    #이름,사이즈,가격,주소
                                    data=[productName,size,price,url]
                                    print("data:", data, "/ data_TYPE:", type(data))
                                    dataList.append(data)
                                    break

                        else:
                            if productName.find(mappingData['포함 키워드']) >= 0 and productName.find(
                                    mappingData['AND 키워드']) >= 0 and str(size) == str(mappingData['SIZE_FF']):
                                resultSize = mappingData['SIZE_KR']
                                # print("resultSize:",resultSize,"/ resultSize_TYPE:",type(resultSize))
                                try:
                                    comparePrice=int(inputElem['avgX'])*float(inputElem['avg3PeravgX'])

                                except:
                                    comparePrice=1
                                print("comparePrice:", comparePrice, "realPrice:", price,'size:',size,'case3')
                                if str(resultSize)==str(size) and int(price)<int(comparePrice):
                                    #이름,사이즈,가격,주소
                                    data=[productName,size,price,url]
                                    print("data:", data, "/ data_TYPE:", type(data))
                                    dataList.append(data)
                                    break

                            else:
                                resultSize = size
                                try:
                                    comparePrice=int(inputElem['avgX'])*float(inputElem['avg3PeravgX'])
                                except:
                                    comparePrice=1
                                print("comparePrice:", comparePrice, "realPrice:", price, 'size:', size, 'case4')
                                # print("comparePrice:", comparePrice, "realPrice:", price)
                                if (str(resultSize)==str(size) or size=="원사이즈") and int(price)<int(comparePrice):
                                    #이름,사이즈,가격,주소
                                    data=[productName,size,price,url]
                                    print("data:", data, "/ data_TYPE:", type(data))
                                    dataList.append(data)
                                    break


            # print("=========================")

    return dataList

while True:
    # Excel 파일 경로
    file_path = 'mapping.xlsx'

    # header는 엑셀의 헤더로 사용할 행의 번호입니다. 기본값은 0(첫 번째 행)입니다.
    df = pd.read_excel(file_path)

    # NaN 값을 빈 문자열로 대체
    df.fillna('', inplace=True)
    # DataFrame을 딕셔너리로 변환

    # orient='records'는 각 행을 개별 딕셔너리로 변환합니다.
    mappingTable = df.to_dict(orient='records')
    print("mappingTable:",mappingTable,"/ mappingTable_TYPE:",type(mappingTable))

    daysAgo=1

    inputList,modelNumbers=GetDB(daysAgo)
    with open('modelNumbers.json', 'w',encoding='utf-8-sig') as f:
        json.dump(modelNumbers, f, indent=2,ensure_ascii=False)
    with open ('modelNumbers.json', "r",encoding='utf-8-sig') as f:
        modelNumbers = json.load(f)

    count=0
    print("modelNumbers:",modelNumbers,"/ modelNumbers_TYPE:",type(modelNumbers))
    print("len(modelNumbers):",len(modelNumbers),"/ len(modelNumbers)_TYPE:",type(len(modelNumbers)))
    with open('inputList.json', 'w',encoding='utf-8-sig') as f:
        json.dump(inputList, f, indent=2,ensure_ascii=False)

    checkResult=[]
    for index,modelNumber in enumerate(modelNumbers):
        print("{}/{}확인중...".format(index+1,len(modelNumbers)))
        print("modelNumber:",modelNumber,"/ modelNumber_TYPE:",type(modelNumber))
        searchKeyword=modelNumber['modelNumber'].replace("-","")
        productName=modelNumber['productName']
        if searchKeyword.find("/")>=0:
            searchKeyword=searchKeyword.split("/")[-1]

        # searchKeyword='CU1726100'
        result=FindProduct(searchKeyword,productName,inputList,mappingTable)
        if len(result)>=1:
            checkResult.extend(result)
            count+=1
        with open('checkResult.json', 'w', encoding='utf-8-sig') as f:
            json.dump(checkResult, f, indent=2, ensure_ascii=False)

    # 리스트의 각 요소를 튜플로 변환
    tuple_list = [tuple(sublist) for sublist in checkResult]

    # 중복 제거
    unique_tuples = set(tuple_list)

    # 다시 리스트로 변환
    unique_lists = [list(t) for t in unique_tuples]

    checkResult=unique_lists

    email='wsgt18@naver.com'
    SendMail(unique_lists,email)
    time.sleep(60*60)

    


