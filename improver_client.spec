%define protocol_name "augeas_protocol"
%define protocol_version "1.0"

Summary:        Improver client
Name:           improver_client
Version:        1.0.0
Release:        26
License:        GPL
URL:            http://www.rosalab.ru
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gnome-doc-utils, libgnomeui2-devel
BuildRequires:  gtk2-devel, desktop-file-utils, libbonoboui
Requires:	pciutils, ldetect, coreutils, usermode-consoleonly, imagemagick, lsb-release >= 2.0, zip, lshw

%description
GUI for testers.

%prep
%setup -q 

%build
%configure
%make

%install
%makeinstall_std

echo "%{name} %{version}-%{release}" > etc/improver/client_version.conf
echo "%{protocol_name} %{protocol_version}" > etc/improver/protocol_version.conf

mkdir -p $RPM_BUILD_ROOT/etc/improver
install -m 644 etc/improver/client_version.conf $RPM_BUILD_ROOT/etc/improver
install -m 644 etc/improver/protocol_version.conf $RPM_BUILD_ROOT/etc/improver

mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}
install -m 644 usr/share/pixmaps/%{name}/*.png $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}
install -m 644 usr/share/pixmaps/%{name}/*.svg $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}
install -m 644 usr/share/%{name}.glade $RPM_BUILD_ROOT/usr/share

mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_hw_info_tar $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_hw_info $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_convert_screenshots $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT/var/local/improver_client/
install -m 644 var/local/improver_client/improver_client.conf $RPM_BUILD_ROOT/var/local/improver_client/

mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_UA/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/en/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES/
install -m 644 usr/share/locale/ru/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
install -m 644 usr/share/locale/ua/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/ru_UA/LC_MESSAGES/
install -m 644 usr/share/locale/en/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/en/LC_MESSAGES/
install -m 644 usr/share/locale/us/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES/

mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/22x22/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/64x64/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/oxygen/128x128/apps

install -m 644 icons/hicolor/16/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps
install -m 644 icons/hicolor/22/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/22x22/apps
install -m 644 icons/hicolor/32/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
install -m 644 icons/hicolor/48/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
install -m 644 icons/hicolor/64/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/64x64/apps
install -m 644 icons/hicolor/128/* $RPM_BUILD_ROOT/usr/share/icons/hicolor/128x128/apps

install -m 644 icons/oxygen/16/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/16x16/apps
install -m 644 icons/oxygen/22/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/22x22/apps
install -m 644 icons/oxygen/32/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/32x32/apps
install -m 644 icons/oxygen/48/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/48x48/apps
install -m 644 icons/oxygen/64/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/64x64/apps
install -m 644 icons/oxygen/128/* $RPM_BUILD_ROOT/usr/share/icons/oxygen/128x128/apps

desktop-file-install --delete-original          \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications               \
    %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps
install -m 644 etc/security/console.apps/improver $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 etc/pam.d/improver $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/

mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -P $RPM_BUILD_DIR/%{name}-%{version}/ln/* $RPM_BUILD_ROOT/usr/bin/

%files
%doc AUTHORS COPYING INSTALL README NEWS
%{_sysconfdir}/*
%{_bindir}/improver
%{_bindir}/improver_client
%{_bindir}/script_hw_info_tar
%{_bindir}/script_hw_info
%{_bindir}/script_convert_screenshots
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}/*.png
%{_datadir}/pixmaps/%{name}/*.svg
%{_datadir}/icons/hicolor/*
%{_datadir}/icons/oxygen/*
#%{_datadir}/pixmaps/%{name}.png
%{_datadir}/improver_client.glade
/var/local/improver_client/improver_client.conf
%{_datadir}/locale/*

