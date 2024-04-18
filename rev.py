import requests

cookies = {
    '_gcl_au': '1.1.1552196191.1711087581',
    'device_id': 'bc051646-969c-48fa-9328-866635b473f5',
    'AMP_MKTG_b34eb5901c': 'JTdCJTdE',
    '_fbp': 'fb.1.1711087584159.219338993',
    '_tt_enable_cookie': '1',
    '_ttp': 'JnJYlveC8vZmSMe8Vojed-z1KCg',
    'g_state': '{"i_l":0}',
    'session_access_token': 'eyJraWQiOiJfVWFrNjM5ekx2WHZ3R05MeDZvaXlFbjM0eG9EeWlJWSJ9.eyJhdWQiOiJ0aWtldC5jb20iLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTcyNzEyNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ.6TcFWIpwmLcqz-d_nJnbs068o5fvOWEWu5rmZWtmY4slnDdhRnZ5hf0eKVJlKE0u',
    'session_refresh_token': 'eyJraWQiOiJUSmZwelBDak1aUVI2TjEtczRPMy1LaDNUYmdYZXpQZCJ9.eyJhdWQiOiJ0aWtldC5jb20vcnQiLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTc0MjkwNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ._M3xhOrKGy1dwGak_yjXmlJRMJW1ObwO5Q07an1slb1LfDPPf1s_JMelyX_FSWFU',
    'userlang': 'id',
    'tiket_currency': 'IDR',
    '_cfuvid': 'S9oW4Qc5NPqhEUeX54e7ImZclsH4ogoWrpEvHYRfULc-1713236363667-0.0.1.1-604800000',
    'cf_clearance': 'uGmog_yBrhxV4VEYS1OlReYedwtxQUCP9Hi.CR446zI-1713236365-1.0.1.1-a4WuQws5HH959RhDlyojI4hl2rzsgB_ehtHlSRkD_RkMPEhgmJahnA.8jTAeXGjalMDy7VCm.v9uT_Gz33AoMg',
    '_gid': 'GA1.2.1667655849.1713236366',
    'ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%22d2c65d43-b251-5fce-84e7-d6b4eafc90cc%22%2C%22c%22%3A1711087581539%2C%22l%22%3A1713236366421%7D',
    'ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%2247c106a6-987a-85ba-afca-1ae09e2e5553%22%2C%22e%22%3A1713238171199%2C%22c%22%3A1713236366418%2C%22l%22%3A1713236371199%7D',
    'country_code': 'id',
    'source': 'hotel',
    'HOTEL_UUID': 'u9NoijHOAA1Aja2x6QpWrq_t7CxYMhAjiVt6do_3RF0',
    '__cf_bm': 'UDAODAxCd0P7VUaX6LXzM8S4ZeA3D4h_fhdAiBlCYTs-1713250559-1.0.1.1-y2M.VaqkfKbsiJXi0aSK9.qZYGV9LupgyroYCoozFm67DA_.JRPnJ9ryGHfTaOS3Q3AtHJYFgpuPWzLbnGhA95HnZios9si2UgHfuoijJ7o',
    '_tix_logger_correlation_id': 'a8756bb0-187e-49bc-bca5-cd6952c4cd96',
    'AMP_b34eb5901c': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYzA1MTY0Ni05NjljLTQ4ZmEtOTMyOC04NjY2MzViNDczZjUlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDEwNDUxMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTMyNTA1NjEwODQlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzEzMjUwNTc4NTk4JTJDJTIybGFzdEV2ZW50SWQlMjIlM0E4ODQlN0Q=',
    '_ga_7H6ZDP2ZXG': 'GS1.1.1713250558.29.1.1713250581.37.0.0',
    '_ga': 'GA1.1.977599541.1711087581',
    'amp_b34eb5': 'bc051646-969c-48fa-9328-866635b473f5.NjQxMDQ1MTM=..1hrir2dn4.1hrir2gn9.1.8.9',
}

headers = {
    'accept': '*/*',
    'accept-language': 'id',
    # 'cookie': '_gcl_au=1.1.1552196191.1711087581; device_id=bc051646-969c-48fa-9328-866635b473f5; AMP_MKTG_b34eb5901c=JTdCJTdE; _fbp=fb.1.1711087584159.219338993; _tt_enable_cookie=1; _ttp=JnJYlveC8vZmSMe8Vojed-z1KCg; g_state={"i_l":0}; session_access_token=eyJraWQiOiJfVWFrNjM5ekx2WHZ3R05MeDZvaXlFbjM0eG9EeWlJWSJ9.eyJhdWQiOiJ0aWtldC5jb20iLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTcyNzEyNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ.6TcFWIpwmLcqz-d_nJnbs068o5fvOWEWu5rmZWtmY4slnDdhRnZ5hf0eKVJlKE0u; session_refresh_token=eyJraWQiOiJUSmZwelBDak1aUVI2TjEtczRPMy1LaDNUYmdYZXpQZCJ9.eyJhdWQiOiJ0aWtldC5jb20vcnQiLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTc0MjkwNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ._M3xhOrKGy1dwGak_yjXmlJRMJW1ObwO5Q07an1slb1LfDPPf1s_JMelyX_FSWFU; userlang=id; tiket_currency=IDR; _cfuvid=S9oW4Qc5NPqhEUeX54e7ImZclsH4ogoWrpEvHYRfULc-1713236363667-0.0.1.1-604800000; cf_clearance=uGmog_yBrhxV4VEYS1OlReYedwtxQUCP9Hi.CR446zI-1713236365-1.0.1.1-a4WuQws5HH959RhDlyojI4hl2rzsgB_ehtHlSRkD_RkMPEhgmJahnA.8jTAeXGjalMDy7VCm.v9uT_Gz33AoMg; _gid=GA1.2.1667655849.1713236366; ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%22d2c65d43-b251-5fce-84e7-d6b4eafc90cc%22%2C%22c%22%3A1711087581539%2C%22l%22%3A1713236366421%7D; ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%2247c106a6-987a-85ba-afca-1ae09e2e5553%22%2C%22e%22%3A1713238171199%2C%22c%22%3A1713236366418%2C%22l%22%3A1713236371199%7D; country_code=id; source=hotel; HOTEL_UUID=u9NoijHOAA1Aja2x6QpWrq_t7CxYMhAjiVt6do_3RF0; __cf_bm=UDAODAxCd0P7VUaX6LXzM8S4ZeA3D4h_fhdAiBlCYTs-1713250559-1.0.1.1-y2M.VaqkfKbsiJXi0aSK9.qZYGV9LupgyroYCoozFm67DA_.JRPnJ9ryGHfTaOS3Q3AtHJYFgpuPWzLbnGhA95HnZios9si2UgHfuoijJ7o; _tix_logger_correlation_id=a8756bb0-187e-49bc-bca5-cd6952c4cd96; AMP_b34eb5901c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYzA1MTY0Ni05NjljLTQ4ZmEtOTMyOC04NjY2MzViNDczZjUlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDEwNDUxMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTMyNTA1NjEwODQlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzEzMjUwNTc4NTk4JTJDJTIybGFzdEV2ZW50SWQlMjIlM0E4ODQlN0Q=; _ga_7H6ZDP2ZXG=GS1.1.1713250558.29.1.1713250581.37.0.0; _ga=GA1.1.977599541.1711087581; amp_b34eb5=bc051646-969c-48fa-9328-866635b473f5.NjQxMDQ1MTM=..1hrir2dn4.1hrir2gn9.1.8.9',
    'currency': 'IDR',
    'deviceid': 'bc051646-969c-48fa-9328-866635b473f5',
    'lang': 'id',
    'referer': 'https://www.tiket.com/review?product_type=TIXHOTEL&searchType=INVENTORY&inventory_id=garden-palace-hotel-surabaya-612001703323291755&reviewSubmitColumn=RATING_SUMMARY',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-audience': 'tiket.com',
    'x-cookie-session-v2': 'true',
    'x-country-code': 'id',
    'x-currency': 'IDR',
}

params = {
    'page': '481',
    'size': '5',
    'productType': 'TIXHOTEL',
    'topic': '',
    'searchType': 'INVENTORY',
    'inventoryId': 'garden-palace-hotel-surabaya-612001703323291755',
    'reviewSubmitColumn': 'RATING_SUMMARY',
    'sortDirection': 'DESC',
}

response = requests.get(
    'https://www.tiket.com/ms-gateway/tix-review-core/verticalReview/internalReview',
    params=params,
    cookies=cookies,
    headers=headers,
)