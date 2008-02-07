%define name soundwrapper
%define version 1.6
%define release %mkrel 1

Summary:	Directs a program's sound output to Pulse, ALSA, aRts, or esd
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	LGPL
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:            http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/SPECS/%{name}/
BuildRequires:	libpulseaudio-devel libalsa-devel libarts-devel esound-devel
Conflicts:  menu < 2.1.12-9mdk

%description
When placed before a command to run a program with some audio component,
that program's audio output is redirected to the ALSA sound device or to
the PulseAudio, aRts, or EsounD sound servers if either of them is in control
of the sound device, enabling programs to play sounds at the same time

%prep
%setup -q

aclocal
automake --add-missing
autoconf

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/soundwrapper



