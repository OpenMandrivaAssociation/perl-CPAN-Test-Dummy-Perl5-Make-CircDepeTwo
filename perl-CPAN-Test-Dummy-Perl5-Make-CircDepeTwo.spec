%define module	CPAN-Test-Dummy-Perl5-Make-CircDepeTwo
%define name	perl-%{module}
%define version 1.00
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/CPAN/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
This module is part of CPAN.pm with the single purpose of testing 
CPAN.pm itself.
Contains no functionality, and will never do so.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/
%{_mandir}/*/*


