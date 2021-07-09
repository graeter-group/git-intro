all: presentation

presentation: presentation.Rmd
	R -e 'rmarkdown::render("presentation.Rmd")'
	xdg-open presentation.html

setup:
	R -e 'install.packages("renv")'
	R -e 'renv::restore()'
	
