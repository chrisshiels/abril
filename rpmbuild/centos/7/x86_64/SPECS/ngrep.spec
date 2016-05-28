# 'ngrep.spec'.
# Chris Shiels.


Name:       ngrep
Version:    1.45
Release:    1.mecachis.centos7
BuildArch:  x86_64
Group:      Mecachis
License:    Author
Vendor:     Mecachis
URL:        http://ngrep.sourceforge.net/
Summary:    Network grep


Source0:    http://prdownloads.sourceforge.net/ngrep/ngrep-1.45.tar.bz2


%description
ngrep strives to provide most of GNU grep's common features, applying
them to the network layer.  ngrep is a pcap-aware tool that will allow
you to specify extended regular expressions to match against data payloads
of packets.  It currently recognizes TCP, UDP and ICMP across
Ethernet, PPP, SLIP, FDDI and null interfaces, and understands bpf filter
logic in the same fashion as more common packet sniffing tools,
such as tcpdump(8) and snoop(1).


BuildRequires:  libpcap-devel
Requires:       libpcap


%prep
%setup -n ngrep-1.45


%build
./configure \
	--prefix=/usr/local \
	--with-pcap-includes=/usr/include/pcap
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
/usr/local/bin/ngrep
/usr/local/share/man/man8/ngrep.8
%doc LICENSE.txt
%doc doc/CHANGES.txt
%doc doc/CREDITS.txt
%doc doc/INSTALL.txt
%doc doc/README.txt
%doc doc/REGEX.txt


%changelog
* Wed May 4 2016 Chris Shiels <chris@mecachis.net> 1.45-1.mecachis.centos7
- Initial release.
