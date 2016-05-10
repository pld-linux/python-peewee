#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	peewee
Summary:	A small, expressive ORM
Name:		python-%{module}
Version:	2.3.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e4a9ce2cf3166ced975b8f7fecca6271
URL:		http://github.com/coleifer/peewee/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python-modules-sqlite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small, expressive ORM written in Python with built-in support for
Sqlite, MySQL and PostgreSQL and special extensions like hstore. For
flask integration, including an admin interface and RESTful API, check
out flask-peewee.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

mv $RPM_BUILD_ROOT%{_bindir}/{pwiz.py,pwiz}

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/pwiz.*
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/playhouse/test_*
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/playhouse/tests_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/pwiz
%{py_sitescriptdir}/peewee.py[co]
%{py_sitescriptdir}/peewee-%{version}-py*.egg-info
%{py_sitescriptdir}/playhouse
