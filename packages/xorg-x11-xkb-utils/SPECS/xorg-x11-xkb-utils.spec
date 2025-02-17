# Component versions
%global setxkbmap 1.3.2
%global xkbcomp 1.4.2
%global xkbevd 1.1.4
%global xkbprint 1.0.4
%global xkbutils 1.0.4
%global _buildshell /usr/sgug/bin/bash

Summary:    X.Org X11 xkb utilities
Name:       xorg-x11-xkb-utils
Version:    7.7
Release:    31%{?dist}
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/setxkbmap-%{setxkbmap}.tar.bz2
Source1:    https://www.x.org/pub/individual/app/xkbcomp-%{xkbcomp}.tar.bz2
Source2:    https://www.x.org/pub/individual/app/xkbevd-%{xkbevd}.tar.bz2
Source3:    https://www.x.org/pub/individual/app/xkbprint-%{xkbprint}.tar.bz2
Source4:    https://www.x.org/pub/individual/app/xkbutils-%{xkbutils}.tar.bz2

Patch0: 0001-Suppress-high-keycode-warnings-at-the-default-warnin.patch

BuildRequires:  byacc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)

Provides:   setxkbmap = %{setxkbmap}
Provides:   xkbcomp = %{xkbcomp}

%description
X.Org X11 xkb core utilities.

%package devel
Summary:    X.Org X11 xkb utilities development package
Requires:   pkgconfig
Requires:   xkbcomp

%description devel
X.Org X11 xkb utilities development files.

%package -n xorg-x11-xkb-extras
Summary:    X.Org X11 xkb gadgets
Provides:   xkbevd = %{xkbevd}
Provides:   xkbprint = %{xkbprint}
Provides:   xkbutils = %{xkbutils}

%description -n xorg-x11-xkb-extras
X.Org X11 xkb gadgets.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4
pushd xkbcomp-*
%patch0 -p1
popd

%build
# Build all apps
{
    for app in * ; do
        pushd $app
            case $app in
                xkbcomp-*)
                    rm xkbparse.c # force regen
                    ;;
                *)
                    ;;
            esac
            %configure
            make %{?_smp_mflags}
        popd
    done
}

%install
# Install all apps
{
    for app in * ; do
        pushd $app
            %make_install
        popd
    done
}

%files
%{_bindir}/setxkbmap
%{_bindir}/xkbcomp
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/xkbcomp.1*

%files -n xorg-x11-xkb-extras
%doc xkbutils-%{xkbutils}/COPYING
%doc xkbutils-%{xkbutils}/README
%{_bindir}/xkbbell
%{_bindir}/xkbevd
%{_bindir}/xkbprint
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
%{_mandir}/man1/xkbbell.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xkbvleds.*
%{_mandir}/man1/xkbwatch.*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Adam Jackson <ajax@redhat.com> - 7.7-30
- setxkbmap 1.3.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Adam Jackson <ajax@redhat.com> - 7.7-28
- Suppress high-keycode warnings from xkbcomp

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Peter Hutterer <peter.hutterer@redhat.com> 7.7-26
- xkbcomp 1.4.2

* Thu Jun 07 2018 Peter Hutterer <peter.hutterer@redhat.com> 7.7-25
- Ignore maximum keycode range greater than 255 (#1587998)

* Tue Mar 13 2018 Adam Jackson <ajax@redhat.com> - 7.7-24
- Make -devel Require the base package, so the pc file will point to an
  xkbcomp that actually exists.

* Thu Mar 01 2018 Adam Jackson <ajax@redhat.com> - 7.7-23
- xkbcomp 1.4.1
- https URLs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Peter Hutterer <peter.hutterer@redhat.com> 7.7-19
- xkbcomp 1.4.0 (#1463366)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Thu Nov 05 2015 Peter Hutterer <peter.hutterer@redhat.com> 7.7-16
- xkbcomp 1.3.1 (#1010592)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Simone Caronni <negativo17@gmail.com> - 7.7-14
- setxkbmap 1.3.1
- xkbevd 1.1.4
- xkbprint 1.0.4

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 7.7-13
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Nov 21 2014 Peter Hutterer <peter.hutterer@redhat.com> 7.7-12
- xkbcomp 1.3.0

* Fri Nov 07 2014 Simone Caronni <negativo17@gmail.com> - 7.7-11
- Clean up SPEC file, build all components like other x11 packages.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-7
- Apply the patch this time...

* Tue May 21 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-6
- Add missing options to xkbcomp man page (#948842)

* Mon Feb 11 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-5
- xkbutils 1.0.4

* Tue Nov 13 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-4
- xkbcomp: Fix generation of XKB directory listing, missing reset on file
  handler caused parse errors and incomplete directory listings

* Tue Aug 28 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-2
- Remove duplicate sources

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-1
- X11R7.7 updates:
- xkbcomp 1.2.4
- setxkbmap 1.3.0
- xkbevd 1.1.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-5
- xkbcomp 1.2.3

* Fri Feb 11 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-4
- xkbcomp 1.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-2
- xkbprint-1.0.3

* Mon Nov 01 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-1
- setxkbmap 1.2.0
- xkbcomp 1.2.0
- xkbutils 1.0.3
- xkbevd 1.1.1

* Mon Oct 11 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.4-9
- xkbcomp-hex-parsing.patch: fix up parsing of hex-code symbols (#638244)

* Thu Jul 08 2010 Adam Jackson <ajax@redhat.com> 7.4-8
- xkbcomp-speed.patch: Backport performance changes from git master.
