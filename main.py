import argparse
import asyncio
import json
import traceback
import urllib.request
import emoji
import claude
import sys, os
import re
import httpx
import uuid
import random
sys.path.insert(0, os.path.dirname(__file__))
public_dir = '/public'

from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.constants import HEADERS_INIT_CONVER
from aiohttp import web

def generate_hex_string(length):
    hex_digits = '0123456789ABCDEF'
    return ''.join(random.choice(hex_digits) for _ in range(length))

async def sydney_process_message(user_message, bot_mode, context, _U, KievRPSSecAuth, MUID, VerifyServer, locale, enable_gpt4turbo, imageInput, enableSearch):
    chatbot = None
    cookies = [{'domain': '.bing.com', 'expirationDate': 1740906919.269414, 'hostOnly': False, 'httpOnly': False, 'name': 'SRCHUSR', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'DOB=20240127&T=1706346917000'}, {'domain': '.bing.com', 'hostOnly': False, 'httpOnly': True, 'name': '_Rwho', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': True, 'storeId': None, 'value': 'u=d'}, {'domain': '.bing.com', 'expirationDate': 1706433380.767807, 'hostOnly': False, 'httpOnly': False, 'name': 'GC', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': '1R-7jh-Y_R8nQHg3Z_Dtb-qkVbmoNUVV4AMQHypGRjJtneFEFVrRoH-Czpr0v0RqQXWzSdAgLHjPVPjrTcbKQw'}, {'domain': '.bing.com', 'expirationDate': 1706433388.876986, 'hostOnly': False, 'httpOnly': False, 'name': 'cct', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': '1R-7jh-Y_R8nQHg3Z_Dtb-qkVbmoNUVV4AMQHypGRjIX0pXmlRUC07UEpPklRYncDHrokLCtCButqhO2YV8Vdw'}, {'domain': '.bing.com', 'expirationDate': 1740907000.160599, 'hostOnly': False, 'httpOnly': False, 'name': 'SRCHHPGUSR', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'SRCHLANG=zh-Hans&IG=275D5C2A88DC450E800B085E819BE1DD&PV=15.0.0&BRW=NOTP&BRH=M&CW=771&CH=838&SCW=771&SCH=796&DPR=2.3&UTC=480&DM=0&CIBV=1.1525.2&EXLTT=1&HV=1706346920'}, {'domain': '.bing.com', 'hostOnly': False, 'httpOnly': False, 'name': '_SS', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': True, 'storeId': None, 'value': 'SID=29CEF1E8FBBC6C2B0E5AE5FBFAEA6D73&R=5&RB=0&GB=0&RG=200&RP=0'}, {'domain': '.bing.com', 'hostOnly': False, 'httpOnly': False, 'name': 'ipv6', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': True, 'storeId': None, 'value': 'hit=1706350522305&t=4'}, {'domain': 'www.bing.com', 'hostOnly': True, 'httpOnly': False, 'name': '_U', 'path': '/', 'sameSite': None, 'secure': False, 'session': True, 'storeId': None, 'value': '142356rwetrytuyiuusdhfg'}, {'domain': '.bing.com', 'expirationDate': 1740906917.539745, 'hostOnly': False, 'httpOnly': False, 'name': 'SRCHD', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'AF=PERE'}, {'domain': '.bing.com', 'expirationDate': 1740042916.539708, 'hostOnly': False, 'httpOnly': True, 'name': '_EDGE_V', 'path': '/', 'sameSite': None, 'secure': False, 'session': False, 'storeId': None, 'value': '1'}, {'domain': '.bing.com', 'expirationDate': 1737969319.683836, 'hostOnly': False, 'httpOnly': False, 'name': '_RwBf', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'W=0&r=0&ilt=1&ihpd=0&ispd=1&rc=5&rb=0&gb=0&rg=200&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=1&l=2024-01-27T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0001-01-01T00:00:00.0000000&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2024-01-27T09:15:20.1456077+00:00&rwred=0&wls=&wlb=&wle=&ccp=&lka=0&lkt=0&aad=0&TH='}, {'domain': '.bing.com', 'hostOnly': False, 'httpOnly': True, 'name': '_EDGE_S', 'path': '/', 'sameSite': None, 'secure': False, 'session': True, 'storeId': None, 'value': 'F=1&SID=29CEF1E8FBBC6C2B0E5AE5FBFAEA6D73&mkt=en-us'}, {'domain': 'www.bing.com', 'expirationDate': 1740042988.876902, 'hostOnly': True, 'httpOnly': True, 'name': 'MUIDB', 'path': '/', 'sameSite': None, 'secure': False, 'session': False, 'storeId': None, 'value': '309D53421E37669C02D947511F616732'}, {'domain': '.bing.com', 'expirationDate': 1740906917.539725, 'hostOnly': False, 'httpOnly': True, 'name': 'USRLOC', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'HS=1'}, {'domain': '.bing.com', 'expirationDate': 1740042916.539543, 'hostOnly': False, 'httpOnly': False, 'name': 'MUID', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': '309D53421E37669C02D947511F616732'}, {'domain': '.bing.com', 'expirationDate': 1740906917.539762, 'hostOnly': False, 'httpOnly': False, 'name': 'SRCHUID', 'path': '/', 'sameSite': 'no_restriction', 'secure': True, 'session': False, 'storeId': None, 'value': 'V=2&GUID=51E4EE9A7ACD489DBF5872E85647CA84&dmnchg=1'}]#loaded_cookies
    image_gen_cookie = []
    '''
    if _U:
        image_gen_cookie += [{"name": "_U", "value": _U}]
    if KievRPSSecAuth:
        image_gen_cookie += [{"name": "KievRPSSecAuth", "value": KievRPSSecAuth}]
    cookies = [{"name": "_U", "value": str(uuid.uuid4()).replace('-','')}]
    SRCHHPGUSR = {
                "creative": "cdxtone=Creative&cdxtoneopts=h3imaginative,gencontentv3,nojbfedge",
                "precise": "cdxtone=Precise&cdxtoneopts=h3precise,clgalileo,gencontentv3,nojbfedge",
                "balanced": "cdxtone=Balanced&cdxtoneopts=galileo,fluxhint,glfluxv13,nojbfedge"
                 }
    cookies += [{"name": "SRCHHPGUSR", "value": SRCHHPGUSR[bot_mode]}]
    image_gen_cookie += [{"name": "SRCHHPGUSR", "value": "SRCHLANG=zh-Hans&" + SRCHHPGUSR[bot_mode]}]
    '''
    os.environ['image_gen_cookie'] = json.dumps(image_gen_cookie)
    # Set the maximum number of retries
    max_retries = 5
    for i in range(max_retries + 1):
        #print(cookies)
        if os.environ.get('cookies_captcha_solved'):
            cookies_bot = json.loads(os.environ.get('cookies_captcha_solved'))
        else:
            cookies_bot = cookies
        #print(f"cookies_bot:{cookies_bot}")
        try:
            chatbot = await Chatbot.create(cookies=cookies_bot, proxy=args.proxy, imageInput=imageInput)
            async for _, response in chatbot.ask_stream(prompt=user_message, conversation_style=bot_mode, raw=True,
                                                        webpage_context=context, search_result=enableSearch,
                                                        locale=locale, enable_gpt4turbo=enable_gpt4turbo):
                yield response
            break
        except Exception as e:
            if (
                "Sorry, you need to login first to access this service." in str(e)
                or "ServiceClient failure for DeepLeo" in str(e)
                or "Cannot retrieve user status" in str(e)
                or "Authentication failed" in str(e)
                or "conversationSignature" in str(e)
                or "Unhandled Exception" in str(e)
            ) and i < max_retries:
                print("Retrying...", i + 1, "attempts.")
                await asyncio.sleep(2)
            elif ("User needs to solve CAPTCHA" in str(e)) and i < max_retries:
                if VerifyServer:
                    async with httpx.AsyncClient(
                            proxies=args.proxy or None,
                            timeout=30,
                            headers={"Content-Type": "application/json",
                                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"},
                    ) as client:
                        #print("solve CAPTCHA ...")
                        await asyncio.sleep(random.randint(0,5))
                        response_cap = await client.post(
                            url=VerifyServer,
                            json={"cookies:": ""},
                            follow_redirects=True,
                        )
                        if response_cap.status_code != 200:
                            yield {"type": "error", "error": "solve CAPTCHA Failed"}
                            #print(f"Status code: {response_cap.status_code}")
                            #print(response_cap.url)
                        else:
                            response_cap_cookie_str = response_cap.json()['result']['cookies']
                            cookies_new = [dict(name=item.split("=")[0], value=item.split("=",1)[1]) for item in response_cap_cookie_str.split("; ")]
                            cookies_new = list(filter(lambda d: d.get('name') != '_U', cookies_new)) + [
                                {"name": "_U", "value": [d['value'] for d in cookies if d['name'] == '_U'][0]}]
                            os.environ['cookies_captcha_solved'] = json.dumps(cookies_new)
            else:
                if i == max_retries:
                    print("Failed after", max_retries, "attempts.")
                yield {"type": "error", "error": traceback.format_exc()}
        finally:
            if chatbot:
                await chatbot.close()



async def claude_process_message(context):
    try:
        async for reply in claude_chatbot.ask_stream(context):
            yield {"type": "reply", "text": emoji.emojize(reply, language='alias').strip()}
        yield {"type": "finished"}
    except:
        yield {"type": "error", "error": traceback.format_exc()}


async def http_handler(request):
    file_path = request.path
    if file_path == "/":
        file_path = "/index.html"
    full_path = os.path.realpath('.' + public_dir + file_path)
    if not full_path.startswith(os.path.realpath('.' + public_dir)):
        raise web.HTTPForbidden()
    response = web.FileResponse(full_path)
    response.headers['Cache-Control'] = 'no-store'
    return response


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async def monitor():
        while True:
            if ws.closed:
                task.cancel()
                break
            await asyncio.sleep(0.1)

    async def main_process():
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                request = json.loads(msg.data)
                user_message = request['message']
                context = request['context']
                locale = request['locale']
                enable_gpt4turbo = request['enable_gpt4turbo']
                _U = request.get('_U')
                MUID = request.get('MUID')
                VerifyServer = request.get('VerifyServer')
                enableSearch = request.get('enableSearch')
                KievRPSSecAuth = request.get('KievRPSSecAuth')
                if (request.get('imageInput') is not None) and (len(request.get('imageInput')) > 0):
                    imageInput = request.get('imageInput').split(",")[1]
                else:
                    imageInput = None
                bot_type = request.get("botType", "Sydney")
                bot_mode = request.get("botMode", "creative")
                if bot_type == "Sydney":
                    async for response in sydney_process_message(user_message, bot_mode, context, _U, KievRPSSecAuth, MUID, VerifyServer, locale=locale, enable_gpt4turbo=enable_gpt4turbo, imageInput=imageInput, enableSearch=enableSearch):
                        await ws.send_json(response)
                elif bot_type == "Claude":
                    async for response in claude_process_message(context):
                        await ws.send_json(response)
                else:
                    print(f"Unknown bot type: {bot_type}")

    task = asyncio.ensure_future(main_process())
    monitor_task = asyncio.ensure_future(monitor())
    done, pending = await asyncio.wait([task, monitor_task], return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()

    return ws


async def main(host, port):
    app = web.Application()
    app.router.add_get('/ws/', websocket_handler)
    app.router.add_get('/{tail:.*}', http_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    print(f"Go to http://{host}:{port} to start chatting!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", "-H", help="host:port for the server", default="localhost:65432")
    parser.add_argument("--proxy", "-p", help='proxy address like "http://localhost:7890"',
                        default=urllib.request.getproxies().get('https'))
    args = parser.parse_args()
    print(f"Proxy used: {args.proxy}")

    host, port = args.host.split(":")
    port = int(port)

    if os.path.isfile("cookies.json"):
        with open("cookies.json", 'r') as f:
            loaded_cookies = json.load(f)
        print("Loaded cookies.json")
    else:
        loaded_cookies = []
        print("cookies.json not found")

    claude_chatbot = claude.Chatbot(proxy=args.proxy)
    os.environ['cookies_captcha_solved'] = ""
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(host, port))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
