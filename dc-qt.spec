Summary:	QT GUI for dctc (Direct Connect)
Summary(pl):	Oparte o QT GUI do dctc (Direct Connect)
Name:		dc-qt
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ac48fec146ac6cb5d57021c96911e7e1
Source1:	%{name}.desktop
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

%build
QTDIR=%{_prefix}; export QTDIR

%configure \
	--with-qt-libs=%{_libdir} \
	--with-qt-includes=%{_includedir}/qt/

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/dc_qt
#%attr(644,root,root) %{_pixmapsdir}/*.xpm
%attr(644,root,root) %{_applnkdir}/Network/Communications/*
