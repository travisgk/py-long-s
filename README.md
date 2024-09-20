# long-s
This Python script converts text to use the archaic long S letter ( ſ ) in its spellings.

English, Spanish, French, Italian, and German are supported.
<br>
`pip install unidecode` is required.
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

## German

With German words, the script might encounter an occurrence of the letter S that remains ambiguous, even after the conversion process.

By default, any leftover ambiguous S will be replaced with a long S ( ſ ).

If it's preferred to leave it up to human interpretation, 
the program can be explicitly told to leave these ambiguities marked in the returned string:
```
print(long_s.convert("Mäuschen", lang="de", keep_unknown_s=True))
```
This will print ```Mäu╳chen```, which can then be manually changed to ```Mäuschen```.

<br>
<hr>

### Special Thanks

Thank you Andrew West of the TeX Users Group for the documentation found under [The Rules for Long S](https://www.tug.org/TUGboat/tb32-1/tb100west.pdf), which was fundamental in writing the conversion functions for English, Spanish, French, and Italian.
