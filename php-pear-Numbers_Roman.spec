%include	/usr/lib/rpm/macros.php
%define		_class		Numbers
%define		_subclass	Roman
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - converting to and from Roman numerals
Summary(pl.UTF-8):	%{_pearname} - konwersja z i do cyfr rzymskich
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	015e9d283ccf698be6a0247c57a96fc6
URL:		http://pear.php.net/package/Numbers_Roman/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Numbers_Roman-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class for converting to and from Roman numerals.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa do konwersji z i do cyfr rzymskich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
