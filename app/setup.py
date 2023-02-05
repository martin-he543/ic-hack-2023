from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(name="tuz", version="1.0.0", packages=["tuz"], install_requires=required)

# POST create account
# name
# default_adress {dict}
# dietary {dict}

# return account_id

# POST create event
# name
# admin account_id [arr]
# guests account_ids [arr]
# address {dict}
# time {dict}
#
# playlist_name
# ?? credentials ??
# ?? spotify_username ??

# return event_id


# ? POST edit account

# GET all messages for 1 event
#   event_id

# POST message
#   event_id
#   account_id
#   message_text
#   datetime

# POST goods_contribution
#   account_id
#   good_str (str)
#   good_val (float)

#
# POST money_contribution:
#   account_id
#   money (float)

# GET list_good_countributions
#   event_id
#   account_id (optional)
#

# GET event
#   event_id

# GET account
#   account_id

# GET spotify_search
# search_string
# event_id -> client_id, client_secret

# GET playlist_gen
# num of songs
# seed_genre (optional)
# target dance (optional)

# more spotify stuff

# return dict
