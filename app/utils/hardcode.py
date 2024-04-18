import time
import asyncio

from playwright.async_api import async_playwright
from .helper import Helper

cookies = {
    'tiket_currency': 'IDR',
    '_gcl_au': '1.1.1552196191.1711087581',
    'device_id': 'bc051646-969c-48fa-9328-866635b473f5',
    'AMP_MKTG_b34eb5901c': 'JTdCJTdE',
    '_fbp': 'fb.1.1711087584159.219338993',
    '_tt_enable_cookie': '1',
    '_ttp': 'JnJYlveC8vZmSMe8Vojed-z1KCg',
    '_gid': 'GA1.2.2016511649.1711253269',
    'userlang': 'id',
    'ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%22d2c65d43-b251-5fce-84e7-d6b4eafc90cc%22%2C%22c%22%3A1711087581539%2C%22l%22%3A1711347624190%7D',
    'device': 'desktop',
    'g_state': '{"i_l":0}',
    'session_access_token': 'eyJraWQiOiJfVWFrNjM5ekx2WHZ3R05MeDZvaXlFbjM0eG9EeWlJWSJ9.eyJhdWQiOiJ0aWtldC5jb20iLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTcyNzEyNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ.6TcFWIpwmLcqz-d_nJnbs068o5fvOWEWu5rmZWtmY4slnDdhRnZ5hf0eKVJlKE0u',
    'session_refresh_token': 'eyJraWQiOiJUSmZwelBDak1aUVI2TjEtczRPMy1LaDNUYmdYZXpQZCJ9.eyJhdWQiOiJ0aWtldC5jb20vcnQiLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTc0MjkwNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ._M3xhOrKGy1dwGak_yjXmlJRMJW1ObwO5Q07an1slb1LfDPPf1s_JMelyX_FSWFU',
    'ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%22e8d01f12-a82d-b3e6-d7f9-572e105e0cdf%22%2C%22e%22%3A1711351467280%2C%22c%22%3A1711347624188%2C%22l%22%3A1711349667280%7D',
    'source': 'hotel',
    'HOTEL_UUID': '8Ec6vwae3ckYRLCD1FyGp7uFEQ-ZWH5ojvHE6R9L0Qs',
    '_cfuvid': 'D9FjQd.BaXJtw9009423z7ahTESwdOoT7NSlaCMZthg-1711372616039-0.0.1.1-604800000',
    'cf_clearance': 'GOZZ4L6jR7zp8iTx7Tv7qo5oeUMFHXx1ocsms2tIMFA-1711378008-1.0.1.1-nRyv3sn.jLF8yFlSyM4fcrd7T.u4nHbCLUKurCM.BpMWXbqe365zotgIWYQbTd4A7pnLS_pC2bidS7frlnhArA',
    'country_code': 'id',
    '_ga': 'GA1.2.977599541.1711087581',
    'AMP_b34eb5901c': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYzA1MTY0Ni05NjljLTQ4ZmEtOTMyOC04NjY2MzViNDczZjUlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDEwNDUxMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTEzNzc5NzUyODglMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzExMzc5NjM4MTkzJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E2MDAlN0Q=',
    '__cf_bm': 'mbApmsVTuyEjoIV88L7tSSf8jWE7m8..4P2tujfflYw-1711380012-1.0.1.1-YQBqSFxwUYtpRuzZ9atfODKFAuasI9UMqxVYzbAW5JCyfRBnDQEFJl.MatkHY4umW1UVmRaQPfuhsZ7YgkwVPvUa_yjamxO5p4lxVAMbvjE',
    '_tix_logger_correlation_id': 'a47a1658-371e-441e-980a-6c92529fd2d1',
    '_ga_7H6ZDP2ZXG': 'GS1.1.1711377974.9.1.1711380546.60.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

class HardCode(Helper):
    def __init__(self):
        super().__init__()

    async def init_playwright(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def init_hadles(self):
        await self.context.set_extra_http_headers(headers=headers)
        await self.context.add_cookies(cookies=self.convert_cookies(cookies))

    async def close(self):
        await self.page.close()
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()


    async def get_id_hard(self, keyword):
        await self.init_playwright()
        await self.init_hadles()
        await self.page.goto('https://www.tiket.com/hotel')
        await self.page.get_by_test_id("destination-input-text").click()
        await self.page.get_by_test_id("destination-search-box").click()
        await self.page.get_by_test_id("destination-search-box").fill(keyword)
        await self.page.get_by_test_id("hotel-list-item").first.click()
        await self.page.get_by_test_id("search-button-lp").click()
        datas = []

        def handler(res):
            nonlocal datas
            item = res.url
            datas.append(item)

        self.page.on("response", handler)
        await self.page.wait_for_timeout(500)

        for data in datas:
            if 'https://www.tiket.com/id/hotel/search?' in data:
                id = data.split('&')[2].split('=')[-1]
                type = data.split('&')[3].split('=')[-1]
                q = data.split('&')[4].split('=')[-1]
                res = {
                    'full_link': data,
                    'id': id,
                    'type': type,
                    'q': q,
                }
        await self.close()
        return res


    async def get_link_hard(self, url, index):
        await self.init_playwright()
        await self.init_hadles()
        await self.page.goto(url)

        while True:
            if await self.page.query_selector('.Button_button__20aRx.Button_full_width__ltMfH.Button_size_large__oW7E0.Button_horizontal_padding__7QPqY.Button_variant_primary__PFcuM'):
                await self.page.click('.Button_button__20aRx.Button_full_width__ltMfH.Button_size_large__oW7E0.Button_horizontal_padding__7QPqY.Button_variant_primary__PFcuM')
            else:
                try:
                    index_content = await self.page.query_selector(f'[data-index="{index}"]')
                    if index_content:
                        link = await index_content.query_selector('.ProductCard_container__Ll1Py')
                        link = await link.get_attribute('href')
                        id = link.split('?')[0].split('/')[-1]
                        break
                    else:
                        await self.page.evaluate("window.scrollBy(0, window.innerHeight)")
                        time.sleep(1)
                except:
                    await self.page.reload()

        await self.close()
        return {"id_hotel":id, "link":link}

    async def get_link_range_hard(self, url, start_index, end_index):
        await self.init_playwright()
        await self.init_hadles()
        await self.page.goto(url)

        links = []

        for i in range(start_index, end_index + 1):
            while True:
                if await self.page.query_selector(
                        '.Button_button__20aRx.Button_full_width__ltMfH.Button_size_large__oW7E0.Button_horizontal_padding__7QPqY.Button_variant_primary__PFcuM'):
                    await self.page.click(
                        '.Button_button__20aRx.Button_full_width__ltMfH.Button_size_large__oW7E0.Button_horizontal_padding__7QPqY.Button_variant_primary__PFcuM')
                else:
                    index_content = await self.page.query_selector(f'[data-index="{i}"]')
                    if index_content:
                        link = await index_content.query_selector('.ProductCard_container__Ll1Py')
                        link = await link.get_attribute('href')
                        id = link.split('?')[0].split('/')[-1]
                        links.append({"id_hotel":id, "link":link, 'index':i})
                        break
                    else:
                        await self.page.evaluate("window.scrollBy(0, window.innerHeight)")
                        time.sleep(1)


        await self.close()
        return links

    async def get_image_hard(self, url):
        await self.init_playwright()
        await self.init_hadles()
        await self.page.goto(url)

        await self.page.get_by_text("Lihat semua foto").click()
        conten_img = await self.page.query_selector('.Navigation_tab_wrapper__jaIGw')
        while True:
            try:
                next = await self.page.query_selector('[data-testid="image-gallery-desktop-navigation-button-next"]')
                await next.click()
            except:
                await self.page.get_by_test_id("image-gallery-desktop-button-close").click()
                break

        img = []
        for src in await conten_img.query_selector_all('img'):
            link_src = await src.get_attribute('src')
            if "jpg" in link_src:
                img.append(link_src)


        await self.close()
        return img



    async def get_info_hard(self, url):
        await self.init_playwright()
        await self.init_hadles()
        await self.page.goto(url)

        # head
        title = await self.page.inner_text(
            '//*[@id="__next"]/div[2]/div[5]/div[1]/div/div[1]/div[2]/h1'
        )
        rating = await self.page.inner_text(
            '//*[@id="__next"]/div[2]/div[5]/div[1]/div/div[1]/div[3]/div/p'
        )
        idr = await self.page.inner_text(
            '//*[@id="__next"]/div[2]/div[5]/div[1]/div/div[1]/div[3]/div/p'
        )
        address = await self.page.inner_text(
            'span.LocationSection_address__V8gdU.Text_text__DSnue.Text_variant_lowEmphasis__VihAq.Text_size_b2__y3Q2E'
        )

        # fasilitas
        fasilitas = await self.page.query_selector(
            '.PopularFacilityList_popular_facility_list__HgtQi'
        )
        button = await fasilitas.query_selector('button')
        await button.click()

        fasilitas_populer = [

        ]

        card_fp = await fasilitas.query_selector(
            '.PopularFacilityList_facility_list_container__KfDwC'
        )
        card_fp_list = await card_fp.query_selector_all(
                'span.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_b2__y3Q2E.Text_weight_regular__pJ2W2'
        )

        for fp in card_fp_list:
            fasilitas_populer.append(await fp.inner_text())

        fasilitas_lain = [

        ]

        for card_fl in await fasilitas.query_selector_all(
                '.PopularFacilityList_facility_list_container__KfDwC.PopularFacilityList_with_mobile_padding__QYl_Z'
        ):
            fc = await card_fl.query_selector('h3')
            fl_data = {
                'fasilitas_category': await fc.inner_text(),
            }

            fl_info = [

            ]

            for fl in await card_fl.query_selector_all(
                    'span.Text_text__DSnue.Text_variant_lowEmphasis__VihAq.Text_size_b2__y3Q2E.Text_weight_regular__pJ2W2'
            ):
                fl_info.append(await fl.inner_text())

            fl_data.update(
                {
                    'info_fasilitas': fl_info
                }
            )

            fasilitas_lain.append(fl_data)

        tentang = await self.page.text_content(
            '.AboutAccomodation_description_wrapper__e_lDJ.Text_text__DSnue.Text_size_b2__y3Q2E'
        )
        tentang = tentang.replace('\\n',' ').replace('\n',' ').replace('  ',' ').replace('\n\n',' ')

        akomodasi = await self.page.query_selector(
            '.AccomodationPolicy_accomodation_policy__8yV7u'
        )


        check_in = await akomodasi.query_selector(
            '[data-testid="check-in"]'
        )
        check_in = await check_in.inner_text()
        check_out = await akomodasi.query_selector(
            '[data-testid="check-out"]'
        )
        check_out = await check_out.inner_text()


        kebijakan_lainnya = await akomodasi.query_selector(
            '.AccomodationPolicy_policy_content_text__zJysS'
        )
        kebijakan_lainnya = await kebijakan_lainnya.text_content()
        kebijakan_lainnya.replace('\n', ' ').replace('  ', ' ').replace('\\n',' ').replace('\n\n',' ')



        kamar_information = await self.page.query_selector(
            '.main_room_list_container__8VYFQ'
        )
        room = [

        ]
        for card_room in await kamar_information.query_selector_all('.ListGroup_list_group__Pz9vB'):
            name_room = await card_room.query_selector(
                'h3.RoomCard_title_text__pwoVI.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_b1__bsanT.Text_weight_bold__m4BAY'
            )
            name_room = await name_room.inner_text()

            status_room = await card_room.query_selector(
                'span.RoomCard_cancellation_policy_text__Nb71t.Text_text__DSnue'
            )

            status_room = await status_room.text_content()

            desk_room = [

            ]
            for dr in await card_room.query_selector_all('.RoomCard_list_item__48PpK'):
                txt = await dr.inner_text()
                if '/>' in txt:
                    txt = txt.split('/>')[-1]
                desk_room.append(txt)

            price_room = await card_room.query_selector(
                '.RoomCard_price_footer__AyTiB'
            )
            pr = await price_room.query_selector(
                'p.RoomCard_discount_price__dp1Ag.Text_text__DSnue.Text_variant_alert__7jMF3.Text_size_h3__qFeEO.Text_weight_bold__m4BAY'
            )
            pr = await pr.inner_text()
            room.append(
                {
                "name_room": name_room,
                "status_room": status_room,
                "price_room": pr,
                "desk": desk_room
                }
            )

        await self.page.click(
            '.rr___ReviewWidget-module__button_see_all____NWyR.rr___Text-module__text___Z3QGS.rr___Text-module__variant_activity___cHKEe.rr___Text-module__size_b2___v3SVa.rr___Text-module__weight_bold___E4E4Z'
        )


        result = self.mapping_hotel(
            name=title,
            rating=rating,
            price=idr,
            addres=address,
            popular=fasilitas_populer,
            other=fasilitas_lain,
            check_in=check_in,
            check_out=check_out,
            policy=kebijakan_lainnya,
            about=tentang,
            room=room,
        )



        await self.close()
        return result



    async def review(self, id):
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
            'tiket_currency': 'IDR',
            'userlang': 'id',
            'country_code': 'id',
            'source': 'hotel',
            'HOTEL_UUID': 'xARdY0sxHhTgt_-XbTYl_JdLT5xxH7YDQF7ncdJlVvA',
            '_cfuvid': '1HX9ZyUyNpXJ3QCvkFdJrwtVliEMjDKjM1UFHbchZ20-1712220905826-0.0.1.1-604800000',
            '__cf_bm': 'LloGHEQvRl4wwsYMZgzYmbV5YHzASkGZKM2DopGE9lI-1712308000-1.0.1.1-ot6cg78IQqmzw.5g3U1SgVRiIZhMgXff8HIYGrl1GGxjV4oZJ7VRT3tDVnbs6zcXAGAbkmvJMHVzrxnEZAv11_dziqjdhWX4LjZ75ZrLvx8',
            'cf_clearance': 'OcLnFCiyhIWzDmIbPQyV9aVZQCpqSkMADL.CLuLH.Tk-1712308003-1.0.1.1-TNA28WbFKjsJf9TERbnRC3MZbtNlKzaPFDCPuZQeWxOk3CMw3642I7DUpe.No57LtmKwg0h8cIpeVfFzbxPiLg',
            '_gid': 'GA1.2.1291182083.1712308006',
            'ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%22d2c65d43-b251-5fce-84e7-d6b4eafc90cc%22%2C%22c%22%3A1711087581539%2C%22l%22%3A1712308005893%7D',
            '_gat_UA-22317351-1': '1',
            'ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519': '%7B%22g%22%3A%22ab74fb8f-bd87-4fcf-6574-7ee7c53d083b%22%2C%22e%22%3A1712309808091%2C%22c%22%3A1712308005891%2C%22l%22%3A1712308008091%7D',
            '_tix_logger_correlation_id': '83664dc6-68e6-4574-b088-e0079d1fc94a',
            'AMP_b34eb5901c': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYzA1MTY0Ni05NjljLTQ4ZmEtOTMyOC04NjY2MzViNDczZjUlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDEwNDUxMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTIzMDgwMDU5NjUlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzEyMzA4MDMzMjIxJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E3ODAlN0Q=',
            '_ga_7H6ZDP2ZXG': 'GS1.1.1712308005.26.1.1712308034.31.0.0',
            '_ga': 'GA1.1.977599541.1711087581',
            'amp_b34eb5': 'bc051646-969c-48fa-9328-866635b473f5.NjQxMDQ1MTM=..1hqmo66dg.1hqmo69du.1.8.9',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_gcl_au=1.1.1552196191.1711087581; device_id=bc051646-969c-48fa-9328-866635b473f5; AMP_MKTG_b34eb5901c=JTdCJTdE; _fbp=fb.1.1711087584159.219338993; _tt_enable_cookie=1; _ttp=JnJYlveC8vZmSMe8Vojed-z1KCg; g_state={"i_l":0}; session_access_token=eyJraWQiOiJfVWFrNjM5ekx2WHZ3R05MeDZvaXlFbjM0eG9EeWlJWSJ9.eyJhdWQiOiJ0aWtldC5jb20iLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTcyNzEyNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ.6TcFWIpwmLcqz-d_nJnbs068o5fvOWEWu5rmZWtmY4slnDdhRnZ5hf0eKVJlKE0u; session_refresh_token=eyJraWQiOiJUSmZwelBDak1aUVI2TjEtczRPMy1LaDNUYmdYZXpQZCJ9.eyJhdWQiOiJ0aWtldC5jb20vcnQiLCJzdWIiOiI2NWZkMWZkOWE3N2JjODM4YjRhOWE2NzIiLCJuYmYiOjE3MTEzNDc3MDUsImlzcyI6Imh0dHBzOi8vd3d3LnRpa2V0LmNvbSIsImV4cCI6MTc0MjkwNzcwNSwiZW1haWwiOiJhemFzYXR1c2F0dUBnbWFpbC5jb20ifQ._M3xhOrKGy1dwGak_yjXmlJRMJW1ObwO5Q07an1slb1LfDPPf1s_JMelyX_FSWFU; tiket_currency=IDR; userlang=id; country_code=id; source=hotel; HOTEL_UUID=xARdY0sxHhTgt_-XbTYl_JdLT5xxH7YDQF7ncdJlVvA; _cfuvid=1HX9ZyUyNpXJ3QCvkFdJrwtVliEMjDKjM1UFHbchZ20-1712220905826-0.0.1.1-604800000; __cf_bm=LloGHEQvRl4wwsYMZgzYmbV5YHzASkGZKM2DopGE9lI-1712308000-1.0.1.1-ot6cg78IQqmzw.5g3U1SgVRiIZhMgXff8HIYGrl1GGxjV4oZJ7VRT3tDVnbs6zcXAGAbkmvJMHVzrxnEZAv11_dziqjdhWX4LjZ75ZrLvx8; cf_clearance=OcLnFCiyhIWzDmIbPQyV9aVZQCpqSkMADL.CLuLH.Tk-1712308003-1.0.1.1-TNA28WbFKjsJf9TERbnRC3MZbtNlKzaPFDCPuZQeWxOk3CMw3642I7DUpe.No57LtmKwg0h8cIpeVfFzbxPiLg; _gid=GA1.2.1291182083.1712308006; ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%22d2c65d43-b251-5fce-84e7-d6b4eafc90cc%22%2C%22c%22%3A1711087581539%2C%22l%22%3A1712308005893%7D; _gat_UA-22317351-1=1; ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%22ab74fb8f-bd87-4fcf-6574-7ee7c53d083b%22%2C%22e%22%3A1712309808091%2C%22c%22%3A1712308005891%2C%22l%22%3A1712308008091%7D; _tix_logger_correlation_id=83664dc6-68e6-4574-b088-e0079d1fc94a; AMP_b34eb5901c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJiYzA1MTY0Ni05NjljLTQ4ZmEtOTMyOC04NjY2MzViNDczZjUlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDEwNDUxMyUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTIzMDgwMDU5NjUlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzEyMzA4MDMzMjIxJTJDJTIybGFzdEV2ZW50SWQlMjIlM0E3ODAlN0Q=; _ga_7H6ZDP2ZXG=GS1.1.1712308005.26.1.1712308034.31.0.0; _ga=GA1.1.977599541.1711087581; amp_b34eb5=bc051646-969c-48fa-9328-866635b473f5.NjQxMDQ1MTM=..1hqmo66dg.1hqmo69du.1.8.9',
            'referer': 'https://www.tiket.com/hotel/indonesia/monoloog-hotel-surabaya-609001695617428336?room=1&adult=1&checkin=2024-04-06&checkout=2024-04-07&referrer=https%3A%2F%2Fwww.tiket.com%2Fhotel%2Fsearch%3Froom%3D1%26adult%3D1%26id%3Deast-java-108001534490276152%26type%3DREGION%26q%3DJawa%2520Timur%26checkin%3D2024-03-22%26checkout%3D2024-03-23&utm_page=searchResultPage',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }
        await self.init_playwright()
        await self.context.set_extra_http_headers(headers=headers)
        await self.context.add_cookies(cookies=self.convert_cookies(cookies))
        await self.page.goto(f'https://www.tiket.com/review?product_type=TIXHOTEL&searchType=INVENTORY&inventory_id={id}&reviewSubmitColumn=RATING_SUMMARY')
        last = await self.page.query_selector('[data-testid="last-page-pagination"]')
        last = await last.text_content()
        review_data = []

        def add_unique_dict(array, new_dict):
            for item in array:
                if item == new_dict:
                    return array
            array.append(new_dict)
            return array



        while True:
            try:
                await self.page.wait_for_selector('.ReviewPagination_page_number__WvWjj.ReviewPagination_active__CDDX0')
                activate = await self.page.query_selector(
                    '.ReviewPagination_page_number__WvWjj.ReviewPagination_active__CDDX0'
                )
                activate = await activate.text_content()
            except:
                await self.page.reload()

            if last != activate:
                try:
                    await self.page.wait_for_selector('[data-testid="chevron-right-pagination"]')
                    button = await self.page.query_selector('[data-testid="chevron-right-pagination"]')
                except:
                    await self.page.reload()
                conten_review = await self.page.query_selector('.ReviewCards_review_card_list__FRKNL')
                for card in await conten_review.query_selector_all('.ReviewCard_review_card__vMDRQ'):
                    title = await card.query_selector(
                        'span.ReviewCard_customer_name__1wk6y.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_b3__6n_9j.Text_weight_bold__m4BAY'
                    )
                    title = await title.inner_text()
                    date_rev = await card.query_selector(
                        'span.ReviewCard_date__M5tUJ.Text_text__DSnue.Text_variant_lowEmphasis__VihAq.Text_size_b3__6n_9j'
                    )
                    date_rev = await date_rev.inner_text()
                    rate = await card.query_selector(
                        'span.ReviewCard_user_review__6CKoB.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_h3__qFeEO'
                    )
                    rate = await rate.inner_text()
                    review_item = {
                        'user': title,
                        'review': date_rev,
                        'rating': rate,
                        'page': activate,
                        'last_page': last
                    }
                    add_unique_dict(review_data, review_item)

                await button.click()
            elif last == activate:
                conten_review = await self.page.query_selector('.ReviewCards_review_card_list__FRKNL')
                for card in await conten_review.query_selector_all('.ReviewCard_review_card__vMDRQ'):
                    title = await card.query_selector(
                        'span.ReviewCard_customer_name__1wk6y.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_b3__6n_9j.Text_weight_bold__m4BAY'
                    )
                    title = await title.inner_text()
                    date_rev = await card.query_selector(
                        'span.ReviewCard_date__M5tUJ.Text_text__DSnue.Text_variant_lowEmphasis__VihAq.Text_size_b3__6n_9j'
                    )
                    date_rev = await date_rev.inner_text()
                    rate = await card.query_selector(
                        'span.ReviewCard_user_review__6CKoB.Text_text__DSnue.Text_variant_highEmphasis__ubq3k.Text_size_h3__qFeEO'
                    )
                    rate = await rate.inner_text()

                    review_item = {
                        'user': title,
                        'review': date_rev,
                        'rating': rate,
                        'page': activate,
                        'last_page': last
                    }
                    add_unique_dict(review_data, review_item)

                break
            else:
                await self.page.reload()



        await self.close()
        return review_data