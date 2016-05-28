# 'golang.spec'.
# Chris Shiels.


Name:       golang
Version:    1.6.2
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    Author
Vendor:     Mecachis
URL:        https://golang.org/
Summary:    The Go Programming Language


Source0:    https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz


%define debug_package %{nil}
%define __os_install_post %{nil}


%description
The Go Programming Language.


AutoReqProv:    no
#BuildRequires:  
#Requires:       


%prep
%setup -n go


%build
:


%install
# Remove unneeded files causing dependency on /bin/rc - I can't work out a
# better way to workaround this...
rm -v src/*.rc

mkdir -p %{buildroot}/usr/local/go
cp -a . %{buildroot}/usr/local/go


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
/usr/local/go


%changelog
* Sat May 7 2016 Chris Shiels <chris@mecachis.net> 1.6.2-1.mecachis.centos7
- Initial release.
