Summary:	QT GUI for dctc (Direct Connect)
Summary(pl):	Oparte o QT GUI do dctc (Direct Connect)
Name:		dc-qt
Version:	0.0.8
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0a4481813107f516a51cb3798892fd3e
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
export QTDIR=/usr

%configure
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
