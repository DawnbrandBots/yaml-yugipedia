#!/usr/bin/env bash
# SPDX-FileCopyrightText: © 2023 Kevin Lu
# SPDX-Licence-Identifier: LGPL-3.0-or-later

set -euxo pipefail

while read CATEGORY
do
    cd "wikitext/$CATEGORY"
    python3 ../../src/incremental.py "$CATEGORY" "$1"
    cd -
done
