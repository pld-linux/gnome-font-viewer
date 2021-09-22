Summary:	Font viewer
Summary(pl.UTF-8):	Przeglądarka czcionek
Name:		gnome-font-viewer
Version:	41.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-font-viewer/41/%{name}-%{version}.tar.xz
# Source0-md5:	ff7fa68a5e870fffed2ab10d993a1bb2
URL:		https://wiki.gnome.org/Attic/GnomeUtils
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gtk+3-devel >= 3.24.1
BuildRequires:	harfbuzz-devel >= 0.9.9
BuildRequires:	libhandy1-devel >= 1.0.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.56.0
Requires:	gtk+3 >= 3.24.1
Requires:	harfbuzz >= 0.9.9
Requires:	libhandy1 >= 1.0.0
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

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-font-viewer
%attr(755,root,root) %{_bindir}/gnome-thumbnail-font
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
%{_desktopdir}/org.gnome.font-viewer.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.font-viewer.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.font-viewer-symbolic.svg
