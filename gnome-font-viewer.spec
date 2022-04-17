# TODO: use gtk4-update-icon-cache
Summary:	Font viewer
Summary(pl.UTF-8):	Przeglądarka czcionek
Name:		gnome-font-viewer
Version:	42.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-font-viewer/42/%{name}-%{version}.tar.xz
# Source0-md5:	7256fb1cba4d74b110cd546852efe302
URL:		https://wiki.gnome.org/Attic/GnomeUtils
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gnome-desktop4-devel >= 42
BuildRequires:	gtk4-devel >= 4.5.0
BuildRequires:	harfbuzz-devel >= 0.9.9
BuildRequires:	libadwaita-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.56.0
Requires:	gtk4 >= 4.5.0
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
