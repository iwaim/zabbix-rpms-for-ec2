Name:           ec2-zabbix-release
Version:        1
Release:        1
Summary:        Zabbix Packages for Amazon Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

URL:            https://dl.dropboxusercontent.com/u/5110926/
Source0:        ec2-zabbix.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains the Zabbix Packages for Amazon Linux repository

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Sun Mar 30 2014 IWAI, Masaharu <iwaim.sub@gmail.com>
- initial release

