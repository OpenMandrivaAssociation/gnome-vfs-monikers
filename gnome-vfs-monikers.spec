%define name gnome-vfs-monikers

%define req_libbonobo_version	2.3.1
%define req_gconf2_version	1.1.1
%define req_orbit_version	2.9.0
%define req_vfs_version 	2.15.3

Summary:	GNOME virtual file-system monikers
Name:		%name
Version: 2.15.3
Release: %mkrel 1
License:	LGPL
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gawk
BuildRequires:  perl-XML-Parser
BuildRequires:	gnome-vfs2-devel >= %req_vfs_version
BuildRequires:	libbonobo2_x-devel >= %{req_libbonobo_version}
BuildRequires:	libGConf2-devel >= %{req_gconf2_version}
BuildRequires:	libORBit2-devel >= %{req_orbit_version}
BuildRequires:  gtk-doc
BuildRequires:  glib2-devel >= 2.9.3

%description
The GNOME Virtual File System provides an abstraction to common file
system operations like reading, writing and copying files, listing
directories and so on.  It is similar in spirit to the Midnight
Commander's VFS (as it uses a similar URI scheme) but it is designed
from the ground up to be extensible and to be usable from any
application.

This contains the monikers split from the main gnome-vfs2 package.


%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc=yes

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# don't package these
rm -f %buildroot%{_libdir}/bonobo/monikers/*a

%clean
rm -rf %{buildroot}



%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%_libdir/bonobo/monikers/libmoniker_gnome_vfs_std.so
%_libdir/bonobo/servers/GNOME_VFS_Moniker_std.server

