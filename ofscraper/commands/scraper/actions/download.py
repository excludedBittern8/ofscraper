r"""_____  _______         _______  _______  _______  _______  _______  _______  _______ 
(  ___  )(  ____ \       (  ____ \(  ____ \(  ____ )(  ___  )(  ____ )(  ____ \(  ____ )
| (   ) || (    \/       | (    \/| (    \/| (    )|| (   ) || (    )|| (    \/| (    )|
| |   | || (__     _____ | (_____ | |      | (____)|| (___) || (____)|| (__    | (____)|
| |   | ||  __)   (_____)(_____  )| |      |     __)|  ___  ||  _____)|  __)   |     __)
| |   | || (                   ) || |      | (\ (   | (   ) || (      | (      | (\ (   
| (___) || )             /\____) || (____/\| ) \ \__| )   ( || )      | (____/\| ) \ \__
(_______)|/              \_______)(_______/|/   \__/|/     \||/       (_______/|/   \__/
"""

import logging
import time

import ofscraper.api.profile as profile
import ofscraper.classes.models as models
import ofscraper.classes.placeholder as placeholder
import ofscraper.commands.scraper.post as OF
import ofscraper.download.download as download
import ofscraper.models.selector as userselector
import ofscraper.utils.constants as constants
import ofscraper.utils.live.live as progress_utils

log = logging.getLogger("shared")


download_str= "Performing Downloading Action on {name}"




def downloader(ele=None,posts=None,media=None,**kwargs):
    model_id = ele.id
    username = ele.name
    avatar = ele.avatar
    progress_utils.update_activity_task(description=download_str.format(name=username))
    logging.getLogger("shared_other").warning(download_str.format(name=username))
    if constants.getattr("SHOW_AVATAR") and avatar:
        log.warning(f"Avatar : {avatar}")
    download.download_process(username, model_id, media, posts=posts)




def scrape_paid_all(user_dict=None):
    user_dict = OF.process_all_paid()
    oldUsers = userselector.get_ALL_SUBS_DICT()
    length = len(list(user_dict.keys()))
    for count, value in enumerate(user_dict.values()):
        model_id = value["model_id"]
        username = value["username"]
        posts = value["posts"]
        medias = value["medias"]
        log.warning(
            f"\[{model_id}_{username}] Downloading Progress :{count+1}/{length} models "
        )
        userselector.set_ALL_SUBS_DICTVManger(
            {username: models.Model(profile.scrape_profile(model_id))}
        )
        download.download_process(username, model_id, medias, posts=posts)
    # restore og users
    userselector.set_ALL_SUBS_DICT(oldUsers)






def unique_name_warning():
    if not placeholder.check_uniquename():
        log.warning(
            "[red]Warning: Your generated filenames may not be unique\n \
            https://of-scraper.gitbook.io/of-scraper/config-options/customizing-save-path#warning[/red]      \
            "
        )
        time.sleep(constants.getattr("LOG_DISPLAY_TIMEOUT") * 3)
