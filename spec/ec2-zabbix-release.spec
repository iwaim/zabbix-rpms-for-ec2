%define dist .ec2
%define amzn 1

Name:           ec2-zabbix-release
Version:        1.1
Release:        1%{?dist}
Summary:        Zabbix Packages for Amazon Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

URL:            http://www.beering.jp/repos/
Source0:        ec2-zabbix.repo
Source1:        GPL
Source2:        RPM-GPG-KEY-ec2-zabbix-amzn1

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains the Zabbix Packages for Amazon Linux repository

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
# gpg
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ec2-zabbix-amzn1

%changelog
* Thu Jul  3 2014 IWAI, Masaharu <iwaim.sub@gmail.com> 1.1-1
- add GnuPG Publick Key (Source1)

* Sun Mar 30 2014 IWAI, Masaharu <iwaim.sub@gmail.com> 1-1
- initial release

