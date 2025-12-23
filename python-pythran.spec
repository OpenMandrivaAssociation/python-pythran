%define module pythran

# docs requires python modules that we do not currenty package, 0 = disabled.
%bcond	docs 0

Summary:	Ahead of Time compiler for numeric kernels
Name:		python-pythran
Version:	0.18.1
Release:	1
Group:		Development/Python
License:	BSD and (MIT or NCSA)
URL:		https://github.com/serge-sans-paille/pythran
Source0:	https://github.com/serge-sans-paille/pythran/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(blas)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
#BuildRequires:	xsimd-devel
%if %{with docs}
# Unpackaged
#BuildRequires:	python%%{pyver}dist(guzzle_sphinx_theme)
#BuildRequires:	python%%{pyver}dist(nbsphinx)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(scipy)
%endif

Requires:	boost-devel
Requires:	pkgconfig(blas)
Requires:	pkgconfig(python)
#Requires:	xsimd-devel

BuildArch:	noarch

%description
Pythran is an ahead of time compiler for a subset of the Python language,
with a focus on scientific computing. It takes a Python module annotated
with a few interface descriptions and turns it into a native Python module
with the same interface, but (hopefully) faster.

It is meant to efficiently compile scientific programs, and takes advantage
of multi-cores and SIMD instruction units.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%if %{with docs}
PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{?with_doc: %doc docs/_build/html}
%{_bindir}/%{module}
%{_bindir}/%{module}-config
%{python_sitelib}/omp
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
