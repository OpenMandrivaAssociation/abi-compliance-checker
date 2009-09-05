Summary:	ABI compliance checker
Name:		abi-compliance-checker
Version:	1.6
Release:	%mkrel 1
Group:		Development/Other
License:	GPL
URL:		http://ispras.linux-foundation.org/index.php/ABI_compliance_checker
Source0:	http://ispras.linux-foundation.org/images/b/ba/Abi-compliance-checker-%{version}.tar.gz
Requires:	gcc
Requires:	binutils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ABI-compliance-checker is a lightweight tool for checking backward binary
compatibility of shared C/C++ libraries in OS Linux. It checks interface
signatures and data type definitions in two library versions (headers and
shared objects) and searches differences that may lead to incompatibility
according to ABI standards. Breakage of the compatibility may result in
crashing or incorrect behavior of applications built with an old version of
a library when it is running with a new one. ABI-compliance-checker was
intended for library developers that are interested in ensuring backward
binary compatibility. Also ABI-compliance-checker may be used for checking
forward binary compatibility and compliance checking of the same library
versions on different linux distributions.

%prep

%setup -q
chmod 644 abi-compliance-checker.pl LICENSE

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 abi-compliance-checker.pl %{buildroot}%{_bindir}/abi-compliance-checker

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/abi-compliance-checker
