%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - Core system for terminals
Summary(pl):	Podstawowy system dla terminali z Linux Terminal Server Project
Name:		ltsp_rdesktop
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-rdesktop-1.6-0-%{_arch}.tgz
# Source1-md5:	97fbeac51118c781bdd8f63eeea8d012
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains rdesktop for LTSP terminals.

%description -l pl
- Jak obni�y� koszty I ocali� planet�?
- Przekszta�ci� te stare pecety na X-terminale z u�yciem LTSP.

Ten pakiet zawiera zdalny desktop dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
cd i386
cp -r {etc,usr} $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/etc/screen.d
%dir %{_ltspdir}/usr
%attr(755,root,root) %{_ltspdir}/usr/bin
%{_ltspdir}/usr/man
%{_ltspdir}/usr/share
