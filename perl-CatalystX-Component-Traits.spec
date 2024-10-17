%define upstream_name    CatalystX-Component-Traits
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Automatic Trait Loading and Resolution for
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CatalystX/CatalystX-Component-Traits-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Pluggable)          >= 3.900.0
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Traits::Pluggable)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch
Requires:	perl(MooseX::Traits::Pluggable)

%description
Adds a the Catalyst::Component/COMPONENT manpage method to your the
Catalyst manpage component base class that reads the optional 'traits'
parameter from app and component config and instantiates the component
subclass with those traits using the MooseX::Traits/new_with_traits manpage
from the MooseX::Traits::Pluggable manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 653555
- rebuild for updated spec-helper

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 573790
- update to 0.16

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 462864
- update to 0.14

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 461727
- update to 0.12

* Sat Aug 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 422083
- update to 0.10

* Thu Aug 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 421618
- update to 0.09

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 409025
- adding missing buildrequires:
- update to 0.08
- update to 0.06

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 396754
- update to 0.04
- fixed license field

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-2mdv2010.0
+ Revision: 390075
- fix dependencies

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 387917
- import perl-CatalystX-Component-Traits


* Sun Jun 21 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


