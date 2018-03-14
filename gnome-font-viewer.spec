Summary:	Font viewer
Summary(pl.UTF-8):	Przeglądarka czcionek
Name:		gnome-font-viewer
Version:	3.28.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-font-viewer/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	1bfe7dcc475526ceb4a7319677408a4a
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.35.1
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	harfbuzz-devel >= 0.9.9
BuildRequires:	meson >= 0.40.1
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	glib2 >= 1:2.35.1
Requires:	gtk+3 >= 3.20.0
Requires:	harfbuzz >= 0.9.9
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
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

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
%{_desktopdir}/org.gnome.font-viewer.desktop
%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
