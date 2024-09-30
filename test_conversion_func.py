"""
Filename: test_conversion_func.py
Description: This file contains a function to verify that
			 the conversion functions for each language are working properly.

Author: TravisGK
Version: 1.0

License: MIT License
"""

import long_s

# these are words from the supported languages
# that are sourced from historical materials,
# so they are used to verify that the conversion functions 
# are working properly.
_SPELLINGS = {
	# English
	"en": [
		"ſatisfation",
		"misfortune",
		"transfuſe",
		"transfix",
		"transfer",
		"ſucceſsful",
		"offset",
		"off-ſet",
		"huſband", # no long S before mid 18th century.
		"Shaftſbury", # no long S before mid 18th century.
		"ſkin", # no long S before mid 18th century.
		"aſk", # no long S before mid 18th century.
		"riſk", # no long S before mid 18th century.
		"maſked", # no long S before mid 18th century.
		"Croſs-ſtitch",
		"Croſs-ſtaff",
		"Croſsſtitch",
		"croſsſtaff",
		"ſong",
		"uſe",
		"preſs",
		"ſubſtitute",
		"croſs-piece",
		"croſs-examination",
		"Preſs-work",
		"bird's-neſt",
	],

	# French
	"fr": [
		"ils",
		"s'il",
		"s'eſt",
		"ſatisfaction",
		"toutesfois",
		"presbyter",
		"déshabiller",
		"déshonnête",
		"ſans",
		"eſt",
		"ſubſtituer",
		"tres-bien",
	],

	# German
	"de": [
		"Kosmos",
		"Hauſe",
		"Häuſer",
		"Liebesbrief",
		"Arbeitsamt",
		"Donnerstag",
		"Unterſuchungsergebnis",
		"Haustür",
		"Dispoſition",
		"disharmoniſch",
		"dasſelbe",
		"Wirtsſtube",
		"Ausſicht",
		"Wachstum",
		"Weisheit",
		"Häuslein",
		"Mäuschen",
		"Bistum",
		"nachweisbar",
		"wohlweislich",
		"boshaft",
		"reiſte",
		"ſechſte",
		"kosmiſch",
		"brüskieren",
		"Realismus",
		"lesbiſch",
		"Mesner",
		"Oswald",
		"Dresden",
		"Schleswig",
		"Osnabrück",
		"einſpielen",
		"ausſpielen",
		"ſkandalös",
		"Pſyche",
		"Miſanthrop",
		"Rätſel",
		"Labſal",
		"ſeltſam",
		"Weſpe",
		"Knoſpe",
		"faſten",
		"faſzinierend",
		"Oſzillograph",
		"Aſt",
		"Haſt",
		"Luſt",
		"einſt",
		"ſtehſt", 
		"meiſtens",
		"beſte",
		"knuſpern",
		"reiſt",
		"lieſt",
		"paſſte",
		"ſechſte",
		"Gſtaad",
		"Buſch",
		"Eſche",
		"Wunſch",
		"wünſchen",
		"Flaſh",
		"Waſſer",
		"Biſſen",
		"Zeugniſſe",
		"Faſs",
		"Eschatologie",
		"aſſimiliert",
		"Aſſonanz",
		"unſre",
		"laſſ'",
		"tranſzendieren",
		"tranſzendent",
	],

	# Spanish
	# [ ] force short S before accented O
	"es": [
		"illuſtriſsimos",
		"confeſſores",
		"sí",
		"sì",
		"sé",
		"sè",
		"Apoſtasìa",
		"Apoſtasía",
		"abrasò",
		"paſsò",
		"ſi",
		"ſe",
		"paſſo",
		"transformandoſe",
		"transfigura",
		"ſatisfaccion",
		"presbytero",
		"deshoneſtos",
		"deshoneſtidad",
		"illuſtriſsimo",
		"paſsion",
		"confeſsion",
		"poſsible",
		"exceſſo",
		"comiſſario",
		"neceſſaria",
		"paſſa",
		"tranſ-formados",
		"copioſiſ-ſimo",
	],

	# Italian
	"it": [
		"s’informaſſero",
		"fuſs’egli",
		"paſsò",
		"ricusò",
		"sù",
		"sì",
		"così",
		"paſſo",
		"ſi",
		"ſoddisfare",
		"ſoddisfazione",
		"trasfigurazione",
		"sfogo",
		"sfarzo",
		"sbaglio",
		"sbagliato",
		"reſtaſ-ſero",
		# sometimes ſſi was forced to ſsi historically (but not here).
		"compreſſioni", 
		"proſſima",
	],
}

_LANG_NAMES = {
	"en": "English",
	"fr": "French",
	"de": "German",
	"es": "Spanish",
	"it": "Italian",
}

def test_conversion_func(lang: str=None):
	"""
	Tests the conversion function and outputs to the user
	if any words fail to convert correctly.

	Parameters:
	lang (string): the language code. if None, then all languages are tested.
	"""

	if lang is None:
		# runs tests for every language if a language isn't specified.
		for lang in ["en", "fr", "de", "es", "it"]:
			test_conversion_func(lang)
		return

	# tests each case in the list of spellings.
	spellings = _SPELLINGS[lang]
	conversion_func = long_s.get_conversion_func(lang)
	mismatches = []
	for expected_output in spellings:
		input_text = expected_output.replace("ſ", "s")
		actual_output = conversion_func(input_text)
		if expected_output != actual_output:
			# outputs to the user any mismatch.
			mismatches.append((input_text, actual_output, expected_output))
	
	# prints the results to the user.
	num_mismatches = len(mismatches)
	num_tests = len(spellings)
	lang_name = _LANG_NAMES[lang]
	if num_mismatches == 0:
		# notifies user of success if no errors arose.
		print(f"All {num_tests} tests were successful for {lang_name}.")
	else:
		# notifies the user of each failed test case.
		print("\n")
		print("-" * 79)
		print(
			f"{lang_name}:\n({num_mismatches}/{num_tests}) tests failed.\n"
			f"{'Input':<16}     {'Actual Output':>16}\t"
			f"|\t{'Expected Output':<16}"
		)
		print("-" * 79)
		for input_text, actual_output, expected_output in mismatches:
			print(
				f"{input_text:<16} --> {actual_output:>16}"
				f"\t|\t{expected_output:<16}"
			)
		print("-" * 79)