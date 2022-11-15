Name:		texlive-atenddvi
Version:	56922
Release:	1
Summary:	Provides the \AtEndDvi command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/atenddvi
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is unneeded and does nothing when used with a
LaTeX format 2020-10-01 or newer as in this case the format
provides the \AtEndDvi command. For older formats it implements
\AtEndDvi, a counterpart to \AtBeginDvi. The execution of its
argument is delayed to the end of the document at the end of
the last page. Thus \special and \write remain effective,
because they are put into the last page. This is the main
difference to \AtEndDocument.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/atenddvi
%{_texmfdistdir}/tex/latex/atenddvi
%doc %{_texmfdistdir}/doc/latex/atenddvi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
