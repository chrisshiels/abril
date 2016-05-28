# 'Makefile'.
# Chris Shiels.


VERSION = latest


run:	build
	sudo docker run --rm -i -t -p 8080:8080 cs/hostnamehttpserver:$(VERSION)


build:	Dockerfile hostnamehttpserver.py
	sudo docker build -t cs/hostnamehttpserver:$(VERSION) .
	touch $@
