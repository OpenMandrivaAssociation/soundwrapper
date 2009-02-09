%define name soundwrapper
%define version 1.6
%define release %mkrel 3

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
BuildRequires: libpulseaudio-devel 
BuildRequires: libalsa-devel 
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



