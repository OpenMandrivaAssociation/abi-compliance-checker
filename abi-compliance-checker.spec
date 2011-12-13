Summary:	API/ABI compatibility checker for C/C++ libraries
Name:		abi-compliance-checker
Version:	1.96
Release:	%mkrel 1
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		http://forge.ispras.ru/projects/abi-compliance-checker
Source0:	http://forge.ispras.ru/attachments/download/1277/abi-compliance-checker-%{version}.tar.gz
Requires:	gcc
Requires:	binutils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ABI Compliance Checker (ACC) is a tool for checking backward binary
compatibility of a shared C/C++ library API. The tool checks header
files and shared libraries of old and new versions and analyzes changes
in Application Binary Interface (ABI=API+compiler ABI) that may break
binary compatibility: changes in calling stack, v-table changes, removed
symbols, etc. Binary incompatibility may result in crashing or incorrect
behavior of applications built with an old version of the library if
they run on a new one. The tool is intended for library developers and
operating system maintainers who are interested in ensuring binary
compatibility, i.e. allow old applications to run with newer library
versions without the need to recompile.

%prep

%setup -q
chmod -x LICENSE.txt

%build
# Nothing to build.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt doc/
%{_bindir}/%{name}
%{_datadir}/%{name}
