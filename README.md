# YAML [Yugipedia](https://yugipedia.com)

The [YAML Yugi](https://github.com/DawnbrandBots/yaml-yugi) project aims to create a comprehensive, machine-readable,
human-editable database of the _Yu-Gi-Oh! Trading Card Game_ and _Official Card Game_. This is an automatically-updated
collection of wikitexts from Yugipedia of cards for intake and transformation into the final database.

All files under [`/wikitext`](/wikitext) are downloaded using the Mediawiki API and copyright belongs to their original
holders. Any Yugipedia-original content is licensed under [CC BY-SA 4.0](https://yugipedia.com/wiki/Yugipedia:Licensing)
but most card text is &copy; Studio Dice/SHUEISHA, TV TOKYO, KONAMI.

The categories being downloaded are
- [Duel Monsters cards](https://yugipedia.com/wiki/Category:Duel_Monsters_cards): [`/wikitext/cards`](/wikitext/cards)
- [Yu-Gi-Oh! Duel Links cards](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_cards): [`/wikitext/duel-links-cards`](/wikitext/duel-links-cards)
- [Yu-Gi-Oh! Duel Links Skills](https://yugipedia.com/wiki/Category:Yu-Gi-Oh!_Duel_Links_Skills): [`/wikitext/duel-links-skills`](/wikitext/duel-links-skills)
- [Rush Duel cards](https://yugipedia.com/wiki/Category:Rush_Duel_cards): [`/wikitext/rush`](/wikitext/rush)
- [Skill Cards](https://yugipedia.com/wiki/Category:Skill_Cards): [`/wikitext/speed`](/wikitext/speed)
- [OCG Forbidden & Limited Lists](https://yugipedia.com/wiki/Category:OCG_Forbidden_%26_Limited_Lists): [`/wikitext/limit-regulation-ocg`](/wikitext/limit-regulation-ocg) (to be replaced by the official sources if possible)

The remaining files — the actual source code of this stage of the pipeline — are available under the
GNU Lesser General Public License 3.0 or later. See [COPYING](./COPYING) and [COPYING.LESSER](./COPYING.LESSER)
for more details.
