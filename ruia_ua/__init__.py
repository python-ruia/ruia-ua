#!/usr/bin/env python
"""
 Created by howie.hu at 2018/9/22.
"""

import os
import random

import aiofiles

from ruia import Middleware

__version__ = "0.0.1"


async def get_random_user_agent() -> str:
    """
    Get a random user agent string.
    :return: Random user agent string.
    """
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    return random.choice(await _get_data('./user_agents.txt', USER_AGENT))


async def _get_data(filename: str, default: str) -> list:
    """
    Get data from all user_agents
    :param filename: filename
    :param default: default value
    :return: data
    """
    root_folder = os.path.dirname(__file__)
    user_agents_file = os.path.join(root_folder, filename)
    try:
        async with aiofiles.open(user_agents_file, mode='r') as f:
            data = [_.strip() for _ in await f.readlines()]
    except:
        data = [default]
    return data


middleware = Middleware()


@middleware.request
async def add_random_ua(request):
    ua = await get_random_user_agent()
    if request.headers:
        request.headers.update({'User-Agent': ua})
    else:
        request.headers = {
            'User-Agent': ua
        }