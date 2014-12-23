TEX_FILES := $(wildcard diagram_files/*.tex)
PDF_FILES := $(TEX_FILES:diagram_files/%.tex=gh-pages/pdf_files/%.pdf)
PNG_FILES := $(TEX_FILES:diagram_files/%.tex=gh-pages/png_files/%.png)
WHITE_PNG_FILES := $(TEX_FILES:diagram_files/%.tex=gh-pages/white_png_files/%.png)

default: $(PDF_FILES) $(PNG_FILES) $(WHITE_PNG_FILES)

gh-pages/pdf_files/:
	mkdir -p $@
gh-pages/png_files/:
	mkdir -p $@
gh-pages/white_png_files/:
	mkdir -p $@
gh-pages/pdf_files/%.pdf: diagram_files/%.tex | gh-pages/pdf_files/
	./convert_feynmp.py $< $@
gh-pages/png_files/%.png: gh-pages/pdf_files/%.pdf | gh-pages/png_files/
	convert -density 900 -quality 100 $< $@
gh-pages/white_png_files/%.png: gh-pages/pdf_files/%.pdf | gh-pages/white_png_files/
	convert -density 900 -alpha off -quality 100 $< $@

clean:
	rm -f $(PDF_FILES) $(PNG_FILES) $(WHITE_PNG_FILES)

.PHONY: default
