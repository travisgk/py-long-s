# long-s
This Python script converts text to use the archaic long S letter ( ſ ) in its spellings.

English, Spanish, French, Italian, and German are supported.

```
import long_s

print(long_s.convert("The discussion was surprisingly insightful.", lang="en"))
print(long_s.convert("La discusión fue sorprendentemente perspicaz.", lang="es"))
print(long_s.convert("La discussion était étonnamment perspicace.", lang="fr"))
print(long_s.convert("La discussione è stata sorprendentemente perspicace.", lang="it"))
print(long_s.convert("Die Diskussion war überraschend aufschlussreich.", lang="de"))
```

```
The diſcuſſion was ſurpriſingly inſightful.
La diſcuſión fue ſorprendentemente perſpicaz.
La diſcuſſion était étonnamment perſpicace.
La diſcuſſione è ſtata ſorprendentemente perſpicace.
Die Diskuſſion war überraſchend aufſchluſsreich.
```

<br>
<hr>

### German

The script might encounter an occurrence of the letter S in a German word that remains ambiguous, even after the conversion process.

By default, any leftover ambiguous S will be replaced with a long S ( ſ ).

If it's preferred to leave it up to human interpretation, 
the program can be explicitly told to leave these ambiguities marked in the returned string:
```
print(long_s.convert("Mäuschen", lang="de", keep_unknown_s=True))
```
This will print ```Mäu╳chen```, which can be then manually changed to ```Mäuschen```.
