%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

Name: gconnman
Summary: A GObject binding of the Connman D-Bus API
Group: User Interface/Desktops
Version: 0.5.0
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libmesagl-devel
BuildRequires: libglib2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: gtk+2-devel
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog COPYING NEWS
%{_libdir}/libgconnman*.so.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgconnman*.so
%{_libdir}/libgconnman*.a
%{_libdir}/libgconnman*.la
