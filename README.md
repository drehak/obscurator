# obscurator, a library for substitution of visually similar letters
__obscurator__ is a program (at the moment just a library) that substitutes letters for their visual counterparts from various other alphabets in Unicode. At the moment, Greek and Cyrillic is implemented. All the replacement letters are tiered according to similarity, with the highest tier having glyphs nearly indistinguishable from their counterparts. This obviously assumes that whoever reads the output has the necessary fonts to display the glyphs.

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
'Ϝҽѡ Ьlӓҫќ tαxίs dяϊѵѐ ϋϸ ϻӑjoя яѳaδs ӧӣ qΰΐeϮ ӊάzӱ ѝϊgҺϮs.'
```

By default, only the most similar Greek and Cyrillic glyphs are used and subsituted with a chance of 50% (if there are equivalents at all, that is.)

This library only focuses on visual similarity, not phonetic. Readers of native scripts are probably gonna trip up on that for a while. Placement into the similarity tiers is subjective.

## Output showcase
lower case; similarity tiers: none / high / medium / low; substitution chance: 100%
* Gaze at this sentence for just about sixty seconds and then explain what makes it quite different from the average sentence.
* Gаzе аt thіѕ ѕеntеnϲе fоr јuѕt аbοut ѕіхtу ѕеϲоndѕ аnd thеn ехрlаіn whаt mаkеѕ іt quіtе dіffеrеnt frοm thе аvеrаgе ѕеntеnсе.
* Gӓzё ӓτ τҺїs sёηтӗηҫҽ ϝӧr jυsт ӑвσυҭ sїӽτӳ sҿҫӧηds ӑηd τӊҽη ҿχρlӓϊη wңӓт ϻӑқѐs ιҭ qυιтѐ dΐϝғҽrӗηҭ ϝrӧϻ тнҿ ӓѵӗrӓgё sҿηтёηҫӗ.
* Gαzε αϮ ϯӈis sӟϗϮϵͷͻє ӻѳя jϋsϮ άѣѳύϮ siӿϯұ s϶ͻӫήδs αѝδ ϯҕэӣ εӿϸlαiѝ ωҕάϮ mαӄέs iϯ qΰiϮέ δiӻӻ϶яэήϯ ӻяѳm Ϯӈэ άѷεяάgэ sӟӣϮӭήͻэ.

upper case; similarity tiers: none / high / medium / low; substitution chance: 100%
* GAZE AT THIS SENTENCE FOR JUST ABOUT SIXTY SECONDS AND THEN EXPLAIN WHAT MAKES IT QUITE DIFFERENT FROM THE AVERAGE SENTENCE.
* GΑΖЕ АΤ ΤНІЅ ЅЕΝТΕΝСΕ FΟR ЈUЅΤ АΒОUТ ЅΙХТΥ ЅЕϹΟΝDЅ ΑΝD ΤНΕΝ ЕХΡLΑӀΝ WΗΑΤ ϺΑΚЕЅ ӀТ QUΙТЕ DΙFFΕRЕΝТ FRОΜ ТΗЕ АVΕRΑGΕ ЅЕΝΤЕΝϹΕ.
* GӒZӖ ӐҬ ҬҢΪS SЁNҬΈNҪЁ ҒΘR JUSҬ ΆBѺUҬ SΊҲҬϒ SЀҪθNDS ΆND ҬҢΈN ЀҲҎLӐΪN WҢӐҬ ӍӐҜЀS ΊҬ QUЇҬӖ DЇϜϜӖRΈNҬ ҒRӦӍ ҬҤЀ ӒѴΈRΆGӖ SΈNҬЀNҪЀ.
* GAϨΣ AͲ ͲҔIS SӠӤͲӞӤϽӠ ГӪЯ JUSͲ AБӪUͲ SIӾͲӮ SҼϽӪͶDS AӤD ͲӇЄИ ЭӾPLAIӤ ѠӇAͲ MAӃӬS IͲ ϘUIͲΞ DIГГҼЯӠӤͲ ҐЯӪM ͲҔӞ AѶӞЯAGӞ SЄͶͲӞӤϽЗ.

I don't see why anyone would want to use the lower tiers.

## Further plans
* Add extended Greek/Cyrillic/Coptic glyphs
* Add more alphabets
* Create a UNIX-style script/executable that reads from standard input and spits out substitutions
* Stabilize the interface, conform to semver
* Publish on PyPi (as if, lol)
