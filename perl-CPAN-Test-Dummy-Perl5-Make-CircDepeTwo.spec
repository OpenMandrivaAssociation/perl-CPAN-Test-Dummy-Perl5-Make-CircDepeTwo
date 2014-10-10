%define upstream_name	 CPAN-Test-Dummy-Perl5-Make-CircDepeTwo
%define upstream_version 1.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	%{upstream_name} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is part of CPAN.pm with the single purpose of testing 
CPAN.pm itself.
Contains no functionality, and will never do so.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.0-6mdv2011.0
+ Revision: 654881
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-5mdv2011.0
+ Revision: 504831
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2010.0
+ Revision: 430344
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.00-3mdv2009.0
+ Revision: 256187
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 15 2007 Stéphane Téletchéa <steletch@mandriva.org> 1.00-1mdv2008.1
+ Revision: 108987
- import perl-CPAN-Test-Dummy-Perl5-Make-CircDepeTwo


