#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	TripleDES
Summary:	Crypt::TripleDES Perl module - pure Perl Triple DES implementation
Summary(pl):	Modu³ Perla Crypt::TripleDES - czysto perlowa implementacja Triple DES
Name:		perl-Crypt-TripleDES
Version:	0.24
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements 3DES encryption in ECB mode. The code is based
on Eric Young's implementation of DES in pure perl. It's quite slow
because of the way Perl handles bit operations and is not recommended
for use with large texts.

%description -l pl
Ten modu³ jest implementacj± szyfrowania 3DES w trybie ECB. Kod bazuje
na czysto perlowej implementacji DES Erica Younga. Jest dosyæ wolny ze
wzglêdu na sposób obs³ugi operacji bitowych przez interpreter i nie
jest zalecany do u¿ycia z du¿ymi tekstami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Crypt/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
