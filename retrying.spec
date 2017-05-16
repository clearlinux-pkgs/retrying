#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : retrying
Version  : 1.3.3
Release  : 22
URL      : https://github.com/rholder/retrying/archive/v1.3.3.tar.gz
Source0  : https://github.com/rholder/retrying/archive/v1.3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: retrying-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
Retrying
=========================
.. image:: https://travis-ci.org/rholder/retrying.png?branch=master
:target: https://travis-ci.org/rholder/retrying

%package python
Summary: python components for the retrying package.
Group: Default

%description python
python components for the retrying package.


%prep
%setup -q -n retrying-1.3.3

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_retrying.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
