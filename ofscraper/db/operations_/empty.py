r"""
                                                             
 _______  _______         _______  _______  _______  _______  _______  _______  _______ 
(  ___  )(  ____ \       (  ____ \(  ____ \(  ____ )(  ___  )(  ____ )(  ____ \(  ____ )
| (   ) || (    \/       | (    \/| (    \/| (    )|| (   ) || (    )|| (    \/| (    )|
| |   | || (__     _____ | (_____ | |      | (____)|| (___) || (____)|| (__    | (____)|
| |   | ||  __)   (_____)(_____  )| |      |     __)|  ___  ||  _____)|  __)   |     __)
| |   | || (                   ) || |      | (\ (   | (   ) || (      | (      | (\ (   
| (___) || )             /\____) || (____/\| ) \ \__| )   ( || )      | (____/\| ) \ \__
(_______)|/              \_______)(_______/|/   \__/|/     \||/       (_______/|/   \__/
                                                                                      
"""

import contextlib
import logging
import sqlite3

from rich.console import Console

import ofscraper.classes.labels as labels_class
import ofscraper.db.operations_.helpers as helpers
import ofscraper.db.operations_.posts as post_
import ofscraper.db.operations_.wrapper as wrapper
import ofscraper.utils.args.accessors.read as read_args
from ofscraper.db.operations_.profile import get_single_model_via_profile

console = Console()
log = logging.getLogger("shared")
postsEmpty = """
SELECT COUNT(*) FROM posts;
"""
mediaEmpty = """
SELECT COUNT(*) FROM medias;
"""
storiesEmpty = """
SELECT COUNT(*) FROM stories;
"""

productsEmpty = """
SELECT COUNT(*) FROM products;
"""
othersEmpty = """
SELECT COUNT(*) FROM others;
"""

messagesEmpty = """
SELECT COUNT(*) FROM messages;
"""


@wrapper.operation_wrapper_async
def empty(conn=None, **kwargs):
  with contextlib.closing(conn.cursor()) as cur:
    # Execute queries for each table and store results in a list
    queries= [postsEmpty,mediaEmpty,storiesEmpty,productsEmpty,othersEmpty,messagesEmpty]
    for query in queries:
      cur.execute(query)
      count = cur.fetchone()
      if dict(count)["COUNT(*)"]>0:
        return False
    return True


