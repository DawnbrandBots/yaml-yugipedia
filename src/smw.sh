#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2024 Kevin Lu
# SPDX-Licence-Identifier: LGPL-3.0-or-later

set -euxo pipefail

CURL_VERSION_STR=$(curl --version | head -n1 | sed 's/(.*//')
# Obtain SMW queries from https://yugipedia.com/wiki/Special:Ask
curl -A "https://github.com/DawnbrandBots/yaml-yugipedia $CURL_VERSION_STR" -vfsSLo unreleased.csv 'https://yugipedia.com/index.php?title=Special:Ask&x=-3Cq-3E-5B-5BCategory%3ADuel-20Monsters-20cards-5D-5D-20-5B-5BOCG-20status%3A%3ANot-20yet-20released-5D-5D-20OR-20-5B-5BCategory%3ADuel-20Monsters-20cards-5D-5D-20-5B-5BTCG-20status%3A%3ANot-20yet-20released-5D-5D-20OR-20-20-3Cq-3E-5B-5BTCG-20Speed-20Duel-20status%3A%3ANot-20yet-20released-5D-5D-3C-2Fq-3E-20-3C-2Fq-3E%2F-3FEnglish-20name%2F-3FOCG-20status%2F-3FOCG-20debut-20date%2F-3FTCG-20status%2F-3FTCG-20debut-20date%2F-3FTCG-20Speed-20Duel-20status%2F-3FTCG-20Speed-20Duel-20debut-20date&format=csv&limit=500&link=all&headers=show&searchlabel=CSV&class=sortable+wikitable+smwtable&sort=Debut+date&order=desc&offset=0&mainlabel=&prettyprint=true&unescape=true'
curl -A "https://github.com/DawnbrandBots/yaml-yugipedia $CURL_VERSION_STR" -vfsSLo unreleased-rush.csv 'https://yugipedia.com/wiki/Special:Ask/format%3Dcsv/limit%3D500/link%3Dall/headers%3Dshow/searchlabel%3DCSV/class%3Dsortable-20wikitable-20smwtable/sort%3DDebut-20date/order%3Ddesc/offset%3D0/-5B-5BRush-20Duel-20status::Not-20yet-20released-5D-5D/-3FEnglish-20name/-3FDebut-20date/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue'
