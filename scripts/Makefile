GT_RUS=${HOME}/gt/langs/rus/src

all : generator-gt-desc.phonetic.hfstol \
	g2p.hfstol \
	g2p.xfst \
	g2p_lex-test.txt

g2p_lex-test.txt : test.csv
	echo "creating tmp test-pair file..."
	cat test.csv | cut -d "," -f 1 > /tmp/g2p_lex-test.txt

g2p.phon.hfst : g2p.twolc
	echo "compiling hfst file..."
	hfst-twolc -i g2p.twolc -o g2p.phon.hfst

lexicon.phonetic.hfst : ${GT_RUS}/morphology/lexicon.tmp.lexc
	echo "building custom lexicon.hfst with ∂ and Ω for в and ъ ..."
	cat ${GT_RUS}/morphology/lexicon.tmp.lexc \
		| sed -E "s/(\+Dat|\+Ins|\+Loc)(.*>)а([мтх]и)/\1\2Ω\3/g" \
		| sed -E "s/(\+Pl3.*<)ят/\1Ωт/g" \
		| sed -E "s/(\+Acc|\+Gen)(.*[ое]́?)г(о)/\1\2∂\3/g" \
		| sed -E "s/(:по̀л[-ёа-я́]+о́?)г(о )/\1∂\2/g" \
		| sed -E "s/(:все)г(о)/\1∂\2/g" \
		| sed -E "s/:(.*-на́все)г(о)/:\1∂\2/g" \
		| sed -E "s/(:ито)г(о)/\1∂\2/g" \
		| sed -E "s/(:не́че)г(о)/\1∂\2/g" \
		| sed -E "s/(:ниче)г(о)/\1∂\2/g" \
		| sed -E "s/(:отто)г(о)/\1∂\2/g" \
		| sed -E "s/(:отче)г(о)/\1∂\2/g" \
		| sed -E "s/(:се)г(о́дня)/\1∂\2/g" \
		| sed -E "s/(:то)г(о́)/\1∂\2/g" \
		| sed -E "s/(то)г(о.% что)/\1∂\2/g" \
		| sed -E "s/(:че)г(о)/\1∂\2/g" \
		| hfst-lexc -v --format=openfst-tropical --alignStrings -o lexicon.phonetic.hfst

generator-gt-desc.phonetic.tmp1.hfst : lexicon.phonetic.hfst ${GT_RUS}/phonology/rus-phon.compose.hfst
	echo "compose-intersecting with standard twolc rules ..."
	hfst-determinize lexicon.phonetic.hfst \
		| hfst-minimize \
		| hfst-compose-intersect -2 ${GT_RUS}/phonology/rus-phon.compose.hfst \
		| hfst-determinize \
		| hfst-minimize \
		> generator-gt-desc.phonetic.tmp1.hfst

generator-gt-desc.phonetic.tmp3.hfst : ${GT_RUS}/filters/reorder-subpos-tags.hfst \
		${GT_RUS}/filters/reorder-semantic-tags.hfst \
		generator-gt-desc.phonetic.tmp1.hfst
	echo "applying filters..."
	printf "read regex \
		@\"${GT_RUS}/filters/reorder-subpos-tags.hfst\" \
		.o. @\"${GT_RUS}/filters/reorder-semantic-tags.hfst\" \
		.o. @\"generator-gt-desc.phonetic.tmp1.hfst\" \
		;\n \
		 save stack generator-gt-desc.phonetic.tmp3.hfst\n \
		quit\n" \
		| hfst-xfst -p -v --format=openfst-tropical

generator-gt-desc.phonetic.tmp4.hfst : ${GT_RUS}/filters/make-optional-transitivity-tags.hfst \
		${GT_RUS}/filters/make-optional-homonymy-tags.hfst \
		${GT_RUS}/filters/make-optional-hyph-tags.hfst \
		${GT_RUS}/filters/make-optional-variant-tags.hfst \
		${GT_RUS}/filters/make-optional-semantic-tags.hfst \
		${GT_RUS}/filters/make-optional-error-tags.hfst \
		${GT_RUS}/filters/make-optional-adv_comp-tags.hfst \
		${GT_RUS}/filters/make-optional-orig_lang-tags.hfst \
		${GT_RUS}/filters/remove-area-tags.hfst \
		${GT_RUS}/filters/remove-dialect-tags.hfst \
		${GT_RUS}/filters/remove-number-string-tags.hfst \
		${GT_RUS}/filters/remove-usage-tags.hfst \
		${GT_RUS}/filters/remove-orthography-tags.hfst \
		${GT_RUS}/filters/remove-Orth_IPA-strings.hfst \
		${GT_RUS}/filters/remove-Use_minus_PMatch-tags.hfst \
		${GT_RUS}/filters/remove-Use_GC-strings.hfst \
		${GT_RUS}/filters/remove-Use_minusGC-tags.hfst \
		${GT_RUS}/filters/remove-Use_PMatch-strings.hfst \
		${GT_RUS}/filters/remove-mwe-tags.hfst \
		generator-gt-desc.phonetic.tmp3.hfst \
		${GT_RUS}/orthography/downcase-derived_proper-strings.compose.hfst \
		${GT_RUS}/filters/remove-hyphenation-marks.hfst \
		${GT_RUS}/filters/remove-infl_deriv-borders.hfst \
		${GT_RUS}/filters/remove-word-boundary.hfst
	printf "read regex \
		@\"${GT_RUS}/filters/make-optional-transitivity-tags.hfst\"  \
		.o. @\"${GT_RUS}/filters/make-optional-homonymy-tags.hfst\"  \
		.o. @\"${GT_RUS}/filters/make-optional-hyph-tags.hfst\"      \
		.o. @\"${GT_RUS}/filters/make-optional-variant-tags.hfst\"   \
		.o. @\"${GT_RUS}/filters/make-optional-semantic-tags.hfst\"  \
		.o. @\"${GT_RUS}/filters/make-optional-error-tags.hfst\"     \
		.o. @\"${GT_RUS}/filters/make-optional-adv_comp-tags.hfst\"  \
		.o. @\"${GT_RUS}/filters/make-optional-orig_lang-tags.hfst\" \
		.o. @\"${GT_RUS}/filters/remove-area-tags.hfst\"             \
		.o. @\"${GT_RUS}/filters/remove-dialect-tags.hfst\"          \
		.o. @\"${GT_RUS}/filters/remove-number-string-tags.hfst\"    \
		.o. @\"${GT_RUS}/filters/remove-usage-tags.hfst\"            \
		.o. @\"${GT_RUS}/filters/remove-orthography-tags.hfst\"      \
		.o. @\"${GT_RUS}/filters/remove-Orth_IPA-strings.hfst\"      \
		.o. @\"${GT_RUS}/filters/remove-Use_minus_PMatch-tags.hfst\" \
		.o. @\"${GT_RUS}/filters/remove-Use_GC-strings.hfst\"        \
		.o. @\"${GT_RUS}/filters/remove-Use_minusGC-tags.hfst\"      \
		.o. @\"${GT_RUS}/filters/remove-Use_PMatch-strings.hfst\"    \
		.o. @\"${GT_RUS}/filters/remove-mwe-tags.hfst\"              \
		.o. @\"generator-gt-desc.phonetic.tmp3.hfst\" \
		.o. @\"${GT_RUS}/orthography/downcase-derived_proper-strings.compose.hfst\" \
		.o. @\"${GT_RUS}/filters/remove-hyphenation-marks.hfst\"        \
		.o. @\"${GT_RUS}/filters/remove-infl_deriv-borders.hfst\"       \
		.o. @\"${GT_RUS}/filters/remove-word-boundary.hfst\"            \
		;\n \
		save stack generator-gt-desc.phonetic.tmp4.hfst\n \
		quit\n" \
		| /usr/local/bin/hfst-xfst -p -v --format=openfst-tropical

generator-gt-desc.phonetic.tmp5.hfst : generator-gt-desc.phonetic.tmp4.hfst g2p.phon.hfst
	hfst-compose-intersect -1 generator-gt-desc.phonetic.tmp4.hfst -2 g2p.phon.hfst \
		| hfst-determinize \
		| hfst-minimize \
		| hfst-remove-epsilons \
		> generator-gt-desc.phonetic.tmp5.hfst

generator-gt-desc.phonetic.hfst : ${GT_RUS}/filters/make-optional-cyrillic-jo.hfst \
		${GT_RUS}/filters/make-ambiguous-AnIn.hfst \
		${GT_RUS}/filters/make-ambiguous-MFN.hfst \
		generator-gt-desc.phonetic.tmp5.hfst
	printf "read regex \
		@\"${GT_RUS}/filters/make-optional-cyrillic-jo.hfst\" \
		.o. @\"${GT_RUS}/filters/make-ambiguous-AnIn.hfst\" \
		.o. @\"${GT_RUS}/filters/make-ambiguous-MFN.hfst\" \
		.o. @\"generator-gt-desc.phonetic.tmp5.hfst\" \
		;\n \
		save stack generator-gt-desc.phonetic.hfst\n \
		quit\n" \
		| /usr/local/bin/hfst-xfst -p -v --format=openfst-tropical

generator-gt-desc.phonetic.hfstol : generator-gt-desc.phonetic.hfst
	echo "converting to optimized lookup format..."
	hfst-determinize generator-gt-desc.phonetic.hfst \
		| hfst-minimize \
		| hfst-fst2fst -O -o generator-gt-desc.phonetic.hfstol

univ.hfst : 
	echo "creating base FST with universal language..."
	echo "?* ;" | hfst-regexp2fst -o univ.hfst

g2p.hfst : g2p.phon.hfst univ.hfst
	echo "compose-intersecting twolc rules with universal FST..."
	hfst-compose-intersect univ.hfst g2p.phon.hfst \
		| hfst-minimize \
		> g2p.hfst

g2p.hfstol : g2p.hfst
	echo "converting to optimized lookup format..."
	hfst-fst2fst -O -i g2p.hfst -o g2p.hfstol

g2p.xfst : g2p.twolc
	printf "read-grammar g2p.twolc\ncompile\nintersect\ny\ng2p-all\nsave-binary g2p.xfst\nlex-test-file /tmp/g2p_lex-test.txt /tmp/tmp_output_g2p_xfst.txt\nquit\n" | twolc

g2p.lookup.xfst : g2p.xfst
	echo -e "\nYou can use 'lookup g2p.lookup.xfst' to test arbitrary strings.\n"
	xfst -e "load stack < g2p.xfst" \
	     -e "invert net" \
	     -e "save stack g2p.lookup.xfst" \
	     -stop

.PHONY : clean
clean :
	-rm *.hfst *.hfstol *.xfst

.PHONY : check
check : all
	echo "running test entries..."
	cat /tmp/g2p_lex-test.txt | hfst-lookup g2p.hfstol 2>/dev/null >/tmp/output_g2p_hfst.txt
	echo "To see output from test.csv, use..."
	echo "less /tmp/output_g2p_hfst.txt"
	cat /tmp/tmp_output_g2p_xfst.txt | egrep -v "^  " > /tmp/output_g2p_xfst.txt
	rm /tmp/tmp_output_g2p_xfst.txt
	echo "To see output from test.csv, use ..."
	echo "less /tmp/output_g2p_xfst.txt"
