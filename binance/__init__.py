"""An unofficial Python wrapper for the Binance exchange API v3

.. moduleauthor:: Sam McHardy

"""

__version__ = "1.0.17"

from binance.binance.client import Client, AsyncClient  # noqa
from binance.binance.depthcache import DepthCacheManager, OptionsDepthCacheManager, ThreadedDepthCacheManager  # noqa
from binance.binance.streams import BinanceSocketManager, ThreadedWebsocketManager  # noqa
