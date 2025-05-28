Name:		texlive-hyphen-slovak
Version:	73410
Release:	1
Summary:	Slovak hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-slovak.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings.
Original patterns 'skhyphen' are still distributed in the
'csplain' package and loaded with ISO Latin 2 encoding (IL2).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-slovak
%_texmf_language_def_d/hyphen-slovak
%_texmf_language_lua_d/hyphen-slovak

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-slovak <<EOF
\%% from hyphen-slovak:
slovak loadhyph-sk.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-slovak
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-slovak <<EOF
\%% from hyphen-slovak:
\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-slovak
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-slovak <<EOF
-- from hyphen-slovak:
	['slovak'] = {
		loader = 'loadhyph-sk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-sk.pat.txt',
		hyphenation = 'hyph-sk.hyp.txt',
	},
EOF
