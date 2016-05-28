# 'registrator.spec'.
# Chris Shiels.


%define revision 6f4147f7b5cea3a966d6f9b586df161fc0b69f39


Name:       registrator
Version:    20160427
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    The MIT License (MIT)
Vendor:     Mecachis
URL:        http://gliderlabs.com/registrator/latest/
Summary:    Service registry bridge for Docker with pluggable adapters


%description
Registrator automatically registers and deregisters services for any
Docker container by inspecting containers as they come online.
Registrator supports pluggable service registries, which currently includes
Consul, etcd and SkyDNS 2.


BuildRequires:  git
BuildRequires:  golang
Requires:       docker


%prep
git clone \
	https://github.com/gliderlabs/registrator \
	registrator/src/github.com/gliderlabs/registrator > /dev/null 2>&1 || :
cd registrator/src/github.com/gliderlabs/registrator
git checkout %{revision}


%build
export GOPATH=`pwd`/registrator
cd registrator/src/github.com/gliderlabs/registrator
go get
go install \
	-ldflags "-X main.Version $(cat VERSION)" \
	github.com/gliderlabs/registrator


%install
mkdir -p \
        %{buildroot}/usr/local/sbin \

install --mode 775 \
        %{_builddir}/registrator/bin/registrator \
        %{buildroot}/usr/local/sbin


mkdir -p %{buildroot}/etc/sysconfig
cat > %{buildroot}/etc/sysconfig/registrator <<'eof'
OPTIONS="-cleanup consul://localhost:8500"
eof
chmod 664 %{buildroot}/etc/sysconfig/registrator


mkdir -p %{buildroot}/usr/lib/systemd/system
cat > %{buildroot}/usr/lib/systemd/system/registrator.service <<'eof'
[Unit]
Description=Registrator
After=network.target remote-fs.target nss-lookup.target docker.service
Requires=docker.service

[Service]
Type=simple
EnvironmentFile=/etc/sysconfig/registrator
Environment="DOCKER_HOST=unix:///var/run/docker.sock"
ExecStart=/usr/local/sbin/registrator $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID
KillSignal=SIGCONT
User=registra

[Install]
WantedBy=multi-user.target
eof
chmod 664 %{buildroot}/usr/lib/systemd/system/registrator.service


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%config(noreplace) /etc/sysconfig/registrator
/usr/lib/systemd/system/registrator.service
/usr/local/sbin/registrator
#%doc


%pre
/usr/sbin/groupadd -r registra > /dev/null 2>&1 || :
/usr/sbin/useradd -r -g registra -G docker -c "Registrator" -d /var/empty \
    	-s /sbin/nologin -M registra > /dev/null 2>&1 || :


%post
if [ $1 -eq 1 ]; then
	/bin/systemctl preset registrator.service > /dev/null 2>&1
fi


%preun
if [ $1 -eq 0 ]; then 
        /bin/systemctl stop registrator.service > /dev/null 2>&1
	/bin/systemctl disable registrator.service > /dev/null 2>&1
fi


%postun
if [ $1 -ge 1 ]; then
	/bin/systemctl try-restart registrator.service > /dev/null 2>&1
fi


%changelog
* Wed May 4 2016 Chris Shiels <chris@mecachis.net> 0.6.4-1.mecachis.centos7
- Initial release.
