#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	TripleDES
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::TripleDES Perl module - pure Perl Triple DES implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::TripleDES - czysto perlowa implementacja Triple DES
Name:		perl-Crypt-TripleDES
Version:	0.24
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	90b562175a8f6c5f6bc3eacaddffbcde
URL:		http://search.cpan.org/dist/Crypt-TripleDES/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements 3DES encryption in ECB mode. The code is based
on Eric Young's implementation of DES in pure perl. It's quite slow
because of the way Perl handles bit operations and is not recommended
for use with large texts.

%description -l pl.UTF-8
Ten moduł jest implementacją szyfrowania 3DES w trybie ECB. Kod bazuje
na czysto perlowej implementacji DES Erica Younga. Jest dosyć wolny ze
względu na sposób obsługi operacji bitowych przez interpreter i nie
jest zalecany do użycia z dużymi tekstami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Crypt/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
