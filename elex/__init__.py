import os
import requests
import tempfile

from cachecontrol import CacheControl
from cachecontrol.caches import FileCache
from elex.cachecontrol_heuristics import EtagOnlyCache

__version__ = "2.4.4"
_DEFAULT_CACHE_DIRECTORY = os.path.join(tempfile.gettempdir(), "elex-cache")

API_KEY = os.environ.get("AP_API_KEY", None)

API_VERSION = os.environ.get("AP_API_VERSION", "v3")
BASE_URL = os.environ.get(
    "AP_API_BASE_URL", "https://api.ap.org/{0}".format(API_VERSION)
)
CACHE_DIRECTORY = os.environ.get("ELEX_CACHE_DIRECTORY", _DEFAULT_CACHE_DIRECTORY)

session = requests.session()

# starting from v3 api key is passed in the header.
session.headers.update({"Accept-Encoding": "gzip", "x-api-key": API_KEY})

cache = CacheControl(
    session, cache=FileCache(CACHE_DIRECTORY), heuristic=EtagOnlyCache()
)
