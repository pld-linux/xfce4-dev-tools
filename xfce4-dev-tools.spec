# $Revision: 1.6 $Date: 2005-04-14 00:41:12 $
%define		_snap	20050410
Summary:	Xfce development tools
Summary(pl):	Narzêdzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.0
Release:	0.%{_snap}.1
License:	GPL v2
Group:		Development/Building
Source0:	http://spuriousinterrupt.org/projects/xfmedia/files/%{name}-%{_snap}.tar.bz2
# Source0-md5:	84d6b95d3d02f023c679e02addf0068f
URL:		http://www.xfce.org/
Requires:	libxfce4util >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from CVS. In
addition it contains the Xfce developer's handbook.

%description -l pl
Narzêdzia programistyczne Xfce s± zbiorem programów oraz makr
przeznaczonych dla programistów Xfce oraz ludzi którzy chc± zbudowaæ
Xfce z CVS-u. Dodatkowo zawiera podrêcznik programisty Xfce.

%prep
%setup -q -n %{name}-%{_snap}

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
