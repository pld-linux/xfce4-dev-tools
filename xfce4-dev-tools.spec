# $Revision: 1.5 $Date: 2005-03-16 19:06:23 $
%define		_rel	cvs
Summary:	Xfce development tools
Summary(pl):	Narzêdzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.0
Release:	0.%{_rel}.2
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/~benny/trials/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	dcdea5e5b5215687e72f080f766c5b07
Patch0:		%{name}-xdt-autogen_bash_fix.patch
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
%setup -q -n %{name}-%{version}%{_rel}
%patch0 -p1

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
