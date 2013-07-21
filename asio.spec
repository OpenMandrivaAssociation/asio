Name:		asio
Version:	1.5.3
Release:	1
Summary:	Cross-platform C++ library for network programming
Group:		Development/C
License:	Boost
Source0:	https://sourceforge.net/projects/asio/files/asio/1.5.3%20%28Development%29/%{name}-%{version}.tar.bz2
URL:		http://asio.sourceforge.net
BuildRequires:	boost-devel >= 1.33
BuildRequires:	pkgconfig(openssl)

%description
asio is a cross-platform C++ library for network programming that provides
developers with a consistent asynchronous I/O model using a modern C++
approach.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%check
# Disable tests for now as 2 of them fail at ABF but pass at local machines
#make check

%files
%doc README
%doc doc/*
%{_includedir}/*.hpp
%{_includedir}/%{name}


%changelog
* Wed Sep 28 2011 Andrey Bondrov <abondrov@mandriva.org> 1.4.8-1mdv2012.0
+ Revision: 701710
- New version: 1.4.8

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 1.4.5-1mdv2011.0
+ Revision: 554382
- update to new version 1.4.5

* Mon Jun 01 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.1-1mdv2010.0
+ Revision: 381774
- update to new version 1.4.1
- fix license (Boost)
- add clean section / delete buildroot before install

* Sun Dec 21 2008 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2009.1
+ Revision: 316879
- New version 1.2.0

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.3.9-3mdv2009.0
+ Revision: 226179
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.3.9-2mdv2008.1
+ Revision: 168118
- put a real summary
- fix no-buildroot-tag

* Sat Jan 19 2008 Funda Wang <fwang@mandriva.org> 0.3.9-1mdv2008.1
+ Revision: 155055
- New version 0.3.9

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.3.8-0.rc3.1mdv2008.1
+ Revision: 97818
- import asio



