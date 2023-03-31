Name:		texlive-datestamp
Version:	61719
Release:	2
Summary:	Fixed date-stamps with LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datestamp
License:	gpl3+ fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datestamp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datestamp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datestamp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Add fixed date-stamps with simple and customizable aux files
and LuaLaTeX. As long as the aux file is not deleted/modified
the date-stamp generated with this package remains intact.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/datestamp
%{_texmfdistdir}/tex/lualatex/datestamp
%doc %{_texmfdistdir}/doc/lualatex/datestamp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
