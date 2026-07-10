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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is unneeded and does nothing when used with a LaTeX format
2020-10-01 or newer as in this case the format provides the \AtEndDvi
command. For older formats it implements \AtEndDvi, a counterpart to
\AtBeginDvi. The execution of its argument is delayed to the end of the
document at the end of the last page. Thus \special and \write remain
effective, because they are put into the last page. This is the main
difference to \AtEndDocument.

