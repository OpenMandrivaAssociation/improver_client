%define protocol_name "augeas_protocol"
%define protocol_version "2.0"

Summary:        Improver client
Name:           improver_client
Version:        2.0.0
Release:        14%{?dist}
License:        GPL
#URL:            
Group:          User Interface/Desktops
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gnome-doc-utils, libgnomeui2-devel, libglade2.0_0-devel
BuildRequires:  gtk2-devel, desktop-file-utils, libbonoboui, libsqlite3-devel
Requires:	pciutils, ldetect, coreutils, usermode-consoleonly, imagemagick, lsb-release >= 2.0, zip, lshw, desktop-common-data


%description
GUI for testers.

%prep
%setup -q 

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

echo "%{name} %{version}-%{release}" > etc/improver/client_version.conf
echo "%{protocol_name} %{protocol_version}" > etc/improver/protocol_version.conf

mkdir -p $RPM_BUILD_ROOT/etc/improver
install -m 644 etc/improver/client_version.conf $RPM_BUILD_ROOT/etc/improver
install -m 644 etc/improver/protocol_version.conf $RPM_BUILD_ROOT/etc/improver

mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}/pixmaps
install -m 644 usr/share/improver_client/pixmaps/*.png $RPM_BUILD_ROOT/usr/share/%{name}/pixmaps/
install -m 644 usr/share/improver_client/pixmaps/*.svg $RPM_BUILD_ROOT/usr/share/%{name}/pixmaps/
install -m 644 usr/share/%{name}/%{name}.glade $RPM_BUILD_ROOT/usr/share/%{name}

mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_hw $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_hw_info_tar $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_hw_info $RPM_BUILD_ROOT/usr/bin
install -m 755 usr/bin/script_convert_screenshots $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT/var/local/improver_client/
mkdir -p $RPM_BUILD_ROOT/var/local/improver/
install -m 644 var/local/improver_client/improver_client.conf $RPM_BUILD_ROOT/var/local/improver_client/
install -m 644 var/local/improver_client/bd $RPM_BUILD_ROOT/var/local/improver_client/
install -m 644 var/local/improver_client/bd_clean $RPM_BUILD_ROOT/var/local/improver_client/
install -m 644 var/local/improver/* $RPM_BUILD_ROOT/var/local/improver/

#
#
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_UA/LC_MESSAGES/
#mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/en/LC_MESSAGES/
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES/
#mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES/
install -m 644 usr/share/locale/ru/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/ru_RU/LC_MESSAGES/
install -m 644 usr/share/locale/ua/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/ru_UA/LC_MESSAGES/
install -m 644 usr/share/locale/en/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/en/LC_MESSAGES/
install -m 644 usr/share/locale/us/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES/
#install -m 644 usr/share/locale/br/%{name}.mo $RPM_BUILD_ROOT/usr/share/locale/pt_BR/LC_MESSAGES/
#
#

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
#ln -sf ln/consolehelper $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL README NEWS
%{_sysconfdir}/*
%{_bindir}/improver
%{_bindir}/improver_client
%{_bindir}/script_hw_info_tar
%{_bindir}/script_hw_info
%{_bindir}/script_hw
%{_bindir}/script_convert_screenshots
#%{_datadir}/%{name}-%{version}/eula.en_US
%{_datadir}/applications/%{name}.desktop
%{_datadir}/improver_client/pixmaps/*
#%{_datadir}/pixmaps/%{name}/*.svg
%{_datadir}/icons/hicolor/*
%{_datadir}/icons/oxygen/*
#%{_datadir}/pixmaps/%{name}.png
%{_datadir}/improver_client/improver_client.glade
/var/local/improver_client/*
/var/local/improver/*
%{_datadir}/locale/*

%ifarch noarch
/usr/lib/debug/*
/usr/lib/debug/.build-id/e5/
%endif
#ru_RU/LC_MESSAGES/%{name}.mo
#/usr/local/bin/augeas_client
#%{_sysconfdir}/pam.d/augeas_client

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jun 28 2011 Leontiev Danila 2.0.0-13
- Fixed little buff with wish file attach
- Added screenshoot convertation script

* Mon Jun 27 2011 Leontiev Danila 2.0.0-12
- Added workw it hypertext
- Added req: desktop-common-data

* Thu Jun 23 2011 Leontiev Danila 2.0.0-10
- Changed sprintf for mprintf in improver_sqlite.c
- Changed glade file (description of testplan label)
- Fixed reload button
- Fixed double-click on groupe
- Fixed label in glade

* Wed Jun 22 2011 Kazygasheb Kuzma 2.0.0-9
- Changed callfunction from sprintf to sqlite3_mprintf imp_sql_answer_edit_choosen.c
- Changed on_window1__key_press_event

* Tue Jun 21 2011 Leontiev Danila 2.0.0-8
- Changed server port from 12347 to 12447
- Added locales for en/us/ua
- Fixed work on client db
- Added locale tag in report.xml
- Cleaning code

* Mon Jun 20 2011 Leontiev Danila 2.0.0-7
- Changed work with adding new testplans
- Added sqlite.log to spec

* Mon Jun 20 2011 Leontiev Danila 2.0.0-6
- Started log changes