Name:           wf-config
Version:        0.8.0
Release:        1
Summary:        Library for managing configuration files, written for wayfire
Group:          Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wf-config
Source0:        https://github.com/WayfireWM/wf-config/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig(glm)
# Needed only for test
#BuildRequires:  cmake(doctest)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayland-protocols)
 
%description
A library for managing configuration files, written for wayfire
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
Development files for %{name}.
 
%prep
%autosetup -p1
 

%build
%meson \
    -Dtests=disabled
 
%meson_build
 
%install
%meson_install
 
%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*
%{_libdir}/lib%{name}.so.1*
 
%files devel
%{_includedir}/wayfire/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
