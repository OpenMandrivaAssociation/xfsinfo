Name: xfsinfo
Version: 1.0.6
Release: 1
Summary: X font server information utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(libfs) >= 1.0.0
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xfsinfo is an utility for displaying information about an X font server, such
as the list of capabilities, catalogues, alternate servers and more.

%prep
%autosetup -p1

%build
%configure

%make_build

%install
%make_install

%files
%{_bindir}/xfsinfo
%{_mandir}/man1/xfsinfo.1*
