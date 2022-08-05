# SPDX-FileCopyrightText: © 2022 Kevin Lu
# SPDX-Licence-Identifier: LGPL-3.0-or-later
import random
import sys
from time import sleep

import httpx
from ruamel.yaml import YAML

from utils import download


def main():
    with httpx.Client(http2=True) as client:
        yaml = YAML()
        url = "https://yugipedia.com/api.php?action=query&redirects=true&generator=categorymembers&prop=revisions&rvprop=content&format=json&formatversion=2&gcmtitle=Category:Duel%20Monsters%20cards&gcmlimit=50"
        if len(sys.argv) > 1:
            gcmcontinue = sys.argv[1]
        else:
            gcmcontinue = download(client, yaml, "gcmcontinue", url)
        while gcmcontinue is not None:
            print(f"gcmcontinue = {gcmcontinue}", flush=True)
            sleep(random.uniform(1, 2))
            gcmurl = f"{url}&gcmcontinue={gcmcontinue}"
            gcmcontinue = download(client, yaml, "gcmcontinue", gcmurl)


if __name__ == "__main__":
    main()
