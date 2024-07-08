%define _disable_rebuild_configure 1

Name:		asio
Version:	1.30.2
Release:	1
Summary:	Cross-platform C++ library for network programming

Group:		Development/C
License:	Boost
Source0:	http://sourceforge.net/projects/asio/files/asio/%{version}%20%28Stable%29/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
URL:		http://asio.sourceforge.net
# Also:
# https://github.com/chriskohlhoff/asio
# https://think-async.com/Asio/
BuildRequires:	boost-devel >= 1.33
BuildRequires:	pkgconfig(openssl)

%define debug_package %{nil}

%description
asio is a cross-platform C++ library for network programming that provides
developers with a consistent asynchronous I/O model using a modern C++
approach.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%check
# Disable tests for now as 2 of them fail at ABF but pass at local machines
#make check

%files
%doc README
%doc doc/*
%{_includedir}/*.hpp
%{_includedir}/%{name}
%{_libdir}/pkgconfig/asio.pc
