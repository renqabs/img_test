import random
import uuid

DELIMITER = "\x1e"
# Generate random IP between range 13.104.0.0/14
FORWARDED_IP = "52.140.193.137"#f"11.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en-US;q=0.9",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.3 OS/Windows",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "accept": "application/json",
    "accept-language": "en-US;q=0.9",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.3 OS/Windows",
    "x-forwarded-for": FORWARDED_IP,
}

HEADER_IMG_UPLOAD = {
    'referer': 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx',
}
