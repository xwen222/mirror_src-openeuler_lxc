%global _release 2020112701

Name:           lxc
Version:        4.0.3
Release:        %{_release}
Summary:        Linux Containers userspace tools
License:        LGPLv2+
URL:            https://github.com/lxc/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/lxc-4.0.3.tar.gz

Patch0001:	0001-huawei-adapt-to-huawei-4.0.3.patch
Patch0002:	0002-add-mount-label-for-rootfs.patch
Patch0003:	0003-format-code-and-verify-mount-mode.patch
Patch0004:	0004-Removes-the-definition-of-the-thread-attributes-obje.patch
Patch0005:	0005-solve-coredump-bug-caused-by-fstype-being-NULL-durin.patch
Patch0006:	0006-SIGTERM-do-not-catch-signal-SIGTERM-in-lxc-monitor.patch
Patch0007:	0007-Using-string-type-instead-of-security_context_t-beca.patch
Patch0008:	0008-hook-pass-correct-mount-dir-as-root-to-hook.patch
Patch0009:	0009-cgroup-refact-cgroup-manager-to-single-file.patch
Patch0010:	0010-cgfsng-adjust-log-level-from-error-to-warn.patch
Patch0011:	0011-rootfs-add-make-private-for-root.path-parent.patch
Patch0012:	0012-mount-make-possible-to-bind-mount-proc-and-sys-fs.patch

BuildRequires:  systemd-units git libtool graphviz docbook2X doxygen chrpath
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  libcap libcap-devel libselinux-devel yajl yajl-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:       lxc-libs = 4.0.3-%{release}

%package           libs
Summary:           Runtime library files for %{name}
Requires:          rsync
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description    libs
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-libs package contains libraries for running %{name} applications.


%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/lxc-4.0.3}

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools and libraries for running lxc
applications, which can be used to start a single daemon in a container, or to
boot an entire "containerized" system, and to manage and debug your containers.

%package        devel
Summary:        Development files for lxc
Requires:       lxc = 4.0.3-%{release}
Requires:       pkgconfig

%description    devel
The lxc-devel package contains header files ,library and templates needed for
development of the Linux containers.


%package        help
Summary:        Documentation and templates for lxc
BuildArch:      noarch

%description    help
This package contains documentation for lxc for creating containers.

%prep
%autosetup -n lxc-4.0.3 -Sgit -p1

%build
%configure --enable-doc --enable-api-docs \
           --disable-silent-rules --docdir=%{_pkgdocdir} --disable-rpath \
           --disable-static --disable-apparmor --enable-selinux \
           --enable-seccomp \
           --with-init-script=systemd --disable-werror

%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/__pycache__
touch %{buildroot}%{_datadir}/%{name}/__pycache__/%{name}

for file in $(find %{buildroot}/usr/bin/lxc-* -type f -exec file {} ';' | grep "\<ELF\>" | grep -vE "*\.static" | awk -F ':' '{print $1}')
do
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/sbin/* -type f -exec file {} ';' | grep "\<ELF\>" | grep -vE "*\.static" | awk -F ':' '{print $1}')
do
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/libexec/lxc/lxc-* -type f -exec file {} ';' | grep "\<ELF\>" | grep -vE "*\.static" | awk -F ':' '{print $1}')
do
    chrpath -d ${file}
done

chrpath -d %{buildroot}/usr/lib64/liblxc.so
chmod +x %{buildroot}/usr/lib64/liblxc.so
# docs
mkdir -p %{buildroot}%{_pkgdocdir}/api
cp -a AUTHORS README %{buildroot}%{_pkgdocdir}
cp -a doc/api/html/* %{buildroot}%{_pkgdocdir}/api/

# cache dir
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}

if [ ! -d %{buildroot}%{_sysconfdir}/sysconfig ]
then
    mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
    touch %{buildroot}%{_sysconfdir}/sysconfig/%{name}
fi

# remove libtool .la file
rm -rf %{buildroot}%{_libdir}/liblxc.la
rm -rf %{buildroot}%{_sbindir}/init.%{name}.static
rm -rf %{buildroot}%{_sysconfdir}/default/%{name}
%check
make check

%post

%preun

%postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}-*
%{_datadir}/%{name}/%{name}.functions
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/lxc
%files libs
%defattr(-,root,root)
%{_libdir}/liblxc.so
%{_libdir}/liblxc.so.*
%{_libdir}/%{name}
%{_libexecdir}/%{name}
%{_sbindir}/init.%{name}
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%config(noreplace) %{_sysconfdir}/lxc/*
%config(noreplace) %{_sysconfdir}/sysconfig/*

%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README
%license COPYING
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-net.service
%dir %{_localstatedir}/cache/%{name}

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/hooks
%{_datadir}/%{name}/lxc-patch.py*
%{_datadir}/%{name}/selinux
%dir %{_datadir}/%{name}/templates
%{_datadir}/%{name}/templates/lxc-*
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/config/*
%dir %{_datadir}/%{name}/__pycache__
%{_datadir}/%{name}/__pycache__/*


%files help
%dir %{_pkgdocdir}
%{_pkgdocdir}/*
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_mandir}/man7/%{name}*
%{_mandir}/*/man5/%{name}*
%{_mandir}/*/man7/%{name}*

%changelog
* Fri Nov 27 2020 lifeng <lifeng68@openeuler.org> - 4.0.3-2020112701
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: mount: make possible to bind mount /proc and /sys/fs.
-	1. add check whether have /proc mounts entry, if has, skip the auto
-	2. mount cgroup before do mount entrys
-	3. pass if the mount on top of /proc and the source of the mount is a proc filesystem

* Fri Nov 13 2020 lifeng <lifeng68@openeuler.org> - 4.0.3-2020111701
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add make private for root.path parent 

* Fri Nov 13 2020 lifeng <lifeng68@openeuler.org> - 4.0.3-2020111301
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: adjust log level from error to warn 

* Tue Nov 3 2020 lifeng <lifeng68@openeuler.org> - 4.0.3-2020110301
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: 1. fix hook root dir error and refact cgroup

* Sat Oct 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020101001
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add patchs to series.conf

* Fri Sep 25 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020092501
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: Code optimization

* Fri Sep 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020091101
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: modify source0 address

* Wed Sep 02 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020090101
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: modify source0 address 

* Mon Aug 03 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020080301
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add debug packages

* Mon Apr 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.3-2020071501
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: update lxc to 4.0.3
