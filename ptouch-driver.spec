Name:           ptouch-driver
Version:        1.3
Release:        2.1%{?dist}
Summary:        CUPS driver for Brother P-touch label printers

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.diku.dk/~panic/P-touch/
Source0:        http://www.diku.dk/~panic/P-touch/%{name}-%{version}.tar.gz
Patch0:         ptouch-driver-1.2-gcc43.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cups-devel
BuildRequires:  automake
Requires:       cups

%description
This is a CUPS raster filter for Brother P-touch label printers.  It is
meant to be used by the PostScript Description files of the drivers from
the foomatic package.

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
# On 64bits, we need to install into lib, not lib64
# and this package for some reason uses libdir
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install-exec DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/lib/cups/filter/rastertoptch
%doc AUTHORS ChangeLog COPYING NEWS README

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Lubomir Rintel <lkundrak@v3.sk> 1.3-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.2-9
- Fix build with gcc-4.3

* Wed Aug 22 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-8
- Bump revision for BuildID in -debuginfo rebuild

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-7
- Modify the License tag in accordance with the new guidelines

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-6
- No. No automake. For the kids!

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-5
- ...and call it

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-4
- ...the specific version of automake

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-3
- We need automake for patch0 to have effect

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-2
- Install to the right place on 64bit platforms

* Fri Jul 20 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.2-1
- Initial package
