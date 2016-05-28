# 'Makefile'.
# Chris Shiels.


SUBJ = '/C=GB/ST=London/L=London/O=Mecachis/OU=Mecachis/CN=registry.service.consul'


registry.service.consul.crt:	registry.service.consul.key
	openssl req \
	-x509 \
	-new  \
	-key registry.service.consul.key \
	-nodes \
	-sha256 \
	-subj $(SUBJ) \
	-days 365 \
	-out ./registry.service.consul.crt


registry.service.consul.key:
	openssl genrsa -out registry.service.consul.key 4096


clean:
	rm -f registry.service.consul.crt registry.service.consul.key
