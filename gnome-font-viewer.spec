Summary:	Font viewer
Summary(pl.UTF-8):	Przeglądarka czcionek
Name:		gnome-font-viewer
Version:	3.12.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-font-viewer/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	253cc356073f8ed8b50beb427496d432
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.35.1
BuildRequires:	gnome-desktop-devel
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	harfbuzz-devel >= 0.9.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	gtk+3 >= 3.12.0
Provides:	gnome-utils-font-viewer = 1:%{version}-%{release}
Obsoletes:	gnome-utils-font-viewer < 1:3.3.92-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides font viewer.

%description -l pl.UTF-8
Ten pakiet dostarcza przeglądarkę czcionek.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-font-viewer
%attr(755,root,root) %{_bindir}/gnome-thumbnail-font
%{_desktopdir}/gnome-font-viewer.desktop
%{_datadir}/appdata/gnome-font-viewer.appdata.xml
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
