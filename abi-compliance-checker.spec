Summary:	API/ABI compatibility checker for C/C++ libraries
Name:		abi-compliance-checker
Version:	1.97.6
Release:	1
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		http://ispras.linuxbase.org/index.php/ABI_compliance_checker
Source0:	https://github.com/lvc/abi-compliance-checker/downloads/abi-compliance-checker-%{version}.tar.gz
Requires:	gcc-c++
Requires:	binutils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ABI Compliance Checker (ACC) is a tool for checking backward binary
and source-level compatibility of a C/C++ library. The tool checks
header files and shared libraries of old and new versions and analyzes
changes in API and ABI (ABI=API+compiler ABI) that may break binary
and/or source compatibility: changes in calling stack, v-table changes,
removed symbols, renamed fields, etc. Binary incompatibility may result
in crashing or incorrect behavior of applications built with an old
version of a library if they run on a new one. Source incompatibility
may result in recompilation errors with a new library version. The
tool is intended for developers of software libraries and maintainers
of operating systems who are interested in ensuring backward
compatibility, i.e. allow old applications to run or to be recompiled
with newer library versions.

%prep
%setup -q
chmod 0644 LICENSE README

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
%doc LICENSE README doc/
%{_bindir}/%{name}
%{_datadir}/%{name}
