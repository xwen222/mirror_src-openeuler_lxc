%global _release 2020042302
%global debug_package %{nil}

Name:           lxc
Version:        4.0.1
Release:        %{_release}
Summary:        Linux Containers userspace tools
License:        LGPLv2+
URL:            http://linuxcontainers.org
Source0:        lxc-4.0.1.tar.gz
Patch9000:      0001-iSulad-add-HAVE_ISULAD-macro.patch
Patch9001:      0002-confile-add-lxc.isulad.init.args-config-interface.patch
Patch9002:      0003-confile-add-lxc.isulad.populate.device-interface.patch
Patch9003:      0004-confile-add-support-umask.patch
Patch9004:      0005-cgroup-refact-cgroup-implemt.patch
Patch9005:      0006-modify-container-exit-code-and-stop-signal.patch
Patch9006:      0007-check-and-save-pid-info-file.patch
Patch9007:      0008-support-block-device-as-rootfs.patch
Patch9008:      0009-support-mount-squashfs-in-mount-entry.patch
Patch9009:      0010-IO-refact-terminal-progress.patch
Patch9010:      0011-add-exit-fifo-to-monitor-state-of-lxc-monitor.patch
Patch9011:      0012-Adapt-to-isulad-log.patch
Patch9012:      0013-set-env-in-container.patch
Patch9013:      0014-exec-refact-attach-progress.patch
Patch9014:      0015-add-masked-paths-and-readonly-paths.patch
Patch9015:      0016-start-separate-i-and-t.patch
Patch9016:      0017-attach-add_terminal_fifos-Add-terminal-fifos-dynamic.patch
Patch9017:      0018-pty-setup-pty-after-setup-rootfs-mount-options.patch
Patch9018:      0019-resize-implement-resize-function-in-exec-start.patch
Patch9019:      0020-confile-decode-escape-charactors-in-config.patch
Patch9020:      0021-cgroup-add-retry-for-destory-cgroups.patch
Patch9021:      0022-support-terminal-log.patch
Patch9022:      0023-Supporting-rootfs-mount-propagation.patch
Patch9023:      0024-start-do-not-check-ppid-when-set-death-signal.patch
Patch9024:      0025-support-oci-hooks.patch
Patch9025:      0026-Supporting-UID-GID-configuration.patch
Patch9026:      0027-Capabilites-security-feature-enhanced.patch
Patch9027:      0028-Supporting-workdir-configuration.patch
Patch9028:      0029-Supporting-additional-groups-configuration.patch
Patch9029:      0030-set-negative-files.limit-value-to-max.patch
Patch9030:      0031-head-file-remove-macro-HAVE_ISULAD-in-installed-head.patch
Patch9031:      0032-link-proc-mounts-to-etc-mtab.patch
Patch9032:      0033-build-add-secure-build-flags.patch
Patch9033:      0034-support-timeout.patch
Patch9034:      0035-Seccomp-security-feature-enhanced.patch
Patch9035:      0036-Security-coding-modification.patch
Patch9036:      0037-cgfsng-fix-build-error-device_cgroup_rule_parse.patch
Patch9037:      0038-Ignore-errors-when-loading-rules-fail.patch
Patch9038:      0039-net-adapt-to-isulad.patch
Patch9039:      0040-cgfsng-make-container-full-path-in-cgfsng_get_cgroup.patch
Patch9040:      0041-build-fix-some-bug-in-free-memory.patch
Patch9041:      0042-cgfsng-make-container-full-path-in-destory-cgroup.patch
Patch9042:      0043-support-error-report.patch
Patch9043:      0044-remove-filelock-in-destroy-dir.patch
Patch9044:      0045-restore-default-signal-handler.patch
Patch9045:      0046-add-support-systemd.patch
Patch9046:      0047-support-namespaced-kernel-params-can-be-changed-in-s.patch
Patch9047:      0048-don-t-use-the-unified-hierarchy-for-the-systemd-cgro.patch
Patch9048:      0049-make-dev-bind-mount-from-host-tmpfs-for-system-conta.patch
Patch9049:      0050-clean-add-init-fd-in-lxc_init_clean_handler.patch
Patch9050:      0051-init-pids-add-init-fd-in-lxc_init_pids_handler.patch
Patch9051:      0052-setupdev-add-judge-whether-have-mount-dev-entry.patch
Patch9052:      0053-attach-seprate-i-and-t-flags.patch
Patch9053:      0054-start-do-not-check-pid-die-when-lxc_poll-exit.patch
Patch9054:      0055-terminal-not-close-pipe-when-lxc_poll-exit.patch
Patch9055:      0056-attach-add-sigfd-to-monitor-the-exit-of-pid.patch
Patch9056:      0057-attach-add-read-data-from-attach-sigfd.patch

BuildRequires:  systemd-units git libtool graphviz docbook2X doxygen chrpath
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  libcap libcap-devel libselinux-devel yajl yajl-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:       lxc-libs = 4.0.1-%{release}

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


%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/lxc-4.0.1}

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
Requires:       lxc = 4.0.1-%{release}
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
%autosetup -n lxc-4.0.1 -Sgit -p1

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
    strip --strip-debug ${file}
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/sbin/* -type f -exec file {} ';' | grep "\<ELF\>" | grep -vE "*\.static" | awk -F ':' '{print $1}')
do
    strip --strip-debug ${file}
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/libexec/lxc/lxc-* -type f -exec file {} ';' | grep "\<ELF\>" | grep -vE "*\.static" | awk -F ':' '{print $1}')
do
    strip --strip-debug ${file}
    chrpath -d ${file}
done

strip --strip-debug %{buildroot}/usr/lib64/liblxc.so
chrpath -d %{buildroot}/usr/lib64/liblxc.so

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
* Mon Apr 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 4.0.1-2020042001
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: update lxc to 4.0.1
