# 'Makefile'.
# Chris Shiels.


TARGETS = consul_0.6.4_linux_amd64.zip \
	  consul-template_0.14.0_linux_amd64.zip \
	  go1.6.2.linux-amd64.tar.gz \
	  ngrep-1.45.tar.bz2


all: $(TARGETS)


consul_0.6.4_linux_amd64.zip:
	curl -L -O https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip


consul-template_0.14.0_linux_amd64.zip:
	curl -L -O https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip


go1.6.2.linux-amd64.tar.gz:
	curl -L -O https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz


ngrep-1.45.tar.bz2:
	curl -L -O http://prdownloads.sourceforge.net/ngrep/ngrep-1.45.tar.bz2


clean:
	rm -vf $(TARGETS)
