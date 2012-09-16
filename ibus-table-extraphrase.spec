Summary:	Extra Chinese phrases for ibus-table
Summary(pl.UTF-8):	Dane dodatkowych fraz chińskich dla ibus-table
Name:		ibus-table-extraphrase
Version:	1.3.9.20110826
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	289da050912045fe59ab525910391f6f
URL:		http://code.google.com/p/ibus/
BuildRequires:	ibus-table-devel >= 1.1.0
BuildRequires:	pkgconfig
Requires:	ibus-table > 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extra Chinese phrases for IBus Table engine.

%description -l pl.UTF-8
Dane dodatkowych fraz chińskich dla IBus Table.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_datadir}/ibus-table/data/extra_phrase.txt
%{_npkgconfigdir}/ibus-table-extraphrase.pc
