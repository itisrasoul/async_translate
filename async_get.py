import aiohttp
import asyncio
from aiohttp.client_exceptions import ContentTypeError
from aiohttp_socks import ProxyConnector
from logger import logger, config_logger
from config import PROXY, REQUEST_HEADERS

config_logger("./log.log")

async def get_url(url, session, mode):
    async with session.get(url=url) as response:
        if mode == 'json':
            try:
                return dict(url=url, response=await response.json())
            except ContentTypeError:
                logger(f"async_get.py: URL {url} returned text/html content instead of JSON.\nResponse Code: {response.status}", 'error')
        elif mode == 'text':
            return dict(url=url, response=await response.text())


async def async_caller(url_list, mode, async_limit):
    if PROXY == True:
        connector = ProxyConnector(host="127.0.0.1", port=9050, limit=async_limit)
    else:
        connector = aiohttp.TCPConnector(limit=async_limit)
    async with aiohttp.ClientSession(connector=connector, headers=REQUEST_HEADERS) as session:
        results = await asyncio.gather(*[
            get_url(url, session, mode) for url in url_list
        ])
        return results


def main(url_list, async_limit, mode='json'):
    loop = asyncio.new_event_loop()
    results = loop.run_until_complete(async_caller(url_list, mode, async_limit))
    return results
