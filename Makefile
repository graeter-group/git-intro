all: presentation

presentation: presentation.Rmd
	R -e 'rmarkdown::render("presentation.Rmd", output_file = "index.html")'
	xdg-open index.html

setup:
	R -e 'install.packages("renv")'
	R -e 'renv::restore()'
	