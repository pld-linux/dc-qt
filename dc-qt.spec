#
# Conditional build:
%bcond_without	xine	# disable media file preview (uses xine)
#
Summary:	QT GUI for dctc (Direct Connect)
Summary(pl):	Oparte o QT GUI do dctc (Direct Connect)
Name:		dc-qt
Version:	0.1.1
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/dc-qt/%{name}-%{version}.tar.gz
# Source0-md5:	411758af4bf06198570aa14f534249e0
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
Patch1:		%{name}-preview.patch
URL:		http://sourceforge.net/projects/dc-qt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 2.3
%{?with_xine:BuildRequires:	xine-lib-devel}
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--%{?with_xine:en}%{!?with_xine:dis}able-preview \
	--with-qt-libs=%{_libdir} \
	--with-qt-includes=%{_includedir}/qt

%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%attr(755,root,root) %{_bindir}/dc_qt
#%attr(644,root,root) %{_pixmapsdir}/*.xpm
%attr(644,root,root) %{_desktopdir}/*
