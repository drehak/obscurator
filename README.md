# obscurator, a library for substitution of visually similar letters
__obscurator__ is a program (at the moment just a library) that substitutes letters for their visual counterparts from various other alphabets in Unicode. At the moment, Greek and half of Cyrillic is implemented. All the replacement letters are tiered according to similarity, with the highest tier having glyphs nearly indistinguishable from their counterparts. This obviously assumes that whoever reads the output has the necessary fonts to display the glyphs.

Only Python 3 is required.

## Why would I ever want to use this?
* Avoiding word filter/detection (4chan, Twitter)
* Making your text way harder to index or search in
* Swearing in Steam reviews
* Driving people with screen readers insane

## Quick start
```python
$ python3 -i obscurator.py
>>> o = Obscurator()
>>> o.substitute('Few black taxis drive up major roads on quiet hazy nights.')
'Fеw blасk tахis drive uр major rοаds оn quiet hazу nights.'
>>> from common import Similarity
>>> o = Obscurator(similarities=[Similarity.MEDIUM, Similarity.LOW])
>>> o.substitute('Few black taxis drive up major roads on quiet hazy nights.', chance=0.8)
'Гэω бlacк тαxιs δrivэ μρ mαjσr яσαδs ση qμiετ нazγ nιgнts.'
```

By default, only the most similar Greek and Cyrillic glyphs are used and subsituted with a chance of 50% (if there are equivalents at all, that is.)

This library only focuses on visual similarity, not phonetic. Readers of native scripts are probably gonna trip up on that for a while. Placement into the similarity tiers is subjective.

## Output showcase
lower case; similarity tiers: none / high / medium / low / medium+low; substitution chance: 100%
* Gaze at this sentence for just about sixty seconds and then explain what makes it quite different from the average sentence.
* Gаzе аt thіѕ ѕеntеnϲе fоr јuѕt аbοut ѕіхtу ѕесοndѕ аnd thеn ехрlаіn whаt mаkеѕ іt quіtе dіffеrеnt frοm thе аvеrаgе ѕеntеnϲе.
* Gӑzӗ ӓт τһїs sёηҭӗηҫҿ ғσr jυsτ ӓвөυт sїχτү sӗҫӧηds ӑηd τҺӗη ѐχρlӓїη wӊӑτ мӓќѐs їτ qυїҭӗ dїғғёrѐηт ғrσӎ тӊё ӑѵҽrӓgѐ sѐηтѐηҫҽ.
* Gαzӟ αt tҕis sεӣtεӥcэ ӻѳя jμst αѢѳμt siӿtў sєcӫиδs αиδ tӈэӥ єӿplαiӣ шӈαt mαӄεs it qμitҙ δiӻӻӭяӭӣt ӻяѳm tӈє αѷєяαgε sзиtεѝcӟ.
* Gӓzҽ ӑҭ τӊїs sёӣҭӭиҫӗ ӻӫя jμsτ ӑвӧυτ sιӽҭӯ sҽҫσиδs ӓηδ τҥэӣ эӿρlӑιӥ шңӓт мӓκӭs їτ qμιтє διӻӻєяёӥτ ӻяσӎ τҕҙ ӑѷэяӓgз sёитӟиҫӗ.

upper case; similarity tiers: none / high / medium / low / medium+low; substitution chance: 100%
* GAZE AT THIS SENTENCE FOR JUST ABOUT SIXTY SECONDS AND THEN EXPLAIN WHAT MAKES IT QUITE DIFFERENT FROM THE AVERAGE SENTENCE.
* GΑΖΕ ΑТ ТНΙЅ ЅЕΝТΕΝϹЕ FОR ЈUЅТ АΒΟUТ ЅӀХΤΥ ЅЕϹОΝDЅ АΝD ТΗΕΝ ЕΧΡLАΙΝ WΗАТ ΜΑΚΕЅ ӀТ QUӀΤЕ DӀFFЕRЕΝТ FRΟМ ТΗΕ АVΕRАGЕ ЅЕΝΤЕΝСΕ.
* GӐZЁ ӐҬ ҬҢЇS SӖNҬӖNҪӖ ӺӨR JUSҬ ӐBѲUҬ SЇҲҬУ SЁҪѺNDS ӐND ҬӉЀN ЁӼҎLӒЇN WҢӐҬ ӍӒҚЁS ЇҬ QUЇҬӖ DЇӺӺӖRЀNҬ ҒRѲӍ ҬӉӖ ӒѴЀRӒGӖ SӖNҬӖNҪЀ.
* GAZҘ AT TӇIS SӬӤTЄӤCӠ ГӪЯ JUST AБΘUT SIӾTЎ SӞCӪЍDS AЍD TӇӞЍ ӞӾPLAIӢ ѠҔAT MAӃΞS IT QUITҼ DIΓГЗЯҼӤT ӶЯӪM TҔҼ AѶЄЯAGӬ SΣЍTӠӤCΣ.
* GӒZЄ ӐҬ ҬҢЇS SҼӤҬҾЍҪӠ ΓӨЯ JUSҬ ӐБӨUҬ SЇҲҬӰ SҘҪӦЍDS ӒЍD ҬҢӖӤ ЭӾҎLӐЇЍ ѠӉӐҬ ӍӐЌӬS ЇҬ QUЇҬЁ DЇГЃЄЯӬЍҬ ҐЯӪӍ ҬҤЄ ӐѴЄЯӒGӖ SΣИҬЁЍҪҼ.

I don't see why anyone would want to use the lower tiers.

## Further plans
* Add more alphabets
* Research the availability of the rest of Greek/Cyrillic blocks in the fonts, add the rest of glyphs
* Create a UNIX-style script/executable that reads from standard input and spits out substitutions
* Stabilize the interface, conform to semver
* Publish on PyPi (as if, lol)
