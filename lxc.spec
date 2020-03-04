%global _release 20200302
%global debug_package %{nil}

Name:           lxc
Version:        3.0.3
Release:        %{_release}
Summary:        Linux Containers userspace tools
License:        LGPLv2+
URL:            http://linuxcontainers.org
Source0:        http://linuxcontainers.org/downloads/lxc-3.0.3.tar.gz
Patch6000:      lxc-CVE-2019-5736-runC-rexec-callers-as-memfd.patch
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
Patch9125:      0123-in-accordance-with-hook-spec-in-oci.patch
Patch9126:      0124-lxc-close-maincmd-fd-before-destroy-cgroup.patch
Patch9127:      0125-lxc-fix-strcat-bug-in-cleanpath.patch
Patch9128:      0126-add-user-option-for-lxc-attach.patch
Patch9129:      0127-log-only-write-size-begin-if-buffer-is-full.patch
Patch9130:      0128-link-proc-mounts-to-etc-mtab.patch
Patch9131:      0129-cgfsng-add-retry-for-enter-cgroup.patch
Patch9132:      0130-fix-snprintf-create-abstract-socket-name-bug.patch
Patch9133:      0131-fix-commands-and-terminal-memory-leak-bug.patch
Patch9134:      0132-lxc-fix-bug-in-cgroup-parent.patch
Patch9135:      0133-lxc-fix-bug-in-cgfsng.patch
Patch9136:      0134-lxc-do-cpuset-same-as-runc.patch
Patch9137:      0135-lxc-fix-code-warnings-for-cgfsng.c.patch
Patch9138:      0136-lxc-fix-retry-bug-in-cgroup.patch
Patch9139:      0137-lxc-fix-bug-in-read-proc.patch
Patch9140:      0138-resize-implement-resize-function-in-exec-start.patch
Patch9141:      0139-lxc-fix-get-cgroup-path-by-config-instead-of-cmd.patch
Patch9142:      0140-lxc-remove-umask-when-populate-devices.patch

BuildRequires:  systemd-units git libtool graphviz docbook2X doxygen chrpath
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  libcap libcap-devel libselinux-devel yajl yajl-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:       lxc-libs = 3.0.3-%{release}

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


%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/lxc-3.0.3}

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
Requires:       lxc = 3.0.3-%{release}
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
%autosetup -n lxc-3.0.3 -Sgit -p1

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

# remove libtool .la file
rm -rf %{buildroot}%{_libdir}/liblxc.la
rm -rf %{buildroot}%{_sbindir}/init.%{name}.static
rm -rf %{buildroot}%{_sysconfdir}/default/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/__pycache__
%check
make check
rm -rf %{buildroot}%{_datadir}/%{name}/__pycache__

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
* Thu Feb 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 3.0.3-20200214
- make lxc-libs package
* Thu Dec 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.0.3-20191218
- Package init
