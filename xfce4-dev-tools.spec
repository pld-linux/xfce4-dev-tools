# $Revision: 1.11 $Date: 2006-09-06 07:40:46 $
Summary:	Xfce development tools
Summary(pl):	Narz�dzia programistyczne Xfce
Name:		xfce4-dev-tools
Version:	4.3.99.1
Release:	1
License:	GPL v2
Group:		Development/Building
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	dc6403caf82edfb896eb3878385b439a
URL:		http://xfce.org/~benny/projects/xfce4-dev-tools/
BuildRequires:	automake
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
	DESTDIR=$RPM_BUILD_ROOT \
	macrodir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*.m4
