Name:		asio
Version:	0.3.9
Release:	%mkrel 1
Summary:	asio
Group:		Development/C
License:	Boost Software License 1.0
Source0:	http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%version.tar.bz2
URL:		http://asio.sourceforge.net
BuildRequires:  boost-devel >= 1.33
BuildRequires:	openssl-devel
BuildRequires:	boost-devel >= 1.33
BuildRequires:	openssl-devel

%description
asio is a cross-platform C++ library for network programming that provides
developers with a consistent asynchronous I/O model using a modern C++
approach.

%prep
%setup -n %name-%version -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%check
make check

%files
%defattr(-,root,root)
%doc README
%doc doc/*
%_includedir/*.hpp
%_includedir/%{name}
