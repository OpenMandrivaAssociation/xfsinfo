Name: xfsinfo
Version: 1.0.1
Release: %mkrel 3
Summary: X font server information utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfs-devel >= 1.0.0
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xfsinfo is a utility for displaying information about an X font server.
It is used to examine the capabilities of a server,

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfsinfo
%{_mandir}/man1/xfsinfo.1x.bz2

