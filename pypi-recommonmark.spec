#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-recommonmark
Version  : 0.7.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/1c/00/3dd2bdc4184b0ce754b5b446325abf45c2e0a347e022292ddc44670f628c/recommonmark-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/00/3dd2bdc4184b0ce754b5b446325abf45c2e0a347e022292ddc44670f628c/recommonmark-0.7.1.tar.gz
Summary  : A docutils-compatibility bridge to CommonMark, enabling you to write CommonMark inside of Docutils & Sphinx projects.
Group    : Development/Tools
License  : MIT
Requires: pypi-recommonmark-bin = %{version}-%{release}
Requires: pypi-recommonmark-license = %{version}-%{release}
Requires: pypi-recommonmark-python = %{version}-%{release}
Requires: pypi-recommonmark-python3 = %{version}-%{release}
Requires: pypi(commonmark)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(commonmark)
BuildRequires : pypi(docutils)
BuildRequires : pypi(sphinx)

%description
# recommonmark
A `docutils`-compatibility bridge to [CommonMark][cm].
This allows you to write CommonMark inside of Docutils & Sphinx projects.

%package bin
Summary: bin components for the pypi-recommonmark package.
Group: Binaries
Requires: pypi-recommonmark-license = %{version}-%{release}

%description bin
bin components for the pypi-recommonmark package.


%package license
Summary: license components for the pypi-recommonmark package.
Group: Default

%description license
license components for the pypi-recommonmark package.


%package python
Summary: python components for the pypi-recommonmark package.
Group: Default
Requires: pypi-recommonmark-python3 = %{version}-%{release}

%description python
python components for the pypi-recommonmark package.


%package python3
Summary: python3 components for the pypi-recommonmark package.
Group: Default
Requires: python3-core
Provides: pypi(recommonmark)
Requires: pypi(commonmark)
Requires: pypi(docutils)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-recommonmark package.


%prep
%setup -q -n recommonmark-0.7.1
cd %{_builddir}/recommonmark-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641837749
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-recommonmark
cp %{_builddir}/recommonmark-0.7.1/license.md %{buildroot}/usr/share/package-licenses/pypi-recommonmark/227326135d61f3b0a7771d7eccc738e48ca056d4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cm2html
/usr/bin/cm2latex
/usr/bin/cm2man
/usr/bin/cm2pseudoxml
/usr/bin/cm2xetex
/usr/bin/cm2xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-recommonmark/227326135d61f3b0a7771d7eccc738e48ca056d4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
