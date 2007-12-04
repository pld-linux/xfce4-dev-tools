# $Revision: 1.17 $Date: 2007-12-04 16:41:14 $
Summary:	Xfce development tools
Summary(pl.UTF-8):	Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.4.0.1
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/archive/xfce-4.4.2/src/%{name}-%{version}.tar.bz2
# Source0-md5:	7d09d161efc7ef86b3b48791d98c8ae8
URL:		http://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	automake
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
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
