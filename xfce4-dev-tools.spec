Summary:	Xfce development tools
Summary(pl.UTF-8):	Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.18.1
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.18/%{name}-%{version}.tar.bz2
# Source0-md5:	69b4cd255a0b8f12bbdc9b10c433b223
URL:		https://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.50.0
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
		helpers/{xfce-get-release-notes,xfce-update-news,xfce-do-release,xfce-get-translations}

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
%attr(755,root,root) %{_bindir}/xdt-csource
%attr(755,root,root) %{_bindir}/xfce-build
%attr(755,root,root) %{_bindir}/xfce-do-release
%attr(755,root,root) %{_bindir}/xfce-get-release-notes
%attr(755,root,root) %{_bindir}/xfce-get-translations
%attr(755,root,root) %{_bindir}/xfce-update-news
%{_aclocaldir}/xdt-*.m4
