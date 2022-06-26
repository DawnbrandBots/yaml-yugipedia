import random
import sys
from time import sleep
from typing import Optional

import httpx
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString


def get_retry(client: httpx.Client, url: str) -> httpx.Response:
    for retry in range(5):
        try:
            return client.get(url, follow_redirects=True)
        except httpx.RequestError as e:
            print(f"TRY {retry}\t{e}\t{url}", flush=True)
            sleep(random.uniform(1 + retry, 2 + retry))


def download(client: httpx.Client, yaml: YAML, url: str) -> Optional[str]:
    response = client.get(url, follow_redirects=True)
    response.raise_for_status()
    result = response.json()
    if not result.get("batchcomplete"):
        print(f"batchcomplete != true | {url}", flush=True)
    gcmcontinue = result["continue"]["gcmcontinue"] if result.get("continue") else None
    for page in result["query"]["pages"]:
        pageid = page["pageid"]
        n_revisions = len(page["revisions"])
        contentformat = page["revisions"][0]["contentformat"]
        contentmodel = page["revisions"][0]["contentmodel"]
        if n_revisions != 1:
            print(f"{n_revisions} revisions | {pageid} | {url}", flush=True)
        if contentformat != "text/x-wiki":
            print(f"contentformat = {contentformat} | {pageid} | {url}", flush=True)
        if contentmodel != "wikitext":
            print(f"contentmodel = {contentmodel} | {pageid} | {url}", flush=True)
        with open(f"{pageid}.yaml", mode="w", encoding="utf-8") as out:
            yaml.dump({
                "title": page["title"],
                "wikitext": LiteralScalarString(page["revisions"][0]["content"])
            }, out)
    return gcmcontinue


def main():
    with httpx.Client(http2=True) as client:
        yaml = YAML()
        url = "https://yugipedia.com/api.php?action=query&redirects=true&generator=categorymembers&prop=revisions&rvprop=content&format=json&formatversion=2&gcmtitle=Category:Duel%20Monsters%20cards&gcmlimit=50"
        if len(sys.argv) > 1:
            gcmcontinue = sys.argv[1]
        else:
            gcmcontinue = download(client, yaml, url)
        while gcmcontinue is not None:
            print(f"gcmcontinue = {gcmcontinue}", flush=True)
            sleep(random.uniform(1, 2))
            gcmurl = f"{url}&gcmcontinue={gcmcontinue}"
            gcmcontinue = download(client, yaml, gcmurl)


if __name__ == "__main__":
    main()
