Name: xfsinfo
Version: 1.0.3
Release: 8
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
%setup -q -n %{name}-%{version}

%build
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfsinfo
%{_mandir}/man1/xfsinfo.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 671316
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592586
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2010.1
+ Revision: 524444
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-3mdv2009.1
+ Revision: 351149
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2009.0
+ Revision: 266086
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 211787
- New version

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154737
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode lzma extension!!!

* Mon Jul 09 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-4mdv2008.0
+ Revision: 50740
- fix package description
- minor %%build cleanup


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

