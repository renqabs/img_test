import random
import uuid

DELIMITER = "\x1e"


# Generate random IP between range 13.104.0.0/14
FORWARDED_IP = f"2.17.{random.randint(102, 106)}.{random.randint(1, 255)}"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": '"Not_A Brand";v="99", Microsoft Edge";v="115", "Chromium";v="115"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"115.0.1901.170"',
    "sec-ch-ua-full-version-list": '"Chromium";v="115.0.5790.75", "Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="115.0.5790.75"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.0 OS/Win32",
    "Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "Referrer-Policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "authority": "www.bing.com",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="115", "Not A(Brand";v="99", "Microsoft Edge";v="115"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"115.0.1901.170"',
    "sec-ch-ua-full-version-list": '"Chromium";v="115.0.5790.75", "Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="115.0.1901.170"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0",
    "x-edge-shopping-flag": "1",
    "Referrer-Policy": "origin-when-cross-origin",
    "Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "x-forwarded-for": FORWARDED_IP,
}

HEADER_IMG_UPLOAD = {
    'referer': 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx',
}
