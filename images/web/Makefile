# 'Makefile'.
# Chris Shiels.


VERSION = latest


run:	build
	sudo docker run --rm -i -t -p 7001:7001 cs/web:$(VERSION)


build:	Dockerfile src/github.com/chris/web/web.go
	GOROOT=/usr/local/go GOPATH=`pwd` /usr/local/go/bin/go install -ldflags "-X main.version=$(VERSION)" github.com/chris/web
	sudo docker build -t cs/web:$(VERSION) .
	touch $@
