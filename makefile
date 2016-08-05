py = python3
script = generate_image.py
preamble = preamble.py
flags = -r -m para # -a logspace
src = equations.tex
out = *.pdf *.out *.aux *.log
fig = figure.pdf
prev = preview.png
texpy = gen_tex_doc.py
texdoc = tex_doc
texeng = xelatex

.PHONY: update clean

show: $(prev)
	xdg-open $(prev)

$(prev): $(fig)
	convert $(fig)[0] $(prev)
	
figure: $(fig)
	xdg-open $(fig)

$(fig): $(src) $(script) $(preamble)
	$(py) $(script) --tex_source $(src) $(flags)

update:
	touch $(script)

tex: $(texdoc)
	$(texeng) $(texdoc).tex
	xdg-open $(texdoc).pdf

$(texdoc): $(src) $(texpy)
	$(py) $(texpy) -s $(src) -o $(texdoc).tex

clean:
	-rm $(out) $(texdoc)
