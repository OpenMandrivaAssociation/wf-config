Name:           wf-config
Version:        0.7.1
Release:        4%{?dist}
Summary:        Library for managing configuration files, written for wayfire
 
License:        MIT
URL:            https://github.com/WayfireWM/wf-config
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47
 
BuildRequires:  cmake(glm)
%if %{with test}
BuildRequires:  cmake(doctest)
%endif
 
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
 
%description
%{summary}.
 
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
Development files for %{name}.
 
 
%prep
%autosetup -p1
 
 
%build
%if %{with test}
%meson \
    -Dtests=enabled
%else
%meson \
    -Dtests=disabled
%endif
 
%meson_build
 
%install
%meson_install
 
%if %{with test}
%check
%meson_test
%endif
 
 
%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*
%{_libdir}/lib%{name}.so.1*
 
%files devel
%{_includedir}/wayfire/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
