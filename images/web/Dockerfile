# 'Dockerfile'.
# Chris Shiels.


from centos:7

expose 7000

env PORT=7000
env DATEENDPOINT=date-1.service.consul
env TIMEENDPOINT=time-1.service.consul

# Prevent Go runtime from defaulting to the non-working 'netdns=cgo'.
cmd GODEBUG=netdns=go /web -p $PORT -dateendpoint $DATEENDPOINT -timeendpoint $TIMEENDPOINT

copy bin/web /
