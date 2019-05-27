import requests, urllib.parse, os
import logging, json

WEBEXTEAMKEY = "NGUwYzQwNGItNTFmYS00MTM1LWFmZTMtMTEwZmRlOTRmMjEwOTliNjM3ZWItMGZl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
ROOM_ID = "Y2lzY29zcGFyazovL3VzL1JPT00vZTI2M2M0MDAtN2NkOC0xMWU5LThjMmUtNjFjYWRjMjgxNjNi"
WEBEXTEAMAPIURL = "https://api.ciscospark.com/v1/"

proxies = None


def make_request(url_ext, method, post_data=""):
    url = WEBEXTEAMAPIURL + url_ext
    headers = {
        "Authorization": "Bearer " + WEBEXTEAMKEY,
        "Content-Type": "application/json"
    }
    print("here")
    # headers = json.dumps(headers_obj)
    if method == "POST":
        print("here POST")
        if proxies:
            resp = requests.post(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.post(url, data=post_data, headers=headers)
            print(resp)
        if int(resp.status_code / 100) == 2:
            return resp.json()
        return False
    if method == "GET":
        if post_data:
            parameters = urllib.parse.urlencode(post_data)
            url = url + "?" + parameters

        if proxies:
            resp = requests.get(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.get(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            return resp.json()
        return False
    if method == "PUT":
        if proxies:
            resp = requests.put(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.put(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            return True
        return False
    if method == "DELETE":
        if proxies:
            resp = requests.delete(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.delete(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            logger.info("DELETE", url, resp)
            return True
    return False


def sent_notification(msg):
    data = {
        "roomId": ROOM_ID,
        "markdown": msg
    }

    try:
        rep = make_request("messages", "POST", json.dumps(data))

    except Exception as e:
        pass
