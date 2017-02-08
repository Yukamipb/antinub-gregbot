'''
Bot settings for antinub-gregbot project.

At minimum you will need to add your bot's oauth in TOKEN and your discord user
ID in OWNER_ID so the bot only listens to you for volatile commands.
'''
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
LOG_PATH = os.path.join(PROJECT_ROOT, 'log')

# The token for the bot, taken from the discord application page
TOKEN = 'MjQ1NTE4MjczODI1NzM0NjU2.CwNQOQ.rnUr7dBI1KYGuxc0u7OAEDyR7BQ'
# List of command prefixes the bot will pick up on in addition to whenever
# it is mentioned (can be left empty to only listen for mentions)
COMMAND_PREFIXES = ['~']
# The user ID of the person the bot should listen to for sensitive commands
OWNER_ID = '90446176968507392'
ADMINS = []

# Extremely verbose logging when true.
DEBUG = False

STARTUP_EXTENSIONS = [
    '_test_cog',
    'fun',
    'jabber',
    # 'killmails',
    'timerboard'
]


# EXTENSION SPECIFIC SETTINGS

KILLMAILS = {
    # If you have difficulties with IPv6 you may need to set this to True
    'force_ipv4': True,

    'redisQ_url':   'http://redisq.zkillboard.com/listen.php',
    'channel_id':   '244849123759489024',
    # Corps you wish to track
    # e.g. '98388312': 100, posts Pandemic Horde Inc. kills/losses
    # as long as they are worth more than 100 million isk
    'corp_ids': {
        '98199571': 0,  # [A-NI]
        '98388312': 100,  # [THXFC]
    },
    # In millions of isk, all losses above this values will be posted
    # Set to 0 to disable posting of non-corp losses regardless of value
    'others_value':  1,
}

JABBER = {
    'channel':      '244849123759489024',
    'servers': [
        # {
        #     'jabber_id':    'ura-a-ni-cheleyl@redalliance.pw',
        #     'password':     'Th5YxHpelxHpztwLDFVs',
        #     'relay_from':   [
        #         'fleetalert@redalliance.pw',
        #         'ura-a-ni-zyphore@redalliance.pw']
        # },
        # {
        #     'jabber_id':    'Cheleyl@coalition.redalliance.pw',
        #     'password':     'EhQPsv2ayXv4DgbsJSBP',
        #     'relay_from':   ['angel_cartel@coalition.redalliance.pw']
        # }
    ],
}
