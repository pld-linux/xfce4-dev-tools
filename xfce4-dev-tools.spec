Summary:	Xfce development tools
Summary(pl.UTF-8):	Narzędzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.14.0
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://archive.xfce.org/src/xfce/xfce4-dev-tools/4.14/%{name}-%{version}.tar.bz2
# Source0-md5:	5f8fc8af73819c08d9e4c26a3ac457e7
URL:		http://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.42.0
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
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/xdt-autogen
%attr(755,root,root) %{_bindir}/xdt-csource
%{_aclocaldir}/xdt-*.m4
