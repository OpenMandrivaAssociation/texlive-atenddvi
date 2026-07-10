%global tl_name atenddvi
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Provides the \AtEndDvi command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/atenddvi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atenddvi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is unneeded and does nothing when used with a LaTeX format
2020-10-01 or newer as in this case the format provides the \AtEndDvi
command. For older formats it implements \AtEndDvi, a counterpart to
\AtBeginDvi. The execution of its argument is delayed to the end of the
document at the end of the last page. Thus \special and \write remain
effective, because they are put into the last page. This is the main
difference to \AtEndDocument.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/atenddvi
%dir %{_datadir}/texmf-dist/source/latex/atenddvi
%dir %{_datadir}/texmf-dist/tex/latex/atenddvi
%doc %{_datadir}/texmf-dist/doc/latex/atenddvi/README.md
%doc %{_datadir}/texmf-dist/doc/latex/atenddvi/atenddvi.pdf
%doc %{_datadir}/texmf-dist/source/latex/atenddvi/atenddvi.dtx
%{_datadir}/texmf-dist/tex/latex/atenddvi/atenddvi-2019-12-11.sty
%{_datadir}/texmf-dist/tex/latex/atenddvi/atenddvi.sty
