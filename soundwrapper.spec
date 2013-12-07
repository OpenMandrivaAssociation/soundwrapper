%define name soundwrapper
%define version 1.6
%define release 11

Summary:	Directs a program's sound output to Pulse, ALSA, aRts, or esd
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0: soundwrapper-1.6-arts-disable.patch
License:	LGPL
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:            http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/SPECS/%{name}/
BuildRequires: pkgconfig(libpulse)
BuildRequires: alsa-oss-devel
BuildRequires: esound-devel
Conflicts:  menu < 2.1.12-9mdk

%description
When placed before a command to run a program with some audio component,
that program's audio output is redirected to the ALSA sound device or to
the PulseAudio, aRts, or EsounD sound servers if either of them is in control
of the sound device, enabling programs to play sounds at the same time

%prep
%setup -q
%patch0 -p0

aclocal
automake --add-missing
autoconf

%build
export CFLAGS="%{optflags} -I%{_kde3_includedir}"
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/soundwrapper





%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6-7mdv2011.0
+ Revision: 670003
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-6mdv2011.0
+ Revision: 607552
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-5mdv2010.1
+ Revision: 524117
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.6-4mdv2010.0
+ Revision: 427205
- rebuild

* Mon Feb 09 2009 Helio Chissini de Castro <helio@mandriva.com> 1.6-3mdv2009.1
+ Revision: 338900
- Adios arts..

* Wed Dec 24 2008 Adam Williamson <awilliamson@mandriva.org> 1.6-2mdv2009.1
+ Revision: 318226
- buildrequires kde3-macros (for kde3_includedir)
- quick fix for arts header location

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Feb 07 2008 Frederic Crozat <fcrozat@mandriva.com> 1.6-1mdv2008.1
+ Revision: 163690
- Release 1.6 : add suport for PulseAudio using padsp
- Remove patch0, better handled in version 1.6 directly

* Fri Jan 04 2008 Frederic Crozat <fcrozat@mandriva.com> 1.5-4mdv2008.1
+ Revision: 144917
- Patch0: add support for PulseAudio

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Sep 11 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-09-11 16:04:43 (60827)
- Remove explicit aoss dependency. Drak tools should know when to install it as
  reported by David Walser

* Tue Sep 05 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-09-05 22:48:14 (60173)
- Added aoss as a requires to alsa, since code relies on this, otherwise alsa
  test is useless.
- Add %%mkrel

* Tue Sep 05 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-09-05 21:31:23 (60165)
- import soundwrapper-1.5-1mdk

* Sat Dec 03 2005 David Walser <luigiwalser@yahoo.com> 1.5-1mdk
- don't return immediately if execvp fails

* Sun Nov 20 2005 David Walser <luigiwalser@yahoo.com> 1.4-1mdk
- add support for ALSA using aoss

* Fri Sep 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-3mdk
- add conflict in order to ease update

* Thu Sep 02 2004 Olivier Blin <blino@mandrake.org> 1.3-2mdk
- fix linking

* Thu Aug 26 2004 David Walser <luigiwalser@yahoo.com> 1.3-1mdk
- fix braces (silly emacs :o) (thanks blino)
- don't use absolute filenames for libs, it breaks 64bit arches (thanks blino)

* Wed Aug 25 2004 David Walser <luigiwalser@yahoo.com> 1.2-1mdk
- use dlopen() to avoid direct requires on libesd/libartsc

* Sun Apr 25 2004 David Walser <luigiwalser@yahoo.com> 1.1-1mdk
- fix stupid bug

