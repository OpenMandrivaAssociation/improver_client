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
BuildRequires:  gnome-doc-utils
BuildRequires:  libgnomeui2-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libbonoboui
Requires:	pciutils
Requires:       ldetect
Requires:       coreutils
Requires:       usermode-consoleonly
Requires:       imagemagick
Requires:       lsb-release >= 2.0
Requires:       zip
Requires:       lshw

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

mkdir -p %buildroot%_sysconfdir/improver
install -m 644 etc/improver/client_version.conf %buildroot%_sysconfdir/improver
install -m 644 etc/improver/protocol_version.conf %buildroot%_sysconfdir/improver

mkdir -p %buildroot%_datadir/pixmaps/%{name}
install -m 644 usr/share/pixmaps/%{name}/*.png %buildroot%_datadir/pixmaps/%{name}
install -m 644 usr/share/pixmaps/%{name}/*.svg %buildroot%_datadir/pixmaps/%{name}
install -m 644 usr/share/%{name}.glade %buildroot%_datadir

mkdir -p %buildroot/usr/bin
install -m 755 usr/bin/script_hw_info_tar %buildroot%_bindir
install -m 755 usr/bin/script_hw_info %buildroot%_bindir
install -m 755 usr/bin/script_convert_screenshots %buildroot%_bindir

mkdir -p %buildroot/var/local/improver_client/
install -m 644 var/local/improver_client/improver_client.conf %buildroot/var/local/improver_client/

mkdir -p %buildroot%_datadir/locale/ru_RU/LC_MESSAGES/
mkdir -p %buildroot%_datadir/locale/ru_UA/LC_MESSAGES/
mkdir -p %buildroot%_datadir/locale/ru_RU/LC_MESSAGES/
mkdir -p %buildroot%_datadir/locale/en/LC_MESSAGES/
mkdir -p %buildroot%_datadir/locale/en_US/LC_MESSAGES/
install -m 644 usr/share/locale/ru/%{name}.mo %buildroot%_datadir/locale/ru_RU/LC_MESSAGES/
install -m 644 usr/share/locale/ua/%{name}.mo %buildroot%_datadir/locale/ru_UA/LC_MESSAGES/
install -m 644 usr/share/locale/en/%{name}.mo %buildroot%_datadir/locale/en/LC_MESSAGES/
install -m 644 usr/share/locale/us/%{name}.mo %buildroot%_datadir/locale/en_US/LC_MESSAGES/

for i in 16 22 32 48 64 128; 
do
	mkdir -p %buildroot%_datadir/icons/hicolor/${i}x${i}/apps
	mkdir -p %buildroot%_datadir/icons/oxygen/${i}x${i}/apps
	install -m 644 icons/oxygen/${i}/* %buildroot%_datadir/icons/oxygen/${i}x${i}/apps
        install -m 644 icons/hicolor/${i}/* %buildroot%_datadir/icons/hicolor/${i}x${i}/apps
done

desktop-file-install --delete-original          \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications               \
    %{name}.desktop

mkdir -p %buildroot%{_sysconfdir}/security/console.apps
install -m 644 etc/security/console.apps/improver %buildroot%{_sysconfdir}/security/console.apps/
mkdir -p %buildroot%{_sysconfdir}/pam.d
install -m 644 etc/pam.d/improver %buildroot%{_sysconfdir}/pam.d/

mkdir -p %buildroot%_bindir
cp -P $RPM_BUILD_DIR/%{name}-%{version}/ln/* %buildroot%_bindir

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

