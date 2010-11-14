# $Revision: 1.19.2.1 $Date: 2010-11-14 12:16:18 $
Summary:	Xfce development tools
Summary(pl.UTF-8):	Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.7.3
Release:	0.1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/archive/xfce/4.8pre1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	38ac952d738634d98566014168e90890
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
%attr(755,root,root) %{_bindir}/xdt-autogen
%attr(755,root,root) %{_bindir}/xdt-commit
%{_aclocaldir}/*.m4
