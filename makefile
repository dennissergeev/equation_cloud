engine = python3
script = generate_image.py
flags = --tex_source 
src = equations.tex
out = figure.pdf
prev = preview.png

all: $(out)
	convert $(out)[0] $(prev)

figure: $(out)
	xdg-open $(out)

preview: $(out)
	convert $(out)[0] $(prev)

$(out) : $(src) $(script)
	$(engine) $(script) $(flags) $(src)

.PHONY: clean
clean :
	-rm $(out)
