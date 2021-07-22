#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : retrying
Version  : 1.3.3
Release  : 44
URL      : https://github.com/rholder/retrying/archive/v1.3.3.tar.gz
Source0  : https://github.com/rholder/retrying/archive/v1.3.3.tar.gz
Summary  : Retrying
Group    : Development/Tools
License  : Apache-2.0
Requires: retrying-license = %{version}-%{release}
Requires: retrying-python = %{version}-%{release}
Requires: retrying-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
Retrying
=========================
.. image:: https://travis-ci.org/rholder/retrying.png?branch=master
:target: https://travis-ci.org/rholder/retrying

%package license
Summary: license components for the retrying package.
Group: Default

%description license
license components for the retrying package.


%package python
Summary: python components for the retrying package.
Group: Default
Requires: retrying-python3 = %{version}-%{release}

%description python
python components for the retrying package.


%package python3
Summary: python3 components for the retrying package.
Group: Default
Requires: python3-core
Provides: pypi(retrying)
Requires: pypi(six)

%description python3
python3 components for the retrying package.


%prep
%setup -q -n retrying-1.3.3
cd %{_builddir}/retrying-1.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133754
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_retrying.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/retrying
cp %{_builddir}/retrying-1.3.3/LICENSE %{buildroot}/usr/share/package-licenses/retrying/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/retrying-1.3.3/NOTICE %{buildroot}/usr/share/package-licenses/retrying/e92af22a6251770635f880bc9961478b400aae4e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/retrying/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/retrying/e92af22a6251770635f880bc9961478b400aae4e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
