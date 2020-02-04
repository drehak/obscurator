# obscurator, a library for substitution of visually similar letters
__obscurator__ is a program (at the moment just a library) that substitutes letters for their visual counterparts from various other alphabets in Unicode. At the moment, Greek and Russian alphabets are implemented. All the replacement letters are tiered according to similarity, with the highest tier having glyphs nearly indistinguishable from their counterparts. This obviously assumes that whoever reads the output has the necessary fonts to display the glyphs.

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

By default, only the most similar Greek and Russian glyphs are used and subsituted with a chance of 50% (if thereare equivalents at all, that is.)

## Output showcase
lower case; similarity tiers: none / high / medium / low; substitution chance: 100%
* Gaze at this sentence for just about sixty seconds and then explain what makes it quite different from the average sentence.
* Gаzе аt this sеntеnϲе fоr just аbοut siхtу sеϲοnds аnd thеn ехрlаin whаt mаkеs it quitе diffеrеnt frоm thе аvеrаgе sеntеnϲе.
* Gaze aτ тнιs seηтeηce fσr jυsτ aвσυτ sιχτγ secσηds aηd тнeη eχρlaιη wнaτ мaкes ιτ qυιτe dιffereηт frσм тнe average seητeηce.
* Gαzз αt this sзиtεиcё foя jμst αбoμt sixty sэcoиδs αиδ thзи зxplαiи шhαt mαkзs it qμitε δiffεязиt fяom thз αvεяαgё sёиtёиcэ.

upper case; similarity tiers: none / high / medium / low; substitution chance: 100%
* GAZE AT THIS SENTENCE FOR JUST ABOUT SIXTY SECONDS AND THEN EXPLAIN WHAT MAKES IT QUITE DIFFERENT FROM THE AVERAGE SENTENCE.
* GΑΖΕ АТ ΤНΙS SЕΝΤЕΝϹΕ FОR JUSΤ АВОUΤ SΙΧΤΥ SΕϹΟΝDS ΑΝD ТΗЕΝ ЕΧРLАΙΝ WНΑТ МΑΚЕS ΙΤ QUΙΤЕ DΙFFΕRΕΝТ FRΟΜ ΤНЕ ΑVΕRΑGΕ SΕΝΤЕΝϹЕ.
* GAZЁ AT THIS SЁNTЁNCЁ FOR JUST ABOUT SIXTУ SЁCONDS AND THЁN ЁXPLAIN WHAT MAKЁS IT QUITЁ DIFFЁRЁNT FROM THЁ AVЁRAGЁ SЁNTЁNCЁ.
* GAZΣ AT THIS SΣИTΞИCΣ ΓΘЯ JUST AБΘUT SIXTY SΣCΘИDS AИD THЗИ ΣXPLAIИ WHAT MAKЭS IT QUITЗ DIГГЭЯΞИT ГЯΘM THЗ AVЭЯAGЗ SΞИTΞИCЗ.

## Further plans
* Add more alphabets
* Research the availability of the rest of Greek/Cyrillic blocks in the fonts, add the rest of glyphs
* Create a UNIX-style script/executable that reads from standard input and spits out substitutions
* Stabilize the interface, conform to semver
* Publish on PyPi (as if)
