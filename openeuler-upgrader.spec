Name:		openeuler-upgrade
Version:	0.1.0
Release:	1%{?dist}
Summary:	Upgrade openEuler to next version using dnf upgrade (unofficial tool)

License:	MulanPSL2
URL:		https://gitee.com/openeuler/openeuler-upgrade.git
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	dnf
Requires:	dnf-plugins-core


%description
Upgrade openEuler to next version using dnf upgrade.
This is an unofficial tool


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m755 openeuler-upgrade %{buildroot}%{_sbindir}

%files
%license LICENSE
%doc README.md
%{_sbindir}/openeuler-upgrade


%changelog
* Mon Sep 29 2024 Your Name <cheayuki13@gmail.com> - 0.1.0-1
- Initial release of the openeuler-upgrade tool
- Implements basic system upgrade functionality using dnf
- Ensures compatibility with openEuler 22.03 LTS to 23.09
- Adds basic logging and error handling capabilities

