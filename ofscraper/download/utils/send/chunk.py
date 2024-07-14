import pathlib

import ofscraper.download.utils.globals as common_globals
import ofscraper.utils.constants as constants
from ofscraper.utils.logs.helpers import getNumber
from ofscraper.download.utils.log import get_medialog



def send_chunk_msg(ele, total, placeholderObj):
    msg = f"{get_medialog(ele)} Download Progress:{(pathlib.Path(placeholderObj.tempfilepath).absolute().stat().st_size)}/{total}"
    if constants.getattr("SHOW_DL_CHUNKS"):
        common_globals.log.log(
            getNumber(constants.getattr("SHOW_DL_CHUNKS_LEVEL")), msg
        )
    else:
        common_globals.log.trace(msg)
