# 'docker-compose.spec'.
# Chris Shiels.


Name:       docker-compose
Version:    1.7.0
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    Apache License Version 2.0
Vendor:     Mecachis
URL:        https://docs.docker.com/compose/
Summary:    Tool for defining and running multi-container Docker applications


#Source0:    


%define __os_install_post %{nil}


%description
Compose is a tool for defining and running multi-container Docker applications.
With Compose, you use a Compose file to configure your application's services.
Then, using a single command, you create and start all the services from your
configuration.


#BuildRequires:  
Requires:       python35u


%prep
:


%build
:


%install
python3.5 -m venv %{buildroot}/usr/local/docker-compose
(
	. %{buildroot}/usr/local/docker-compose/bin/activate
	python3.5 %{buildroot}/usr/local/docker-compose/bin/pip \
		install docker-compose==%{version}
)


sed -i -e "s!%{buildroot}!!" \
	%{buildroot}/usr/local/docker-compose/bin/activate \
	%{buildroot}/usr/local/docker-compose/bin/activate.csh \
	%{buildroot}/usr/local/docker-compose/bin/activate.fish \
	%{buildroot}/usr/local/docker-compose/bin/docker-compose \
	%{buildroot}/usr/local/docker-compose/bin/easy_install \
	%{buildroot}/usr/local/docker-compose/bin/easy_install-3.5 \
	%{buildroot}/usr/local/docker-compose/bin/jsonschema \
	%{buildroot}/usr/local/docker-compose/bin/pip \
	%{buildroot}/usr/local/docker-compose/bin/pip3 \
	%{buildroot}/usr/local/docker-compose/bin/pip3.5 \
	%{buildroot}/usr/local/docker-compose/bin/wsdump.py


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
/usr/local/docker-compose


%changelog
* Wed May 4 2016 Chris Shiels <chris@mecachis.net> 1.45-1.mecachis.centos7
- Initial release.
