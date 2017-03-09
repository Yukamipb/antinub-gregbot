'''
Entry point for antinub-gregbot project.

Configures logging, loads startup extensions and starts the bot.
'''
import logging
import logging.config
from logging.handlers import RotatingFileHandler

import discord.ext.commands as commands

from core.configbuilder import ConfigYAML


async def load_extensions(bot):
    'Load the startup extensions'
    logger = logging.getLogger(__name__)
    logger.info('Loading extensions')
    try:
        bot.load_extension('core.control')
    except Exception as exc:
        logger.exception('Failed to load core extension, shutting down.')
        await bot.logout()
        raise exc
    logger.info('Successfully loaded extension: control')

    for ext in bot.config['bot']['startup_extensions']:
        libname = 'ext.{}'.format(ext)
        if libname not in bot.extensions:
            try:
                bot.load_extension(libname)
                logger.info('Successfully loaded extension: %s', ext)
            except ImportError:
                logger.warning('Extension not found: %s', ext)
            except Exception as exc:
                logger.exception('Failed to load extension: %s', ext)
                raise exc
        else:
            logger.warning('Extension with same name already loaded: %s', ext)


async def finish_startup(bot):
    '''Wait until bot is ready, then load startup extensions'''
    logger = logging.getLogger(__name__)
    await bot.wait_until_ready()

    logger.info('Logged in as %s, id: %s', bot.user.name, bot.user.id)
    await load_extensions(bot)


def configure_logging(config, debug):
    '''Configure logging from dictionary and rollover RotatingFileHandlers'''
    logging.config.dictConfig(config)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG if debug else logging.INFO)
    for handler in root_logger.handlers:
        if isinstance(handler, RotatingFileHandler):
            handler.doRollover()


def start_bot(config):
    '''Configure logging and start the bot, load start extensions when ready'''
    configure_logging(config['logging'], config['bot']['debug'])
    logger = logging.getLogger(__name__)
    logger.info('Starting up bot')
    bot = commands.Bot(
        commands.when_mentioned_or(*config['bot']['command_prefixes']),
        pm_help=True)

    bot.config = config
    fut = bot.loop.create_task(finish_startup(bot))
    bot.run(bot.config['bot']['token'])


if __name__ == '__main__':
    start_bot(ConfigYAML('config.yaml'))
