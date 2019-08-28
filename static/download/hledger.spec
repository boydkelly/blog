%global commit d5a92559f1dc9337ff628fa64c48aa07300e4ae7 
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global gittag hledger-1.14.2
%global debug_package %{nil}

Name:     hledger 
Version:  1.14.2
Release:  1%{dist} 
Summary:  hledger 
License:  GPL-3.0
URL:      https://hledger.org
 
Source0:  https://github.com/simonmichael/hledger/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: stack 
BuildRequires: ghc 
#BuildRequires: glibc-langpack-en
BuildRequires: perl 
BuildRequires: gcc
BuildRequires: make	
BuildRequires: automake	
BuildRequires: gmp-devel	
BuildRequires: libffi 
BuildRequires: zlib-devel 
BuildRequires: tar 
BuildRequires: git 
BuildRequires: gnupg

%description
hledger is a computer program for easily tracking money, time, or other commodities, on unix, mac and windows (and web-capable mobile devices, to some extent).

%prep
%autosetup -n %{name}-%{commit}

%build
#( curl -sSL https://get.haskellstack.org/ | sh )
LANG=en_US.UTF-8 stack setup
LANG=en_US.UTF-8 stack build

%install
stack install
mkdir -p -m 755  %{buildroot}%{_bindir}/
install -m 755  ~/.local/bin/* %{buildroot}%{_bindir}/

%post

%files
/%_bindir/*

%changelog
* Wed Jul 31 2019 Boyd Kelly <bkelly@coastsystems.net> - 1.14.2 
- Initial build of hledger 1.14.2 works locally but not on copr 

