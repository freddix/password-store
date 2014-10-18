Summary:	Standard unix password manager
Name:		password-store
Version:	1.6.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://git.zx2c4.com/password-store/snapshot/%{name}-%{version}.tar.xz
# Source0-md5:	bcfd1027f5c92f26d7fcbf4e3af750eb
URL:		http://zx2c4.com/projects/password-store/
Requires:	gnupg2
Requires:	pwgen
Requires:	tree
Requires:	util-linux
Suggests:	git
Suggests:	xclip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pass is a very simple password store that keeps passwords inside gpg2
encrypted files inside a simple directory tree residing at
~/.password-store. The pass utility provides a series of commands for
manipulating the password store, allowing the user to add, remove,
edit, synchronize, generate, and manipulate passwords.

%package -n zsh-completion-pass
Summary:	Zsh auto-complete site functions
Group:		Documentation
Requires:	zsh

%description -n zsh-completion-pass
Zsh auto-complete site functions.

%package -n dmenu-pass
Summary:	dmenu interface to pass
Group:		Applications
Requires:	dmenu

%description -n dmenu-pass
dmenu interface to pass.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	BINDIR=%{_bindir}	\
	LIBDIR=%{_libdir}	\
	MANDIR=%{_mandir}	\
	SYSCONFDIR=%{_sysconfdir}

install -D src/completion/pass.zsh-completion \
    $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_pass

install -D contrib/dmenu/passmenu \
    $RPM_BUILD_ROOT%{_bindir}/passmenu

%{__sed} -i -e '1s,#!/usr/bin/env bash,#!/usr/bin/bash,' \
    $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pass
%{_mandir}/man1/pass.1*

%files -n zsh-completion-pass
%defattr(644,root,root,755)
%{_datadir}/zsh/site-functions/_pass

%files -n dmenu-pass
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/passmenu

