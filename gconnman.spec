%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

Name: gconnman
Summary: A GObject binding of the Connman D-Bus API
Group: System/Configuration/Networking
Version: 0.5.0
License: LGPL 2.1
URL: http://www.moblin.org
Release: 5
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: connman-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gettext-devel

%description
Description: %{summary}

%package -n %{libname}
Summary: Gconnman library, GObject binding of the Connman D-Bus API
Group: System/Libraries

%description -n %{libname}
Description: %{summary}

%package -n %{develname}
Summary: Gconnman development package
Group: System/Libraries

Requires: %{libname} >= %{version}
Provides: %{name}-devel

%description -n %{develname}
Gconnman development package

%prep
%setup -q 
perl -pi -e 's,^./configure.*,,' ./autogen.sh

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc README AUTHORS ChangeLog COPYING NEWS
%{_libdir}/libgconnman*.so.*

%files -n %{develname}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgconnman*.so
%{_libdir}/libgconnman*.a
