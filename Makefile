default: outputs.html

LFVdiagrams.tar.gz: pdf_files
	./gen_overview.py
LFVdiagrams.zip: pdf_files
	./gen_overview.py
outputs.html: pdf_files
	./gen_overview.py

clean:
	rm outputs.html LFVdiagrams.tar.gz LFVdiagrams.zip

.PHONY: default
