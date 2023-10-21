# SPDX-FileCopyrightText: © 2022–2023 Kevin Lu
# SPDX-Licence-Identifier: LGPL-3.0-or-later
import logging
from platform import python_version
import random
import sys
from time import sleep

import httpx
from ruamel.yaml import YAML

from utils import download


# User agents containing the substring "python" in any casing are forbidden after 2023-01-28
user_agent = f"https://github.com/DawnbrandBots/yaml-yugipedia httpx/{httpx.__version__} py/{python_version()}"


def skip_condition(page) -> bool:
    return "categories" not in page


def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} <category> <start time: MediaWiki timestamp> [grccontinue]")
    logging.basicConfig(level=logging.INFO)
    with httpx.Client(http2=True, headers={"User-Agent": user_agent}) as client:
        yaml = YAML()
        url = "https://yugipedia.com/api.php?format=json&formatversion=2&action=query&generator=recentchanges&prop=revisions|categories&grctype=new|edit|categorize&grctoponly=true&grclimit=50&grcnamespace=0&grcdir=newer&rvprop=content&cllimit=max"
        url += f"&clcategories=Category:{sys.argv[1]}"
        url += f"&grcstart={sys.argv[2]}"
        if len(sys.argv) > 3:
            grccontinue = sys.argv[3]
        else:
            grccontinue = download(client, yaml, "grccontinue", url, skip_condition)
        while grccontinue is not None:
            logging.info(f"grccontinue = {grccontinue}")
            sleep(random.uniform(1, 2))
            grcurl = f"{url}&grccontinue={grccontinue}"
            grccontinue = download(client, yaml, "grccontinue", grcurl, skip_condition)


if __name__ == "__main__":
    main()
