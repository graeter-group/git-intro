.PHONY : all setup

presentation_input=presentation.Rmd
open=true

all: index.html

index.html: $(presentation_input)
	R -e 'rmarkdown::render("$<", output_file = "$@")'
	if $(open); then xdg-open $@; fi


# on unubuntu: sudo apt-get install libcurl4-openssl-dev
setup:
	R -e 'install.packages("renv")'
	R -e 'renv::restore()'
	