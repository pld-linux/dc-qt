#
# Conditional build:
%bcond_without	xine	# disable media file preview (uses xine)
#
Summary:	Qt GUI for dctc (Direct Connect)
Summary(pl.UTF-8):   Oparte o Qt GUI do dctc (Direct Connect)
Name:		dc-qt
Version:	0.1.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/dc-qt/%{name}-%{version}.tar.gz
# Source0-md5:	2653c020cd2cc3957d35f2c1e77b4d46
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://dc-qt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.2
BuildRequires:	rpmbuild(macros) >= 1.129
%{?with_xine:BuildRequires:	xine-lib-devel}
Requires:	dctc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Direct Connect client (dctc) Qt GUI.

%description -l pl.UTF-8
Graficzny interfejs użytkownika używający Qt do dctc (Direct Connect).

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT \
	 kde_htmldir=%{_kdedocdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/dc_qt
%{_desktopdir}/*.desktop
%{_docdir}/%{name}
%{_pixmapsdir}/%{name}.png
