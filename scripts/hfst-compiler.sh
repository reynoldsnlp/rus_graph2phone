#!/bin/bash

if [[ test.csv -nt /tmp/g2p_lex-test.txt ]]; then
	echo "creating tmp test-pair file..."
	cat test.csv | cut -d "," -f 1 > /tmp/g2p_lex-test.txt
fi

# if source is newer than compiled, recompile
if [[ g2p.twolc -nt g2p.hfst ]]; then
	echo "compiling hfst file..."
	hfst-twolc -i g2p.twolc -o g2p.hfst
fi

if [[ g2p.hfst -nt g2pall.hfst ]]; then
	echo "splitting and intersecting twolc rules..."
	hfst-split g2p.hfst --prefix g2prule --extension .hfst
	echo "?* ;" | hfst-regexp2fst -o g2pall.hfst
	for fst in g2prule*.hfst ; do
	    hfst-intersect $fst g2pall.hfst -o temp.hfst
	    cp temp.hfst g2pall.hfst
	done
	rm g2prule*.hfst
	rm temp.hfst
fi

echo "running test entries..."
cat /tmp/g2p_lex-test.txt | hfst-lookup g2pall.hfst 2>/dev/null >/tmp/output_g2p_hfst.txt

echo -e "To see output from test.csv, 'less /tmp/output_g2p_hfst.txt'\n"
