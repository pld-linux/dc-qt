Summary:	QT GUI for dctc (Direct Connect)
Summary(pl):	QT GUI do dctc (Direct Connect)
Name:		dc-qt
Version:	0.0.3
Release:	3
License:	GPL v2
Group:		X11/Applications/Networking
# Sourceforge is crazy with this mirrors... telia is fast...
Source0:	http://telia.dl.sourceforge.net/sourceforge/dc-qt/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-home_etc.patch
URL:		http://sourceforge.net/projects/dc-qt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 2.3
Requires:	dctc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Direct Connect client (dctc) QT GUI.

%description -l pl
Graficzny interfejs u¿ytkownika u¿ywaj±cy QT do dctc (Direct Connect).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
QTDIR=%{_includedir}/qt
export QTDIR
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_datadir}/pixmaps,%{_bindir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install dc_qt		$RPM_BUILD_ROOT%{_bindir}
install icon.xpm	$RPM_BUILD_ROOT%{_datadir}/pixmaps/dc_qt.xpm
install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README DESIGN
%attr(755,root,root) %{_bindir}/dc_qt
%attr(644,root,root) %{_datadir}/pixmaps/*.xpm
%attr(644,root,root) %{_applnkdir}/Network/Communications/*
