%include	/usr/lib/rpm/macros.php
%define         _class          Numbers
%define         _subclass       Roman
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - converting to and from Roman numerals
Summary(pl):	%{_pearname} - konwersja z i do cyfr rzymskich
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	a00477f4b4e7d6b621bf15de26a048bb
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class for converting to and from Roman numerals.

%description -l pl
Klasa do konwersji z i do cyfr rzymskich.

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
