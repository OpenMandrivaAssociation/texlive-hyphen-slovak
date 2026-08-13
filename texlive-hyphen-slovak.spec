%global tl_name hyphen-slovak
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Slovak hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-slovak
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-slovak.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings. Original
patterns 'skhyphen' are still distributed in the 'csplain' package and
loaded with ISO Latin 2 encoding (IL2).


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-slovak:
slovak loadhyph-sk.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-slovak:
\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-slovak:
['slovak'] = {
	loader = 'loadhyph-sk.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-sk.pat.txt',
	hyphenation = 'hyph-sk.hyp.txt',
},
TL_HYPHEN_EOF
