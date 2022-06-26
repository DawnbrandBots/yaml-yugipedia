import random
import sys
from time import sleep

import httpx
from ruamel.yaml import YAML

from utils import download


def skip_condition(page) -> bool:
    return "categories" not in page


def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} <start time: MediaWiki timestamp>")
    with httpx.Client(http2=True) as client:
        yaml = YAML()
        url = "https://yugipedia.com/api.php?format=json&formatversion=2&action=query&generator=recentchanges&prop=revisions|categories&grctype=new|edit|categorize&grctoponly=true&grclimit=50&grcnamespace=0&grcdir=newer&rvprop=content&cllimit=max&clcategories=Category:Duel%20Monsters%20cards"
        url += f"&grcstart={sys.argv[1]}"
        if len(sys.argv) > 2:
            grccontinue = sys.argv[2]
        else:
            grccontinue = download(client, yaml, "grccontinue", url, skip_condition)
        while grccontinue is not None:
            print(f"grccontinue = {grccontinue}", flush=True)
            sleep(random.uniform(1, 2))
            grcurl = f"{url}&grccontinue={grccontinue}"
            grccontinue = download(client, yaml, "grccontinue", grcurl, skip_condition)


if __name__ == "__main__":
    main()
