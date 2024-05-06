# YAML [Yugipedia](https://yugipedia.com)

[![Update wikitext from Yugipedia with recent changes](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/update.yml/badge.svg)](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/update.yml)
[![Lint](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/python.yml/badge.svg)](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/python.yml)

An automatically-updated collection of wikitexts from Yugipedia of cards for intake and transformation into the
[YAML Yugi](https://github.com/DawnbrandBots/yaml-yugi) database. Storing a cache here reduces load on the wiki while
also serving as an external backup of current wiki text. The YAML Yugi project aims to create a comprehensive,
machine-readable, human-editable database of _Yu-Gi-Oh! Trading Card Game_ (TCG), _Official Card Game_ (OCG),
_Master Duel_ video game, _Rush Duel_, and _Speed Duel_.

All files under [`/wikitext`](/wikitext) are downloaded using the Mediawiki API and copyright belongs to their original
holders. Any Yugipedia-original content is licensed under [CC BY-SA 4.0](https://yugipedia.com/wiki/Yugipedia:Licensing)
but most card text is &copy; Studio Dice/SHUEISHA, TV TOKYO, KONAMI.

The remaining files — the actual source code of this stage of the pipeline — are available under the
GNU Lesser General Public License 3.0 or later. See [COPYING](./COPYING) and [COPYING.LESSER](./COPYING.LESSER)
for more details.

## Categories being automatically downloaded
- [Duel Monsters cards](https://yugipedia.com/wiki/Category:Duel_Monsters_cards)
- [Rush Duel cards](https://yugipedia.com/wiki/Category:Rush_Duel_cards)
- [Skill Cards](https://yugipedia.com/wiki/Category:Skill_Cards)
- [TCG and OCG archetypes](https://yugipedia.com/wiki/Category:TCG_and_OCG_archetypes)
- [Yu-Gi-Oh! Master Duel cards](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Master_Duel_cards)
- [Yu-Gi-Oh! Master Duel Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Master_Duel_Forbidden_%26_Limited_Lists)
- [Tokens](https://yugipedia.com/wiki/Category:Tokens)
- [Cards by Konami index number](https://yugipedia.com/wiki/Category:Cards_by_Konami_index_number)
- [Yu-Gi-Oh! Duel Links cards](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_cards)
- [Yu-Gi-Oh! Duel Links Skills](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_Skills)
- [Yu-Gi-Oh! Master Duel accessories](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Master_Duel_accessories)
- [TCG Speed Duel Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:TCG_Speed_Duel_Forbidden_%26_Limited_Lists)

[OCG Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:OCG_Forbidden_%26_Limited_Lists) was previously
downloaded into [`/wikitext/limit-regulation-ocg`](/wikitext/limit-regulation-ocg) but is no longer automatically
updating as it is not needed downstream. This could change as needed in the future.

## Adding a new category

1. Run the [download workflow](https://github.com/DawnbrandBots/yaml-yugipedia/actions/workflows/download.yml) with the URL-encoded title of the category page without the `Category:` as input, e.g. `Yu-Gi-Oh!_Master_Duel_Forbidden_%26_Limited_Lists`.
1. Add this URL-encoded category title to the [update list](/src/categories.txt) for the saved wikitexts automatically receive new changes via the [update workflow](https://github.com/DawnbrandBots/yaml-yugipedia/blob/master/.github/workflows/update.yml).

You can request to include a category by opening a pull request adding an entry to the [update list](/src/categories.txt).
