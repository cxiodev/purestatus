from vk import VK
from vk.utils import TaskManager as ApplicationManager  # don`t ask why

from pytz import timezone

import asyncio
import datetime
import utils


try:
    from loguru import logger
    logger.debug('Loguru found! Using fast logs...')
except ModuleNotFoundError:
    import logging
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()
    logger.debug('Loguru not found. Using bad slow logging...')

try:
    import ujson as json_parser
    logger.debug('UJSON found! Using fast loading...')
except ModuleNotFoundError:
    import json as json_parser
    logger.debug('UJSON not found. Using slow loading...')


with open('configuration.json') as fh:
    config = json_parser.load(fh)

application = VK(access_token=config['token'])


async def fetch_profile_info(vk: VK):
    return await vk.api_request('account.getProfileInfo')


async def set_online(vk: VK):
    if config['lifetime_online_settings']['voip'] is True:
        return await vk.api_request('account.setOnline', {'voip': 1})
    else:
        return await vk.api_request('account.setOnline', {'voip': 0})


async def set_status(vk: VK, status: str):
    return await vk.api_request('account.saveProfileInfo', {'status': status})


async def application_cycle():
    data = await fetch_profile_info(application)
    logger.info(f'Authorized to vk.com/{data["screen_name"]}')
    pattern = config['status_pattern']
    while True:
        _pattern = pattern.replace('%current_time%', str(datetime.datetime.now().astimezone(timezone(config['timezone'])).strftime(config['time_pattern'])))
        _pattern = _pattern.replace('%emoji_time%', utils.digits_to_emojis(str(datetime.datetime.now().astimezone(timezone(config['timezone'])).strftime(config['time_pattern']))))
        await asyncio.sleep(0.2)
        if (await fetch_profile_info(application))["status"] != _pattern:
            logger.debug("Changing status...")
            await set_status(application, _pattern)
            logger.debug('Status changed!')
        if config['lifetime_online_settings']['enabled'] is True:
            await set_online(application)
        await asyncio.sleep(0.5)

if __name__ == '__main__':
    application_manager = ApplicationManager(application.loop)
    application_manager.add_task(application_cycle)
    application_manager.run()
