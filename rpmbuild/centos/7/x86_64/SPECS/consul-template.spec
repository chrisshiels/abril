# 'consul-template.spec'.
# Chris Shiels.


Name:       consul-template
Version:    0.14.0
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    Mozilla Public License, version 2.0
Vendor:     Mecachis
URL:        https://www.hashicorp.com/blog/introducing-consul-template.html
Summary:    Populate values from Consul into the filesystem


%define debug_package %{nil}


Source0:    https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip


%description
The daemon consul-template queries a Consul instance and updates any number of
specified templates on the filesystem.  As an added bonus, consul-template can
optionally run arbitrary commands when the update process completes.


#BuildRequires:  
#Requires:       


%prep
%setup -n consul-template-0.14.0 -c


%build
:


%install
mkdir -p \
	%{buildroot}/usr/local/etc/consul-template/conf.d \
	%{buildroot}/usr/local/etc/consul-template/templates \
	%{buildroot}/usr/local/sbin


install --mode 775 \
	%{_builddir}/consul-template-0.14.0/consul-template \
	%{buildroot}/usr/local/sbin


mkdir -p %{buildroot}/etc/sysconfig
cat > %{buildroot}/etc/sysconfig/consul-template <<'eof'
OPTIONS=""
eof
chmod 664 %{buildroot}/etc/sysconfig/consul-template


mkdir -p %{buildroot}/usr/lib/systemd/system
cat > %{buildroot}/usr/lib/systemd/system/consul-template.service <<'eof'
[Unit]
Description=Consul Template
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=simple
EnvironmentFile=/etc/sysconfig/consul-template
ExecStart=/usr/local/sbin/consul-template -config /usr/local/etc/consul-template/conf.d $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID
KillSignal=SIGCONT
User=consulte

[Install]
WantedBy=multi-user.target
eof
chmod 664 %{buildroot}/usr/lib/systemd/system/consul-template.service


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%config(noreplace) /etc/sysconfig/consul-template
/usr/lib/systemd/system/consul-template.service
/usr/local/etc/consul-template/conf.d
/usr/local/etc/consul-template/templates
/usr/local/sbin/consul-template
#%doc


%pre
/usr/sbin/groupadd -r consulte > /dev/null 2>&1 || :
/usr/sbin/useradd -r -g consulte -c "Consul Template" -d /var/empty \
	-s /sbin/nologin -M consulte > /dev/null 2>&1 || :


%post
if [ $1 -eq 1 ]; then
	/bin/systemctl preset consul-template.service > /dev/null 2>&1
fi


%preun
if [ $1 -eq 0 ]; then 
	/bin/systemctl stop consul-template.service > /dev/null 2>&1
	/bin/systemctl disable consul-template.service > /dev/null 2>&1
fi


%postun
if [ $1 -ge 1 ]; then
	/bin/systemctl try-restart consul-template.service > /dev/null 2>&1
fi


%changelog
* Wed May 4 2016 Chris Shiels <chris@mecachis.net> 0.14.0-1.mecachis.centos7
- Initial release.
