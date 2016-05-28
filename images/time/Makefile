# 'Makefile'.
# Chris Shiels.


VERSION = latest


run:	build
	sudo docker run --rm -i -t -p 7001:7001 cs/time:$(VERSION)


build:	Dockerfile src/github.com/chris/time/time.go
	GOROOT=/usr/local/go GOPATH=`pwd` /usr/local/go/bin/go install -ldflags "-X main.version=$(VERSION)" github.com/chris/time
	sudo docker build -t cs/time:$(VERSION) .
	touch $@
