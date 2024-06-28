from ._romance import french_conversion, italian_conversion, spanish_conversion
from ._germanic import english_conversion, german_conversion

def convert(text, lang="en"):
	if lang == "en":
		return english_conversion(text)
	elif lang == "fr":
		return french_conversion(text)
	elif lang == "it":
		return italian_conversion(text)
	elif lang == "es":
		return spanish_conversion(text)
	elif lang == "de":
		return german_conversion(text)
	print("language not found. the options are: en, fr, it, es, de.")
	return text
