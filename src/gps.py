import gpsd # pip3 install gpsd-py3
import logging
from retrying import retry # pip3 install retrying

class Gps():
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel("DEBUG")

        self.__connect()

    def get_pos_bearing(self):
        # Get gps position
        packet = gpsd.get_current()

        # See the inline docs for GpsResponse for the available data: https://github.com/MartijnBraam/gpsd-py3/blob/master/DOCS.md
        try:
            return packet.position() + (packet.track(),)
        except:
            return None

    @retry(wait_fixed=1000)
    def __connect(self):
        # TODO: logging
        self.__logger.debug("Going to connect to gpsd")

        # Connect to the local gpsd
        #gpsd.connect()

        # Connect somewhere else
        gpsd.connect(host="127.0.0.1", port=55555)
