TEX_FILES := $(wildcard diagram_files/*.tex)
PDF_FILES := $(TEX_FILES:diagram_files/%.tex=pdf_files/%.pdf)

default: $(PDF_FILES)

pdf_files/:
	mkdir -p $@
pdf_files/%.pdf: diagram_files/%.tex | pdf_files/
	./convert_feynmp.py $< $@

clean:
	rm -f $(PDF_FILES)
	rmdir --ignore-fail-on-non-empty pdf_files

.PHONY: default
