import random
import uuid
#from .ip_rand import get_random_ip
DELIMITER = "\x1e"

# Generate random IP between range 13.104.0.0/14 
# f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
# FORWARDED_IP = get_random_ip() 

HEADERS = {
    "host": "sydney.bing.com",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "accept-encoding": "gzip, deflate, br, zstd",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    # "x-forwarded-for": FORWARDED_IP,
    "origin": "https://www.bing.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057",
}

HEADERS_INIT_CONVER = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.bing.com/search',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"123.0.2420.53"',
    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="123.0.2420.53", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.59"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-ms-gec-version': '1-123.0.2420.53',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'x-edge-shopping-flag': '1',
    'x-ms-client-request-id': str(uuid.uuid4()),
    'x-ms-useragent': 'azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.12.3 OS/Windows',
    # "x-forwarded-for": FORWARDED_IP,
}



HEADER_IMG_UPLOAD = {
    "sec-ch-ua": '"Not)A;Brand";v="24", "Microsoft Edge";v="116", "Chromium";v="116",',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0",
    'referer': 'https://www.bing.com/search?q=Bing+AI',
    # "x-forwarded-for": FORWARDED_IP,
}
