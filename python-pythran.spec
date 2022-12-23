%bcond_with	docs

Summary:	Ahead of Time compiler for numeric kernels
Name:		python-pythran
Version:	0.12.0
Release:	1
Group:		Development/Python
License:	BSD and (MIT or NCSA)
URL:		https://github.com/serge-sans-paille/pythran
#Source0:	https://github.com/serge-sans-paille/pythran/archive/%{version}/pythran-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pythran/pythran-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(blas)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pypandoc)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
#BuildRequires:	xsimd-devel
%if %{with docs}
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(scipy)
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

%files
%license LICENSE
%doc README.rst
%{?with_doc: %doc docs/_build/html}
%{_bindir}/pythran
%{_bindir}/pythran-config
%{py_sitedir}/pythran
%{py_sitedir}/pythran-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n pythran-%{version}

# use system libs
rm -r third_party/boost #third_party/xsimd
cat >> setup.cfg << EOF
[build_py]
no_boost=True
#no_xsimd=True
EOF

# fix doc
sed -i -e '/guzzle_sphinx_theme/d' docs/conf.py docs/requirements.txt

%build
%py_build

%if %{with docs}
PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif
 
%install
%py_install

