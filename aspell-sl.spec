Summary:	Slovene dictionary for aspell
Summary(pl.UTF-8):	Słownik słoweński dla aspella
Name:		aspell-sl
Version:	0.50
%define	subv	0
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sl/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	c4c11402bc834d796d1b56e711470480
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slovene dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik słoweński (lista słów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
