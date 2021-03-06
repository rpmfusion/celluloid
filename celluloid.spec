Name:           celluloid
Version:        0.21
Release:        1%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPLv3+
URL:            https://github.com/celluloid-player/celluloid
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  intltool >= 0.40.6
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  mpv-libs-devel
Requires:       youtube-dl >= 2016.03.06
Requires:       hicolor-icon-theme

Provides:       gnome-mpv = %{version}-%{release}
Obsoletes:      gnome-mpv < 0.17

%description
Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv.
It aims to be easy to use while maintaining high level of configurability.

%prep
%autosetup -p1

%build
%configure
%make_build V=1

%install
%make_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop
%{_datadir}/dbus-1/services/io.github.celluloid_player.Celluloid.service
%{_datadir}/glib-2.0/schemas/io.github.celluloid_player.Celluloid.gschema.xml
# The old GSchema is left installed for settings migration.
%{_datadir}/glib-2.0/schemas/io.github.GnomeMpv.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
 %{_mandir}/man1/%{name}.1.*

%changelog
* Mon Mar 22 2021 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.21-1
- Update to 0.21

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.20-2
- Rebuild for new mpv

* Sat Sep 19 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.20-1
- Update to 0.20

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-3
- Fix wayland blackscreen

* Tue Apr 21 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-2
- Enable LTO

* Thu Apr 09 2020 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.19-1
- Update to 0.19

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.18-1
- Update to 0.18

* Mon Sep 23 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.17-2
- Fix crash #5392

* Fri Aug 09 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.17-1
- Update to 0.17
- Renamed gnome-mpv to celluloid
