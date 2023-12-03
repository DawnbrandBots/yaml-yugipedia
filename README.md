# YAML [Yugipedia](https://yugipedia.com)

[![Update wikitext from Yugipedia with recent changes](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/update.yml/badge.svg)](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/update.yml)

The [YAML Yugi](https://github.com/DawnbrandBots/yaml-yugi) project aims to create a comprehensive, machine-readable,
human-editable database of the _Yu-Gi-Oh! Trading Card Game_ and _Official Card Game_. This is an automatically-updated
collection of wikitexts from Yugipedia of cards for intake and transformation into the final database.

All files under [`/wikitext`](/wikitext) are downloaded using the Mediawiki API and copyright belongs to their original
holders. Any Yugipedia-original content is licensed under [CC BY-SA 4.0](https://yugipedia.com/wiki/Yugipedia:Licensing)
but most card text is &copy; Studio Dice/SHUEISHA, TV TOKYO, KONAMI.

The categories being downloaded are
- [Duel Monsters cards](https://yugipedia.com/wiki/Category:Duel_Monsters_cards)
- [Rush Duel cards](https://yugipedia.com/wiki/Category:Rush_Duel_cards)
- [Skill Cards](https://yugipedia.com/wiki/Category:Skill_Cards)
- [TCG and OCG archetypes](https://yugipedia.com/wiki/Category:TCG_and_OCG_archetypes)
- [Yu-Gi-Oh! Master Duel cards](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Master_Duel_cards)
- [Yu-Gi-Oh! Master Duel Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Master_Duel_Forbidden_%26_Limited_Lists)
- [Tokens](https://yugipedia.com/wiki/Category:Tokens)
- [Cards by Konami index number](https://yugipedia.com/wiki/Category:Cards_by_Konami_index_number)

These categories were downloaded but are not automatically updating.
The Duel Links categories remain damaged since the March 2023 outage and the remaining is no longer needed downstream.
- [Yu-Gi-Oh! Duel Links cards](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_cards): [`/wikitext/duel-links-cards`](/wikitext/duel-links-cards)
- [Yu-Gi-Oh! Duel Links Skills](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_Skills): [`/wikitext/duel-links-skills`](/wikitext/duel-links-skills)
- [OCG Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:OCG_Forbidden_%26_Limited_Lists): [`/wikitext/limit-regulation-ocg`](/wikitext/limit-regulation-ocg)

The remaining files — the actual source code of this stage of the pipeline — are available under the
GNU Lesser General Public License 3.0 or later. See [COPYING](./COPYING) and [COPYING.LESSER](./COPYING.LESSER)
for more details.

## Adding a new category

1. Run the [download workflow](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/download.yml) with the URL-encoded title of the category page without the `Category:` as input, e.g. `Yu-Gi-Oh!_Master_Duel_Forbidden_%26_Limited_Lists`.
1. Add this URL-encoded category title to the [update list](/src/categories.txt) for the saved wikitexts automatically receive new changes via the [update workflow](https://github.com/DawnbrandBots/yaml-yugipedia/blob/master/.github/workflows/update.yml).

You can request to include a category by opening a pull request adding an entry to the [update list](/src/categories.txt).
