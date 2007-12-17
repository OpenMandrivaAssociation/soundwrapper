Name: soundwrapper
Version:	1.5
Release:	%mkrel 3
Summary:	Directs a program's sound output to aRts or esd
Source0:	%{name}-%{version}.tar.bz2
License:	LGPL
Group:		System/Base
Prefix:		%{_prefix}
BuildRequires:	libarts-devel 
BuildRequires: esound-devel
Conflicts:  menu < 2.1.12-9mdk

%description
When placed before a command to run a program with some audio component,
that program's audio output is redirected to the aRts or EsounD sound
servers if either of them is in control of the sound device

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



