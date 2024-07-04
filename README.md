# long-s
This python script converts text to use the archaic long S letter ( ſ ) in its spellings. English, Spanish, Italian, French, and German are supported.

```
import long_s

print(long_s.convert("The discussion was surprisingly insightful.", lang="en"))
print(long_s.convert("La discussion était étonnamment perspicace.", lang="fr"))
print(long_s.convert("La discussione è stata sorprendentemente perspicace.", lang="it"))
print(long_s.convert("La discusión fue sorprendentemente perspicaz.", lang="es"))
print(long_s.convert("Die Diskussion war überraschend aufschlussreich.", lang="de"))
```

```
The diſcuſſion was ſurpriſingly inſightful.
La diſcuſſion était étonnamment perſpicace.
La diſcuſſione è ſtata ſorprendentemente perſpicace.
La diſcuſión fue ſorprendentemente perſpicaz.
Die Diskuſſion war überraſchend aufſchluſsreich.

```
