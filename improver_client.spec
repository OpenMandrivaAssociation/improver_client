%define protocol_name "augeas_protocol"
%define protocol_version 2.0

Summary:        Improver client
Name:           improver_client
Version:        %{protocol_version}.0
Release:        27
License:        GPL
URL:            http://www.rosalab.ru
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gnome-doc-utils
BuildRequires:  libgnomeui2-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libbonoboui2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  sqlite3-devel
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

%files -f %name.lang
%doc AUTHORS COPYING INSTALL README NEWS
%{_sysconfdir}/*
%{_bindir}/improver
%{_bindir}/improver_client
%{_bindir}/script_hw
%{_bindir}/script_hw_info_tar
%{_bindir}/script_hw_info
%{_bindir}/script_convert_screenshots
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/icons/oxygen/*
%{_datadir}/%{name}/pixmaps/
%{_datadir}/%{name}/bd*
%{_datadir}/%{name}/improver_client.conf
%{_datadir}/%{name}/improver_client.glade

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%configure
%make

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/improver
echo "%{name} %{version}-%{release}" > %buildroot%_sysconfdir/improver/client_version.conf
echo "%{protocol_name} %{protocol_version}" > %buildroot%_sysconfdir/improver/protocol_version.conf

mkdir -p %buildroot%_datadir/%{name}/pixmaps
install -m 644 usr/share/%{name}/pixmaps/*.png %buildroot%_datadir/%{name}/pixmaps
install -m 644 usr/share/%{name}/pixmaps/*.svg %buildroot%_datadir/%{name}/pixmaps
install -m 644 usr/share/%{name}/%name.glade %buildroot%_datadir/%{name}

install -m 755 usr/bin/script_hw %buildroot%_bindir

mkdir -p %buildroot/usr/bin
install -m 755 usr/bin/script_hw_info_tar %buildroot%_bindir
install -m 755 usr/bin/script_hw_info %buildroot%_bindir
install -m 755 usr/bin/script_convert_screenshots %buildroot%_bindir

install -m 644 usr/share/improver_client/improver_client.conf %buildroot%_datadir/%{name}
install -m 644 usr/share/improver_client/bd %buildroot%_datadir/%{name}
install -m 644 usr/share/improver_client/bd_clean %buildroot%_datadir/%{name}

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

%find_lang %name

