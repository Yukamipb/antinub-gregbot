'''
Utility functions made for antinub-gregbot project.
'''
import core.config as config


def paginate(string, pref='```\n', aff='```', max_length=2000, sep='\n'):
    'Chops a string into even chunks of max_length around the given separator'
    max_size = max_length - len(pref) - len(aff)

    str_length = len(string)
    if str_length <= max_size:
        return [pref + string + aff]
    else:
        split = string.rfind(sep, 0, max_size) + 1
        if split:
            return ([pref + string[:split] + aff]
                    + paginate(string[split:], pref, aff, max_length, sep))
        else:
            return ([pref + string[:max_size] + aff]
                    + paginate(string[max_size:], pref, aff, max_length, sep))


async def notify_admins(bot, messages):
    'Send message to the private channel of each admin'
    recipients = set(config.ADMINS)
    recipients.add(config.OWNER_ID)  # Include owner if not already there
    for user_id in recipients:
        channel = await bot.get_user_info(user_id)
        for message in messages:
            await bot.send_message(channel, message)
