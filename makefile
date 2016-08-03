engine = python3
script = generate_image.py
preamble = preamble.py
flags = -rrr -a logspace
src = equations.tex
out = figure.pdf
prev = preview.png

.PHONY: update clean

show: $(prev)
	xdg-open $(prev)

$(prev): $(out)
	convert $(out)[0] $(prev)
	
figure: $(out)
	xdg-open $(out)

$(out): $(src) $(script) $(preamble)
	$(engine) $(script) --tex_source $(src) $(flags)

update:
	touch $(script)

clean:
	-rm $(out)
