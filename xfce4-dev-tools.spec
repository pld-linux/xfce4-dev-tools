# $Revision: 1.3 $Date: 2005-03-15 13:49:22 $
%define		_rel	cvs
Summary:	Xfce development tools
Summary(pl):	Narzêdzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.0
Release:	0.%{_rel}.1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/~benny/trials/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	dcdea5e5b5215687e72f080f766c5b07
URL:		http://www.xfce.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from CVS. In
addition it contains the Xfce developer's handbook.

%description -l pl
Narzêdzia programistyczne Xfce s± zbiorem programów oraz makr
przeznaczonych dla deweloperów Xfce oraz ludzi którzy chc± zbudowaæ
Xfce z CVSa. Dodatkowo zawiera podrêcznik dewelopera Xfce.

%prep
%setup -q -n %{name}-%{version}%{_rel}

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
%{_datadir}/xfce4/dev-tools/m4macros/*
