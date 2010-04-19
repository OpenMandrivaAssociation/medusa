%define	name	medusa
%define	version	2.0
%define	release	%mkrel 1
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Medusa Parallel Network Login Auditor
License:	GPLv2
Group:		Monitoring
URL:		http://www.foofus.net/jmk/medusa/medusa.html
Source0:	http://www.foofus.net/jmk/tools/%{name}-%{version}.tar.gz
BuildRequires:  openssl-devel
BuildRequires:  ssh2-devel
BuildRequires:  ncpfs-devel
BuildRequires:  subversion-devel
BuildRequires:  postgresql-devel
BuildRequires:  pcre-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Medusa is intended to be a speedy, massively parallel, modular, login
brute-forcer. The goal is to support as many services which allow remote
authentication as possible. The author considers following items as some of the
key features of this application:
* Thread-based parallel testing. Brute-force testing can be performed against
  multiple hosts, users or passwords concurrently.
* Flexible user input. Target information (host/user/password) can be specified
  in a variety of ways. For example, each item can be either a single entry or
  a file containing multiple entries. Additionally, a combination file format
  allows the user to refine their target listing.
* Modular design. Each service module exists as an independent .mod file. This
  means that no modifications are necessary to the core application in order to
  extend the supported list of services for brute-forcing. 

%prep
%setup -q

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/medusa
%{_libdir}/medusa
%{_mandir}/man1/medusa.1*

