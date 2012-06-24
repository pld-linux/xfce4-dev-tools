# $Revision: 1.7 $Date: 2005-11-13 22:25:33 $
Summary:	Xfce development tools
Summary(pl):	Narz�dzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.0
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.foo-projects.org/~benny/files/xfce4-dev-tools/4.3/%{name}-%{version}.tar.bz2
# Source0-md5:	42b2fe6056bc5525cc5448979bef3301
URL:		http://www.home.unix-ag.org/bmeurer/projects/xfce4-dev-tools/
Requires:	libxfce4util >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from CVS. In
addition it contains the Xfce developer's handbook.

%description -l pl
Narz�dzia programistyczne Xfce s� zbiorem program�w oraz makr
przeznaczonych dla programist�w Xfce oraz ludzi kt�rzy chc� zbudowa�
Xfce z CVS-u. Dodatkowo zawiera podr�cznik programisty Xfce.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xfce4/dev-tools
