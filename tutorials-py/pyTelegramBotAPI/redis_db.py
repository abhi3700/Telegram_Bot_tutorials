"""
	This file - `db.py` is to check the database data.

	Reference: https://devcenter.heroku.com/articles/heroku-redis#connecting-in-python
"""

import redis
import datetime
import json
from input import REDIS_URL


# ---------------------------------------------------------------
# define Redis database
r = redis.from_url(REDIS_URL, ssl_cert_reqs=None)		# ssl_verify to false

# ---------------set data-----------------------------------------


# ---------------get data-----------------------------------------
print(r.keys())