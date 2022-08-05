# SPDX-FileCopyrightText: © 2022 Kevin Lu
# SPDX-Licence-Identifier: LGPL-3.0-or-later
import random
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


def download(client: httpx.Client, yaml: YAML, continue_key: str, url: str, skip_condition=None) -> Optional[str]:
    response = client.get(url, follow_redirects=True)
    response.raise_for_status()
    result = response.json()
    if not result.get("batchcomplete"):
        print(f"batchcomplete != true | {url}", flush=True)
    continue_value = result["continue"][continue_key] if result.get("continue") else None
    if "query" not in result:
        print(f"No results! | {url}", flush=True)
        return
    for page in result["query"]["pages"]:
        if skip_condition is not None and skip_condition(page):
            continue
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
    return continue_value
