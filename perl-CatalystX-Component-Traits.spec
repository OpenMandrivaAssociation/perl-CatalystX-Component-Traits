%define upstream_name    CatalystX-Component-Traits
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Automatic Trait Loading and Resolution for
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CatalystX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Pluggable)          >= 3.900.0
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(MooseX::Traits::Pluggable)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}
Requires: perl(MooseX::Traits::Pluggable)

%description
Adds a the Catalyst::Component/COMPONENT manpage method to your the
Catalyst manpage component base class that reads the optional 'traits'
parameter from app and component config and instantiates the component
subclass with those traits using the MooseX::Traits/new_with_traits manpage
from the MooseX::Traits::Pluggable manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
