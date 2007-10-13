%define prerel rc3

Name:		asio
Version:	0.3.8
Release:	%mkrel -c %prerel 1
Summary:	asio
Group:		Development/C
License:	Boost Software License 1.0
Source0:	http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%version%prerel.tar.bz2
URL:		http://asio.sourceforge.net
BuildRequires:  boost-devel openssl-devel

%description
asio is a cross-platform C++ library for network programming that provides
developers with a consistent asynchronous I/O model using a modern C++
approach.

%prep
%setup -n %name-%version%prerel -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%check
make check

%files
%defattr(-,root,root)
%doc COPYING README THANKS
%doc doc/*
%_includedir/*.hpp
%_includedir/%{name}
