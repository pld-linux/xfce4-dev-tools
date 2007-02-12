# $Revision: 1.8.2.5 $Date: 2007-02-12 13:20:16 $
Summary:	Xfce development tools
Summary(pl.UTF-8):   Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.90.2
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	2cf48dc426f971896c955bc197fe0b68
URL:		http://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from CVS. In
addition it contains the Xfce developer's handbook.

%description -l pl.UTF-8
Narzędzia programistyczne Xfce są zbiorem programów oraz makr
przeznaczonych dla programistów Xfce oraz ludzi którzy chcą zbudować
Xfce z CVS-u. Dodatkowo zawiera podręcznik programisty Xfce.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	macrodir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
