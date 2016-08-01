engine = python3
script = generate_image.py
flags = -r 
src = equations.tex
out = figure.pdf
prev = preview.png

all: $(out)
	convert $(out)[0] $(prev)
	xdg-open $(prev)

figure: $(out)
	xdg-open $(out)

preview: $(out)
	convert $(out)[0] $(prev)

$(out) : $(src) $(script)
	$(engine) $(script) --tex_source $(src) $(flags)

.PHONY: clean
clean :
	-rm $(out)
