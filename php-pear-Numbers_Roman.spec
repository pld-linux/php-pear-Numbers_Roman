%include	/usr/lib/rpm/macros.php
%define		_class		Numbers
%define		_subclass	Roman
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - converting to and from Roman numerals
Summary(pl):	%{_pearname} - konwersja z i do cyfr rzymskich
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5103711a2e29d48a5ccda8ba1a11c893
URL:		http://pear.php.net/package/Numbers_Roman/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class for converting to and from Roman numerals.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa do konwersji z i do cyfr rzymskich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
