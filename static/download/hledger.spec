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

%description
hledger is a computer program for easily tracking money, time, or other commodities, on unix, mac and windows (and web-capable mobile devices, to some extent).

%prep
%autosetup -n %{name}-%{commit}

%build
curl -sSL https://get.haskellstack.org/ | sh
stack setup
LANG=en_US.UTF-8 stack build

%install
stack install
mkdir -p -m 755  %{buildroot}%{_bindir}/
install -m 755  ~/.local/bin/* %{buildroot}%{_bindir}/

%post

%files
/%_bindir/*

%changelog
* Mon Jul 15 2019 Boyd Kelly <bkelly@coastsystems.net> - 0.20 
- Initial version of sommelier for Fedora and fedora-crouton-wayland 

