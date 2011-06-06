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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gnome-doc-utils, libgnomeui2-devel
BuildRequires:  gtk2-devel, desktop-file-utils, libbonoboui
Requires:	pciutils, ldetect, coreutils, usermode-consoleonly, imagemagick, lsb-release >= 2.0, zip, lshw


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
#ln -sf ln/consolehelper $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL README NEWS
%{_sysconfdir}/*
%{_bindir}/improver
%{_bindir}/improver_client
%{_bindir}/script_hw_info_tar
%{_bindir}/script_hw_info
%{_bindir}/script_convert_screenshots
#%{_datadir}/%{name}-%{version}/eula.en_US
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}/*.png
%{_datadir}/pixmaps/%{name}/*.svg
%{_datadir}/icons/hicolor/*
%{_datadir}/icons/oxygen/*
#%{_datadir}/pixmaps/%{name}.png
%{_datadir}/improver_client.glade
/var/local/improver_client/improver_client.conf
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
* Tue May 24 2011 Leontiev Danila 1.0.0-26
- Fixed ru locale

* Mon May 23 2011 Leontiev Danila 1.0.0-25
- Rebrending augeas_client to improver_client

* Fri May 20 2011 Leontiev Danila 1.0.0-24
- Added check for cur_file, if now cur_file -- clear cache

* Wed May 11 2011 Leontiev Danila 1.0.0-23
- Added new locale

* Fri May 06 2011 Leontiev Danila 1.0.0-22
- Added error on bad registr
- Added fio info to report
- Added close sesseion after testplan getted

* Tue Apr 26 2011 Leontiev Danila 1.0.0-21
- Removed debug info fpom hw_parser

* Thu Apr 21 2011 Leontiev Danila 1.0.0-20
- Changed lsb_release format
- Several changes in glade file


* Tue Apr 19 2011 Leontiev Danila 1.0.0-19
- Fixed buf with a large attach

* Tue Apr 19 2011 Leontiev Danila 1.0.0-18
- Changed scripts (tar -> zip; hw_id) 
- Added req

* Tue Apr 19 2011 Leontiev Danila 1.0.0-17
- Added ua,en locales (TODO: integrate locales in makefile)

* Fri Apr 15 2011 Leontiev Danila 1.0.0-16
- Changed locale
- Added label withport
- Changed scripts (fixed hw_id)


* Wed Apr 13 2011 Leontiev Danila 1.0.0-15
- Added send client/protocol version on connect to server

* Tue Apr 12 2011 Leontiev Danile 1.0.0-14
- In prev version was too many bugs.
- Removed "skip" options
- Removed hw_id script (now hw_id grapped from ls_hwinfo script)
- Fix many bugs
- Chagned locale
- Added client version for sending it to server

* Fri Apr 08 2011 Leontiev Danila 1.0.0-13
- Fixed bug with many attaches

* Fri Apr 08 2011 Leontiev Danila 1.0.0-12
- Changed locale
- label in welcome/send states are resizeble

* Thu Apr 07 2011 Leontiev Danila 1.0.0-11
- Added hotkeyas 
- Changed gram error with "atthachAble"


* Wed Apr 06 2011 Leontiev Danila 1.0.0-10
- mysticaa

* Wed Apr 06 2011 Leontiev Danila 1.0.0-9
- Added attach any file button
- Added working with skipped questions
- Changed design
- Changed locale

* Mon Apr 04 2011 Leontiev Danila 1.0.0-8
- Added button to get new testplan after sending
- Chacnged size of comment textbuffer to 8192

* Thu Mar 29 2011 Leontiev Danila 1.0.0-7
- Added CACHE_DIR (now we can fast chagne it and all will work)
- Added consolehelper support

* Mon Mar 28 2011 Leontiev Danila 1.0.0-6
- Added script to gathering hwinfo and added send file to command_registr command at src/client.c

* Fri Mar 25 2011 Leontiev Danila 1.0.0-5
- Added desktop file and icons

* Thu Mar 24 2011 Leontiev Danila 1.0.0-4
- Added send hw_id for testaplans list

* Tue Mar 22 2011 Leontiev Danila 1.0.0-3
- Added locale
- Fixed several bugs

* Fri Mar 04 2011 Leontiev Danila
- Added conf to var/local
- Fixed tester.glade (replaced with augeas_client.glade)
- Added libgnomeui-devel req

* Thu Mar 03 2011 Leontiev Danila
- First release (just package)
