%global with_seccomp 1
%global _release 20190926
%global debug_package %{nil}

Name:           lxc
Version:        3.0.3
Release:        %{_release}%{?dist}
Summary:        Linux Containers userspace tools
License:        LGPLv2+
URL:            http://linuxcontainers.org
Source0:        http://linuxcontainers.org/downloads/%{name}-%{version}.tar.gz
Patch6000:      lxc-2.0.7-fix-init.patch
Patch6001:      lxc-2.0.6-fix-lxc-net.patch
Patch6002:      lxc-CVE-2019-5736-runC-rexec-callers-as-memfd.patch
Patch9003:      0001-confile-add-lxc.isulad.init.args-config-interface.patch
Patch9004:      0002-namespace-add-support-share-namespace-by-path.patch
Patch9005:      0003-confile-add-lxc.isulad.populate.device-interface.patch
Patch9006:      0004-support-isulad-fifo-log.patch
Patch9007:      0005-auto-mount-cgroup-sys-and-proc.patch
Patch9008:      0006-conf.c-fix-bug-when-set-no-ro-mount-mount-propagatio.patch
Patch9009:      0007-use-isulad-log-format.patch
Patch9010:      0008-isulad-modify-exit-code-and-stop-signal.patch
Patch9011:      0009-lxc_start-add-default-terminal-fifos.patch
Patch9012:      0010-Save-pid-ppid-info-into-file-for-isulad.patch
Patch9013:      0011-Add-exit-FIFO-to-monitor-state-of-lxc-monitor.patch
Patch9014:      0012-Init-fifos-in-lxc_attach_terminal.patch
Patch9015:      0013-isulad-set-env-home-in-container.patch
Patch9016:      0014-support-rotate-for-container-log-file.patch
Patch9017:      0015-fix-high-gcc-compile-bug.patch
Patch9018:      0016-add-masked-paths-and-ro-paths.patch
Patch9019:      0017-isulad-check-cgroup-cpu.shares-after-setted.patch
Patch9020:      0018-lxc-attach-add-support-terminal-fifos.patch
Patch9021:      0019-remount-cgroup-readonly-and-make-soft-link-of-subcgr.patch
Patch9022:      0020-fix-log-error-when-symlink-subcgroup.patch
Patch9023:      0021-lxc-attch-add-error-message.patch
Patch9024:      0022-support-rootfs-mount-propagation.patch
Patch9025:      0023-attach.c-change-uid-and-gid-from-lxc-container-confi.patch
Patch9026:      0024-isulad-support-symlink-in-mount-entry-and-not-permit.patch
Patch9027:      0025-support-oci-hooks.patch
Patch9028:      0026-remove-filelock-and-do-not-destroy-directory-when-de.patch
Patch9029:      0027-fix-bug-of-memory-leak.patch
Patch9030:      0028-support-rootfs-for-container.patch
Patch9031:      0029-add-start-timeout-to-limit-start-time.patch
Patch9032:      0030-support-block-device-as-rootfs.patch
Patch9033:      0031-clean-add-clean-resources-api.patch
Patch9034:      0032-Drop-all-caps-when-cap.keep-ISULAD_KEEP_NONE.patch
Patch9035:      0033-support-mount-squashfs-in-mount-entry.patch
Patch9036:      0034-some-small-bugfix.patch
Patch9037:      0035-lxc-fixup-builds-with-newer-glibc.patch
Patch9038:      0036-drop_caps-add-drop-caps-of-current-process.patch
Patch9039:      0037-restore-default-signal-handlers-and-set-umask-0027.patch
Patch9040:      0038-make-the-given-terminal-as-controlling-terminal.patch
Patch9041:      0039-print-error-message-when-container-start-failed.patch
Patch9042:      0040-add-timeout-200ms-for-cmds-send-to-lxc-monitor.patch
Patch9043:      0041-return-1-when-_lxc_start-fails.patch
Patch9044:      0042-lxc-seccomp-adopt-to-lxc3.0.patch
Patch9045:      0043-check-null-pointer-of-handler-to-fix-coredump-of-att.patch
Patch9046:      0044-support-space-in-volume-mount-and-env.patch
Patch9047:      0045-add_terminal_fifos-Add-terminal-fifos-dynamically.patch
Patch9048:      0046-Do-not-test-cgroup-writeable.patch
Patch9049:      0047-Fix-memory-leak-in-lxc_global_config_value.patch
Patch9050:      0048-clear-ONLCR-flag-from-master-of-terminal.patch
Patch9051:      0049-Add-100ms-timeout-for-console-epoll.patch
Patch9052:      0050-seccomp-add-rules-for-specified-architecture-only.patch
Patch9053:      0051-if-ocihook-is-empty.patch
Patch9054:      0052-Fix-seccomp-fail-when-all-specified-in-config.patch
Patch9055:      0053-destroy-empty-cgroup-path-return-ture.patch
Patch9056:      0054-fix-invalid-log-message.patch
Patch9057:      0055-Fix-compile-error.patch
Patch9058:      0056-caps-use-_LINUX_CAPABILITY_VERSION_3-to-set-cap.patch
Patch9059:      0057-confile-add-support-umask.patch
Patch9060:      0058-do-not-check-ppid-when-set-death-signal.patch
Patch9061:      0059-delete-unused-variable-ppid.patch
Patch9062:      0060-using-json-file-to-write-console-log-of-container.patch
Patch9063:      0061-Fix-hook-use-the-path-args-envs-execvp-dirctory.patch
Patch9064:      0062-setup-sysctls-before-set-read-only-path-and-masked-p.patch
Patch9065:      0063-lxc-ignore-systemcall-load-failure-error.patch
Patch9066:      0064-lxc-Reduce-seccomp-processing-log-level.patch
Patch9067:      0065-Storage-return-true-if-storage_init-init-fail.patch
Patch9068:      0066-lxc-Pids-limit-does-not-report-an-error-after-execut.patch
Patch9069:      0067-lxc-report-error-when-remove-directory-failed.patch
Patch9070:      0068-support-record-stdout-stderr-log-of-container-consol.patch
Patch9071:      0069-lxc-killall-processes-if-container-shared-pid-namesp.patch
Patch9072:      0070-lxc-signal-all-process-for-shared-container-when-con.patch
Patch9073:      0071-lxc-get-cgroup-path-according-to-cgroup-mountpoint.patch
Patch9074:      0072-lxc-adapt-to-docker-18.09.patch
Patch9075:      0073-lxc-support-set-additional-groups.patch
Patch9076:      0074-lxc-only-add-valid-fd-to-mainloop.patch
Patch9077:      0075-lxc-add-timeout-for-attach.patch
Patch9078:      0076-lxc-delete-unused-variable.patch
Patch9079:      0077-lxc-set-negative-files.limit-to-max-and-fix-bug-of-s.patch
Patch9080:      0078-Run-pre-start-hook-before-chroot.patch
Patch9081:      0079-inherid-env-from-parent-in-oci-hooks.patch
Patch9082:      0080-lxc-fix-compile-error.patch
Patch9083:      0081-lxc-Change-the-range-of-attach-timeout.patch
Patch9084:      0082-lxc-fix-memory-leak-cause-by-setenv.patch
Patch9085:      0083-lxc-free-lxc-handler.patch
Patch9086:      0084-lxc-memory-leak-of-lxc_grow_array.patch
Patch9087:      0085-lxc-update-json-file-from-isulad.patch
Patch9088:      0086-confile-add-support-systemd.patch
Patch9089:      0087-lxc-adapt-to-spec-of-oci-hook.patch
Patch9090:      0088-fix-lxc-build-error.patch
Patch9091:      0089-lxc-add-get-container-processes-pids-func.patch
Patch9092:      0090-lxc-remove-unused-variable.patch
Patch9093:      0091-lxc-support-namespaced-kernel-params-can-be-changed-.patch
Patch9094:      0092-lxc-add-output-error-when-create-unified-cgroup.patch
Patch9095:      0093-optimize-isulad_kit-operator.patch
Patch9096:      0094-exec-load-uid-gid-and-groups.patch
Patch9097:      0095-lxc-don-t-use-the-unified-hierarchy-for-the-systemd-.patch
Patch9098:      0096-close-inherited-fd-in-hook-process.patch
Patch9099:      0097-lxc-report-error-when-fork-exec-error-for-hooks.patch
Patch9100:      0098-lxc-make-dev-bind-mount-from-host-tmpfs-for-system-c.patch
Patch9101:      0099-terminal-do-not-close-the-master-fd-of-pty.patch
Patch9102:      0100-start-add-check-save-pid-info-file.patch
Patch9103:      0101-lxc-fix-code-error.patch
Patch9104:      0102-lxc-fix-compile-warnings.patch
Patch9105:      0103-lxc-fix-code-error-in-conf.c.patch
Patch9106:      0104-lxc-fix-code-error.patch
Patch9107:      0105-lxc-fix-code-error-warnings.patch
Patch9108:      0106-set-timeout-to-1s-for-cmds-send-to-lxc-monitor.patch
Patch9109:      0107-add-log-for-failure-of-rename-file.patch
Patch9110:      0108-check-calloc-input-valid.patch
Patch9111:      0109-add-secure-compile-flags-to-lxc.patch
Patch9112:      0110-add-doc-for-lxc.patch
Patch9113:      0111-lxc-use-safe_strdup-instead-of-strdup.patch
Patch9114:      0112-fix-secure-errors.patch
Patch9115:      0113-Malloc-parameter-check-and-judgment.patch
Patch9116:      0114-lxc-fix-code-errors.patch
Patch9117:      0115-fix-compile-error-on-ubuntu.patch
Patch9118:      0116-lxc-set-base-cgroup-path-to.patch
Patch9119:      0117-pupulate-device-with-dir-mode-750-and-set-uid-gid.patch
Patch9120:      0118-fix-sscanf-return-value-check.patch
Patch9121:      0119-remove-unuse-binary.patch
Patch9122:      0120-remove-unuse-unmount-namespace.patch
Patch9123:      0121-optimize-log-when-root-path-is-invalid.patch
Patch9124:      0122-lxc-fix-code-reivew-errors.patch

BuildRequires:  systemd-units
BuildRequires:  git libtool
BuildRequires:  docbook2X doxygen
BuildRequires:  chrpath
%if 0%{?with_seccomp}
BuildRequires:  pkgconfig(libseccomp)
%endif
BuildRequires:  libcap libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  yajl yajl-devel
BuildRequires:  libsecurec libsecurec-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:          rsync
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools and libraries for running %{name}
applications, which can be used to start a single daemon in a container, or to
boot an entire "containerized" system, and to manage and debug your containers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains header files ,library and templates needed for
development of the Linux containers.


%package        help
Summary:        Documentation and templates for %{name}
BuildArch:      noarch

%description    help
This package contains documentation for %{name} for creating containers.

%prep
%setup -q -n %{name}-%{version}
%patch6000 -p1
%patch6001 -p1
%patch6002 -p1
%patch9003 -p1
%patch9004 -p1
%patch9005 -p1
%patch9006 -p1
%patch9007 -p1
%patch9008 -p1
%patch9009 -p1
%patch9010 -p1
%patch9011 -p1
%patch9012 -p1
%patch9013 -p1
%patch9014 -p1
%patch9015 -p1
%patch9016 -p1
%patch9017 -p1
%patch9018 -p1
%patch9019 -p1
%patch9020 -p1
%patch9021 -p1
%patch9022 -p1
%patch9023 -p1
%patch9024 -p1
%patch9025 -p1
%patch9026 -p1
%patch9027 -p1
%patch9028 -p1
%patch9029 -p1
%patch9030 -p1
%patch9031 -p1
%patch9032 -p1
%patch9033 -p1
%patch9034 -p1
%patch9035 -p1
%patch9036 -p1
%patch9037 -p1
%patch9038 -p1
%patch9039 -p1
%patch9040 -p1
%patch9041 -p1
%patch9042 -p1
%patch9043 -p1
%patch9044 -p1
%patch9045 -p1
%patch9046 -p1
%patch9047 -p1
%patch9048 -p1
%patch9049 -p1
%patch9050 -p1
%patch9051 -p1
%patch9052 -p1
%patch9053 -p1
%patch9054 -p1
%patch9055 -p1
%patch9056 -p1
%patch9057 -p1
%patch9058 -p1
%patch9059 -p1
%patch9060 -p1
%patch9061 -p1
%patch9062 -p1
%patch9063 -p1
%patch9064 -p1
%patch9065 -p1
%patch9066 -p1
%patch9067 -p1
%patch9068 -p1
%patch9069 -p1
%patch9070 -p1
%patch9071 -p1
%patch9072 -p1
%patch9073 -p1
%patch9074 -p1
%patch9075 -p1
%patch9076 -p1
%patch9077 -p1
%patch9078 -p1
%patch9079 -p1
%patch9080 -p1
%patch9081 -p1
%patch9082 -p1
%patch9083 -p1
%patch9084 -p1
%patch9085 -p1
%patch9086 -p1
%patch9087 -p1
%patch9088 -p1
%patch9089 -p1
%patch9090 -p1
%patch9091 -p1
%patch9092 -p1
%patch9093 -p1
%patch9094 -p1
%patch9095 -p1
%patch9096 -p1
%patch9097 -p1
%patch9098 -p1
%patch9099 -p1
%patch9100 -p1
%patch9101 -p1
%patch9102 -p1
%patch9103 -p1
%patch9104 -p1
%patch9105 -p1
%patch9106 -p1
%patch9107 -p1
%patch9108 -p1
%patch9109 -p1
%patch9110 -p1
%patch9111 -p1
%patch9112 -p1
%patch9113 -p1
%patch9114 -p1
%patch9115 -p1
%patch9116 -p1
%patch9117 -p1
%patch9118 -p1
%patch9119 -p1
%patch9120 -p1
%patch9121 -p1
%patch9122 -p1
%patch9123 -p1
%patch9124 -p1

%build
%configure --with-distro=fedora --enable-doc --enable-api-docs \
           --disable-silent-rules --docdir=%{_pkgdocdir} --disable-rpath \
           --disable-static --disable-apparmor --enable-selinux \
%if 0%{?with_seccomp}
           --enable-seccomp \
%endif
           --with-init-script=systemd --disable-werror

%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

for file in $(find %{buildroot}/usr/bin/lxc-* -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}')
do
    strip --strip-debug ${file}
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/sbin/* -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}')
do
    strip --strip-debug ${file}
    chrpath -d ${file}
done

for file in $(find %{buildroot}/usr/libexec/lxc/lxc-* -type f -exec file {} ';' | grep "\<ELF\>" | awk -F ':' '{print $1}')
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

# remove libtool .la file
rm -rf %{buildroot}%{_libdir}/liblxc.la

%check
make check

%post
%{?ldconfig}
%systemd_post %{name}-net.service
%systemd_post %{name}.service
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}-net.service
%systemd_preun %{name}.service
%systemd_preun %{name}@.service

%postun
%{?ldconfig}
%systemd_postun %{name}-net.service
%systemd_postun %{name}.service
%systemd_postun %{name}@.service

%files
%defattr(-,root,root)
%{_bindir}/%{name}-*
%{_datadir}/%{name}/%{name}.functions
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%{_libdir}/liblxc.so
%{_libdir}/liblxc.so.*
%{_libdir}/%{name}
%{_libexecdir}/%{name}
%{_sbindir}/init.%{name}
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%license COPYING
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README
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
%{_datadir}/%{name}/%{name}-patch.py*
%{_datadir}/%{name}/selinux
%dir %{_datadir}/%{name}/templates
%{_datadir}/%{name}/templates/lxc-*
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/config/*

%files help
%dir %{_pkgdocdir}
%{_pkgdocdir}/*
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_mandir}/man7/%{name}*
%{_mandir}/*/man5/%{name}*
%{_mandir}/*/man7/%{name}*
