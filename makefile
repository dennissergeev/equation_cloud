py = python3
script = generate_image.py
preamble = preamble.py
flags = -rr -a logspace
src = equations.tex
out = *.pdf *.out *.aux *.log
prev = preview.png
texpy = gen_tex_doc.py
texdoc = tex_doc
texeng = xelatex

.PHONY: update clean

tex: $(texdoc)
	$(texeng) $(texdoc).tex
	xdg-open $(texdoc).pdf

$(texdoc): $(src) $(texpy)
	$(py) $(texpy) -s $(src) -o $(texdoc).tex

show: $(prev)
	xdg-open $(prev)

$(prev): $(out)
	convert $(out)[0] $(prev)
	
figure: $(out)
	xdg-open $(out)

$(out): $(src) $(script) $(preamble)
	$(py) $(script) --tex_source $(src) $(flags)

update:
	touch $(script)

clean:
	-rm $(out) $(texdoc)
