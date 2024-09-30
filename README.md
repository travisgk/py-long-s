# long-s
This Python script converts text to use the archaic long S letter ( ſ ) in its spellings.

English, French, German, Spanish, and Italian are supported.
<br>
`pip install unidecode` is required.

```
import long_s

print(long_s.convert("The discussion was surprisingly insightful.", lang="en"))
print(long_s.convert("La discussion était étonnamment perspicace.", lang="fr"))
print(long_s.convert("Die Diskussion war überraschend aufschlussreich.", lang="de"))
print(long_s.convert("La discusión fue sorprendentemente perspicaz.", lang="es"))
print(long_s.convert("La discussione è stata sorprendentemente perspicace.", lang="it"))
```

```
The diſcuſſion was ſurpriſingly inſightful.
La diſcuſſion était étonnamment perſpicace.
Die Diskuſſion war überraſchend aufſchluſsreich.
La diſcuſión fue ſorprendentemente perſpicaz.
La diſcuſſione è ſtata ſorprendentemente perſpicace.
```

<br>

### Special Thanks

Thank you Andrew West of the TeX Users Group for the documentation found under [The Rules for Long S](https://www.tug.org/TUGboat/tb32-1/tb100west.pdf), which was fundamental in writing the conversion functions for English, Spanish, French, and Italian.
