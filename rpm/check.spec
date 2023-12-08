Name:       check
Summary:    A unit test framework for C
Version:    0.15.2
Release:    1
License:    LGPLv2+
URL:        https://libcheck.github.io/check/
Source0:    %{name}-%{version}.tar.gz
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:    cmake

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests
are run in a separate address space, so Check can catch both assertion
failures and code errors that cause segmentation faults or other signals.
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary:    Libraries and headers for developing programs with check
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check

%description static
Static libraries of check.

%package checkmk
Summary:    Translate concise versions of test suites into C programs
License:    checkmk
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description checkmk
The checkmk binary translates concise versions of test suites into C
programs suitable for use with the Check unit test framework.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

%cmake
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING.LESSER
%doc README.md
%{_libdir}/libcheck.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/libcheck.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/check.pc

#check used to be static only, hence this.
%files static
%license COPYING.LESSER
%{_libdir}/libcheck.a

%files checkmk
%doc checkmk/README checkmk/examples
%{_bindir}/checkmk
%{_mandir}/man1/checkmk.1*
