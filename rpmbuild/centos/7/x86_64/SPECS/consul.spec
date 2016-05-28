# 'consul.spec'.
# Chris Shiels.


Name:       consul
Version:    0.6.4
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    Mozilla Public License, version 2.0
Vendor:     Mecachis
URL:        https://www.consul.io/
Summary:    Consul service discovery and configuration


%define debug_package %{nil}


Source0:    https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip


%description
Consul is a tool for service discovery and configuration.  Consul is
distributed, highly available, and extremely scalable.


#BuildRequires:  
#Requires:       


%prep
%setup -n consul-0.6.4 -c


%build
:


%install
mkdir -p \
	%{buildroot}/usr/local/etc/consul/conf.d \
	%{buildroot}/usr/local/sbin \
	%{buildroot}/usr/local/var/lib/consul


install --mode 775 \
	%{_builddir}/consul-0.6.4/consul \
	%{buildroot}/usr/local/sbin


mkdir -p %{buildroot}/etc/sysconfig
cat > %{buildroot}/etc/sysconfig/consul <<'eof'
OPTIONS="-dev"
eof
chmod 664 %{buildroot}/etc/sysconfig/consul


mkdir -p %{buildroot}/usr/lib/systemd/system
cat > %{buildroot}/usr/lib/systemd/system/consul.service <<'eof'
[Unit]
Description=Consul
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=simple
EnvironmentFile=/etc/sysconfig/consul
ExecStart=/usr/local/sbin/consul agent -config-dir /usr/local/etc/consul/conf.d $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID
KillSignal=SIGCONT
User=consul

[Install]
WantedBy=multi-user.target
eof
chmod 664 %{buildroot}/usr/lib/systemd/system/consul.service


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%config(noreplace) /etc/sysconfig/consul
/usr/lib/systemd/system/consul.service
/usr/local/etc/consul/conf.d
/usr/local/sbin/consul
%attr(750, consul, consul) /usr/local/var/lib/consul
#%doc


%pre
/usr/sbin/groupadd -r consul > /dev/null 2>&1 || :
/usr/sbin/useradd -r -g consul -c "Consul" -d /var/empty \
    	-s /sbin/nologin -M consul > /dev/null 2>&1 || :


%post
if [ $1 -eq 1 ]; then
	/bin/systemctl preset consul.service > /dev/null 2>&1
fi


%preun
if [ $1 -eq 0 ]; then 
        /bin/systemctl stop consul.service > /dev/null 2>&1
	/bin/systemctl disable consul.service > /dev/null 2>&1
fi


%postun
if [ $1 -ge 1 ]; then
	/bin/systemctl try-restart consul.service > /dev/null 2>&1
fi


%changelog
* Wed May 4 2016 Chris Shiels <chris@mecachis.net> 0.6.4-1.mecachis.centos7
- Initial release.
