import requests as r


def youtubeSearch(query):
    data = {
        "context": {
            "client": {
                "hl": "es-419",
                "gl": "MX",
                "remoteHost": "",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36,gzip(gfe)",  # noqa
                "clientName": "WEB_REMIX",
                "clientVersion": "1.20240103.01.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://music.youtube.com/",
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CJTa96wGEKXC_hIQ9fmvBRCp968FEL6KsAUQiIewBRDamLAFEOvo_hIQmvCvBRDh8q8FEMn3rwUQ6sOvBRCooLAFEKuCsAUQzK7-EhD8hbAFEJmksAUQnouwBRC4i64FEK7U_hIQ7qKwBRDT4a8FEKWQsAUQ_bj9EhDnhv8SEKaBsAUQqKGwBRC3768FEJj8_hIQvPmvBRC9tq4FEIjjrwUQ57qvBRDZya8FEMeDsAUQjaKwBRCZlLAFENCNsAUQl__-EhDks_4SELfq_hIQzZWwBRC9mbAFEOuTrgUQ3ej-EhCigbAFELedsAUQrLevBRComrAFEL75rwUQzN-uBRDViLAFEOmMsAUQ25ywBQ%3D%3D",  # noqa
                    "coldConfigData": "CJTa96wGEO26rQUQxYWuBRDrk64FEL22rgUQ2O6uBRCkxa8FEJburwUQv4KwBRCah7AFEL6KsAUQpZCwBRC-lLAFEJOWsAUQnZmwBRDbnLAFELedsAUQt56wBRCooLAFELSgsAUQ_aCwBRDyobAFEI2isAUQqqKwBRDuorAFEJmksAUQgaawBRoyQU9qRm94MmJTMmNCNDlJWGhBWTg0M1JMV21jRm8xU1JmQ1FoVHNsQ0w5WFd2YkNXRkEiMkFPakZveDJiUzJjQjQ5SVhoQVk4NDNSTFdtY0ZvMVNSZkNRaFRzbENMOVhXdmJDV0ZBKkhDQU1TTWcwVGdwYW9BczRUcGhfWEVJOFoxUUM3SnQ4RXl3SVZIWktDMEF6aGpRV3R5QWFRMlFTZjBjd0wyemphNUFYekk0VlA%3D",  # noqa
                    "coldHashData": "CJTa96wGEhMyNjQ4Mjg0MzQ5NTkwMjk2Njg1GJTa96wGMjJBT2pGb3gyYlMyY0I0OUlYaEFZODQzUkxXbWNGbzFTUmZDUWhUc2xDTDlYV3ZiQ1dGQToyQU9qRm94MmJTMmNCNDlJWGhBWTg0M1JMV21jRm8xU1JmQ1FoVHNsQ0w5WFd2YkNXRkFCSENBTVNNZzBUZ3Bhb0FzNFRwaF9YRUk4WjFRQzdKdDhFeXdJVkhaS0MwQXpoalFXdHlBYVEyUVNmMGN3TDJ6amE1QVh6STRWUA%3D%3D",  # noqa
                    "hotHashData": "CJTa96wGEhQxMjE5ODg4MTg5ODg0NTI2NTc4MBiU2vesBiiU5PwSKNyT_RIoxrL9EiiqtP0SKJ6R_hIomq3-EijIyv4SKN3O_hIoqOH-EijC7v4SKKj8_hIotfz-Eiid_f4SKMX-_hIol__-EijIg_8SKNeE_xIoq4j_EijBiP8SKMOI_xIoxoj_Eij-iP8SKJuJ_xIomYr_EjIyQU9qRm94MmJTMmNCNDlJWGhBWTg0M1JMV21jRm8xU1JmQ1FoVHNsQ0w5WFd2YkNXRkE6MkFPakZveDJiUzJjQjQ5SVhoQVk4NDNSTFdtY0ZvMVNSZkNRaFRzbENMOVhXdmJDV0ZBQkBDQU1TS2cwSTJJXzVGY29BcURuQUVlOElteFJvRlJDTjRzME1pLTRCOGVBT3RZQUV6TG5MQ19OV1JZN3NCUT09",  # noqa
                },
                "browserName": "Chrome",
                "browserVersion": "120.0.6099.71",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",  # noqa
                "deviceExperimentId": "ChxOek15TWpJMk9USXpPVGMyTlRnMk9UTXlPQT09EJTa96wGGJTa96wG",  # noqa
                "screenWidthPoints": 767,
                "screenHeightPoints": 778,
                "screenPixelDensity": 1,
                "screenDensityFloat": 1.25,
                "utcOffsetMinutes": -360,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "America/Mexico_City",
                "musicAppInfo": {
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_UNKNOWN",  # noqa
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "storeDigitalGoodsApiSupportStatus": {
                        "playStoreDigitalGoodsApiSupportStatus": "DIGITAL_GOODS_API_SUPPORT_STATUS_UNSUPPORTED",  # noqa
                    },
                },
            },
            "user": {
                "lockedSafetyMode": False,
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": [],
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1704848665222",
                    },
                    {
                        "key": "flash",
                        "value": "0",
                    },
                    {
                        "key": "frm",
                        "value": "0",
                    },
                    {
                        "key": "u_tz",
                        "value": "-360",
                    },
                    {
                        "key": "u_his",
                        "value": "2",
                    },
                    {
                        "key": "u_h",
                        "value": "864",
                    },
                    {
                        "key": "u_w",
                        "value": "1536",
                    },
                    {
                        "key": "u_ah",
                        "value": "864",
                    },
                    {
                        "key": "u_aw",
                        "value": "1536",
                    },
                    {
                        "key": "u_cd",
                        "value": "24",
                    },
                    {
                        "key": "bc",
                        "value": "31",
                    },
                    {
                        "key": "bih",
                        "value": "778",
                    },
                    {
                        "key": "biw",
                        "value": "755",
                    },
                    {
                        "key": "brdim",
                        "value": "761,0,761,0,1536,0,782,871,767,778",
                    },
                    {
                        "key": "vis",
                        "value": "1",
                    },
                    {
                        "key": "wgl",
                        "value": "true",
                    },
                    {
                        "key": "ca_type",
                        "value": "image",
                    },
                ],
                "bid": "ANyPxKrVqXXKA4cnW5r09Br-WD3H9zG9fZI82BzGM-58_5oEBvf9RVgKPv-1GhC34urzoIP85HxU7hGx8BU3uGUi7FOIzd8YlQ",  # noqa
            },
        },
        "query": query,
    }
    headers = {
        "Host": "music.youtube.com",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
        "Sec-Ch-Ua-Arch": '""',
        "Sec-Ch-Ua-Platform-Version": '""',
        "Sec-Ch-Ua-Wow64": "?0",
        "Sec-Ch-Ua-Model": '""',
        "Sec-Ch-Ua-Bitness": '""',
        "Sec-Ch-Ua-Platform": '"Windows"',
        "X-Youtube-Bootstrap-Logged-In": "false",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",  # noqa
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Full-Version": '""',
        "X-Youtube-Client-Name": "67",
        "X-Youtube-Client-Version": "1.20240103.01.00",
        "X-Goog-Visitor-Id": "",
        "Accept": "*/*",
        "Origin": "https://music.youtube.com",
        "X-Client-Data": "",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "same-origin",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://music.youtube.com/",
        "Accept-Language": "es-419,es;q=0.9",
        "Priority": "u=1, i",
    }

    params = {
        "key": "AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30",
        "prettyPrint": "false",
    }

    response = r.post(
        "https://music.youtube.com/youtubei/v1/search",
        json=data,
        headers=headers,
        params=params,
    )
    if response.status_code != 200:
        print(response.json())
        return "Error."
    try:
        data = response.json()["contents"]["tabbedSearchResultsRenderer"][
            "tabs"
        ][  # noqa
            0
        ][  # noqa
            "tabRenderer"
        ][
            "content"
        ][
            "sectionListRenderer"
        ][
            "contents"
        ][
            0
        ][
            "musicCardShelfRenderer"
        ]  # noqa
        video = data["title"]["runs"][0]
        author = data["subtitle"]["runs"][2]
        video_id = video["navigationEndpoint"]

        if video_id.get("watchEndpoint"):
            author = author["text"]
            title = video["text"]
            url = f'https://music.youtube.com/watch?v={video_id["watchEndpoint"]["videoId"]}'  # noqa
            return True, {"author": author, "title": title, "url": url}
        else:
            return False, "No hubieron resultados."
    except Exception as e:
        return False, e
