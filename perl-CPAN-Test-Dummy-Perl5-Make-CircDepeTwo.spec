%define upstream_name	 CPAN-Test-Dummy-Perl5-Make-CircDepeTwo
Name:		perl-%{upstream_name}
Version:	1.00
Release:	10

Summary:	%{upstream_name} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/A/AN/ANDK/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is part of CPAN.pm with the single purpose of testing 
CPAN.pm itself.
Contains no functionality, and will never do so.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/
%{_mandir}/*/*
