Summary:	Extra phrase for ibus-table
Name:		ibus-table-extraphrase
Version:	1.2.0.20100305
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	ab3a0bd3b443ad4df9ad5554e155550d
URL:		http://code.google.com/p/ibus/
BuildArch:	noarch
BuildRequires:	ibus-table-devel >= 1.1.0
Requires:	ibus-table > 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extra phrase data for IBus-Table engine.

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
%doc AUTHORS ChangeLog NEWS README
%{_npkgconfigdir}/ibus-table-extraphrase.pc
%{_datadir}/ibus-table/data/extra_phrase.txt
