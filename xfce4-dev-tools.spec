Summary:	Xfce development tools
Summary(pl.UTF-8):	Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.20.0
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	bea58046e67b4274c022fcff893fa350
URL:		https://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.72.0
Conflicts:	autoconf < 2.60
Conflicts:	pkgconfig < 1:0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build Xfce from Git. In
addition it contains the Xfce developer's handbook.

%description -l pl.UTF-8
Narzędzia programistyczne Xfce są zbiorem programów oraz makr
przeznaczonych dla programistów Xfce oraz ludzi którzy chcą zbudować
Xfce z repozytorium Git. Dodatkowo zawiera podręcznik programisty
Xfce.

%prep
%setup -q
%{__sed} -i '1s,/usr/bin/env bash$,%{__bash},' \
		helpers/{xfce-do-release.in,xfce-get-release-notes,xfce-get-translations,xfce-update-news}

%{__sed} -i '1s,/usr/bin/env python3$,%{__python3},' \
		scripts/xdt-gen-visibility

%build
%configure \
	--disable-silent-rules
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
%doc AUTHORS ChangeLog HACKING NEWS
%{_mandir}/man1/xdt-csource.1*
%attr(755,root,root) %{_bindir}/xdt-autogen
%attr(755,root,root) %{_bindir}/xdt-check-abi
%attr(755,root,root) %{_bindir}/xdt-csource
%attr(755,root,root) %{_bindir}/xdt-gen-visibility
%attr(755,root,root) %{_bindir}/xfce-build
%attr(755,root,root) %{_bindir}/xfce-do-release
%attr(755,root,root) %{_bindir}/xfce-get-release-notes
%attr(755,root,root) %{_bindir}/xfce-get-translations
%attr(755,root,root) %{_bindir}/xfce-update-news
%{_aclocaldir}/xdt-*.m4
