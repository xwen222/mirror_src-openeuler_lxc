%global _release 2022102404

Name:           lxc
Version:        4.0.3
Release:        %{_release}
Summary:        Linux Containers userspace tools
License:        LGPLv2+ and GPLv2 and GPLv3
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
Patch0013:	0013-use-path-based-unix-domain-sockets-instead-of-abstra.patch
Patch0014:	0014-api-add-get-container-metrics-api.patch
Patch0015:	0015-Streaming-IO-solution-optimization-and-enhancement.patch
Patch0016:	0016-avoid-using-void-pointers-in-caclulation.patch
Patch0017:	0017-fix-compilation-errors-without-libcap.patch
Patch0018:	0018-IO-fix-io-data-miss-when-exec-with-pipes.patch
Patch0019:	0019-metrics-add-total_inactive_file-metric-for-memory.patch
Patch0020:	0020-support-cgroup-v2.patch
Patch0021:	0021-support-isula-exec-workdir.patch
Patch0022:	0022-print-error-message-if-process-workdir-failed.patch
Patch0023:	0023-log-support-long-syslog-tag.patch
Patch0024:	0024-log-adjust-log-level-from-error-to-warn.patch
Patch0025:	0025-get-cgroup-data-len-first-and-malloc-read-buff-by-le.patch
Patch0026:	0026-coredump-fix-coredump-when-cgroup-get-return-error.patch
Patch0027:	0027-add-help-for-new-arguments.patch
Patch0028:	0028-seccomp-init-and-destroy-notifier.cookie.patch
Patch0029:	0029-just-use-origin-loop-if-do-not-have-io.patch
Patch0030:	0030-conf-fix-a-memory-leak.patch
Patch0031:	0031-fix-lsm_se_mount_context-memory-leak.patch
Patch0032:	0032-disable-lxc_keep-with-oci-image.patch
Patch0033:	0033-conf-ensure-that-the-idmap-pointer-itself-is-freed.patch
Patch0034:	0034-cgfsng-fix-cgroup-attach-cgroup-creation.patch
Patch0035:	0035-adapt-upstream-compiler-settings.patch
Patch0036:	0036-compile-in-android-env.patch
Patch0037:	0037-fix-always-print-and-temp-len.patch
Patch0038:	0038-just-print-error-when-new-lock-failed.patch
Patch0039:	0039-fix-bug-of-memory-free.patch
Patch0040:	0040-refactor-the-way-to-convert-selinux-label-to-shared.patch
Patch0041:	0041-do-not-free-the-pointer-returned-by-dirname.patch
Patch0042:	0042-add-x-permission-when-create-directory.patch
Patch0043:	0043-do-not-operate-playload-and-attach-cgroup-if-no-cont.patch
Patch0044:	0044-fix-HOME-env-unset-error.patch
Patch0045:	0045-only-set-user-or-image-set-non-empty-HOME.patch
Patch0046:	0046-return-fail-if-no-args-or-no-rootfs-path-found.patch
Patch0047:	0047-fix-tools-with-option-give-error-message.patch
Patch0048:	0048-fix-do-mask-paths-after-parent-mounted.patch
Patch0049:	0049-skip-kill-cgroup-processes-if-no-hierarchies.patch
Patch0050:	0050-lxc-Add-sw64-architecture.patch
Patch0051:	0051-add-macro-to-adapt-musl-libc.patch
Patch0052:	0052-add-lxc-attach-add-gids-option.patch

BuildRequires:  systemd-units git libtool graphviz docbook2X doxygen chrpath
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  libcap libcap-devel libselinux-devel yajl yajl-devel
BuildRequires:  pkgconfig(bash-completion)

Requires:       lxc-libs = 4.0.3-%{release}

%package           libs
Summary:           Runtime library files for %{name}
Requires:          rsync libcap libseccomp libselinux
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

%ifarch sw_64
chrpath -d %{buildroot}/usr/lib/liblxc.so
chmod +x %{buildroot}/usr/lib/liblxc.so
%else
chrpath -d %{buildroot}/usr/lib64/liblxc.so
chmod +x %{buildroot}/usr/lib64/liblxc.so
%endif
# docs
mkdir -p %{buildroot}%{_pkgdocdir}/api
%ifarch sw_64
%else
cp -a AUTHORS README %{buildroot}%{_pkgdocdir}
cp -a doc/api/html/* %{buildroot}%{_pkgdocdir}/api/
%endif

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
%ifarch sw_64
%else
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_mandir}/man7/%{name}*
%{_mandir}/*/man5/%{name}*
%{_mandir}/*/man7/%{name}*
%endif

%changelog
* Fri Dec 02 2022 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2022102404
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: add lxc-attach add-gids option

* Thu Nov 24 2022 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2022102403
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: add macro to adapt musl libc

* Mon Oct 24 2022 wuzx<wuzx1226@qq.com> - 4.0.3-2022102401
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add sw64 architecture

* Mon Oct 17 2022 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2022101701
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: update version to 4.0.3-2022101701

* Tue Oct 11 2022 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2022101101
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: skip kill cgroup processes if no hierarchies

* Tue Sep 20 2022 Neil.wrz<wangrunze13@huawei.com> - 4.0.3-2022092001
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: do mask paths after parent mounted

* Fri Sep 02 2022 Neil.wrz<wangrunze13@huawei.com> - 4.0.3-2022090201
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix tools using -? option give error

* Wed Aug 31 2022 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2022083101
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: return fail if no args or no rootfs path founds

* Fri Aug 12 2022 haozi007<liuhao27@huawei.com> - 4.0.3-2022081201
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: only set user or image set non empty HOME

* Mon Jul 25 2022 haozi007<liuhao27@huawei.com> - 4.0.3-2022072501
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix HOME env unset error

* Wed May 25 2022 hejunjie<hejunjie10@huawei.com> - 4.0.3-2022052501
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: correct license info

* Mon May 23 2022 wangfengtu<wangfengtu@huawei.com> - 4.0.3-2022052301
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: do not operate playload and attach cgroup if no controller found

* Sat May 21 2022 wangfengtu<wangfengtu@huawei.com> - 4.0.3-2022052101
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: add x permission when create directory

* Fri Apr 15 2022 wujing<wujing50@huawei.com> - 4.0.3-2022041501
- Type:refactor
- ID:NA
- SUG:NA
- DESC: refactor the way to convert selinux label to shared mode

* Sat Apr 09 2022 wujing<wujing50@huawei.com> - 4.0.3-2022040901
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix bug of memory free

* Thu Mar 17 2022 haozi007<liuhao27@huawei.com> - 4.0.3-2022031701
- Type:improve
- ID:NA
- SUG:NA
- DESC: fix unnecessary print error message

* Mon Feb 21 2022 chegJH   <hejunjie10@huawei.com> - 4.0.3-2022022101
- Type:improve
- ID:NA
- SUG:NA
- DESC: fix alwasy print and len

* Tue Feb 15 2022 chegJH   <hejunjie10@huawei.com> - 4.0.3-2022021501
- Type:improve
- ID:NA
- SUG:NA
- DESC:changes for compile in android env

* Mon Dec 27 2021 haozi007 <liuhao27@huawei.com> - 4.0.3-2021122701
- Type:improve
- ID:NA
- SUG:NA
- DESC:adapt upstream compiler settings

* Thu Nov 25 2021 wangfengtu<wangfengtu@huawei.com> - 4.0.3-2021112501
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix cgroup attach cgroup creation

* Fri Nov 19 2021 wangfengtu<wangfengtu@huawei.com> - 4.0.3-2021111901
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:ensure that the idmap pointer itself is freed

* Thu Oct 21 2021 gaohuatao<gaohuatao@huawei.com> - 4.0.3-2021102101
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:disable lxc_keep

* Sun Sep 26 2021 chengzeruizhi<chengzeruizhi@huawei.com> - 4.0.3-2021092601
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add dependencies under require field

* Fri Sep 17 2021 zhangxiaoyu<zhangxiaoyu58@huawei.com> - 4.0.3-2021091703
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix conf memory leak

* Fri Sep 17 2021 haozi007<liuhao27@huawei.com> - 4.0.3-2021091702
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:just use origin loop if do not have io

* Fri Sep 17 2021 zhangxiaoyu <zhangxiaoyu58@huawei.com> - 4.0.3-2021091701
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:seccomp init and destroy notifier.cookie

* Thu Aug 26 2021 haozi007 <liuhao27@huawei.com> - 4.0.3-2021082601
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add help info for new arguments

* Sat Jun 12 2021 lifeng <lifeng68@huawei.com> - 4.0.3-2021061201
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix coredump

* Tue Jun 01 2021 zhangxiaoyu <zhangxiaoyu58@huawei.com> - 4.0.3-2021060101
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:adjust log level

* Thu May 13 2021 lifeng <lifeng68@huawei.com> - 4.0.3-2021051301
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:adjust log level

* Sat May 08 2021 haozi007 <liuhao27@huawei.com> - 4.0.3-2021050802
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:support long syslog tag

* Sat May 08 2021 wangfengtu <wangfengtu@huawei.com> - 4.0.3-2021050801
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:print error message if process workdir failed

* Wed Apr 07 2021 wangfengtu <wangfengtu@huawei.com> - 4.0.3-2021040701
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:some patches missing in series.conf

* Wed Mar 31 2021 wangfengtu <wangfengtu@huawei.com> - 4.0.3-2021033101
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: support cgroup v2

* Thu Mar 11 2021 wangfengtu <wangfengtu@huawei.com> - 4.0.3-2021031102
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: support isula exec --workdir

* Thu Jan 28 2021 lifeng <lifeng68@huawei.com> - 4.0.3-2021012801
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add inactive file total metrics

* Thu Jan 21 2021 lifeng <lifeng68@huawei.com> - 4.0.3-2021012001
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: fix io data miss when exec with pipes

* Tue Jan 05 2021 wujing <wujing50@huawei.com> - 4.0.3-2021010501
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: fix compilation errors without libcap 

* Thu Dec 24 2020 wujing <wujing50@huawei.com> - 4.0.3-2020122401
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: Streaming IO solution optimization and enhancement

* Tue Dec 15 2020 lifeng <lifeng68@huawei.com> - 4.0.3-2020121501
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add get container metrics api to get the stat

* Mon Dec 07 2020 wujing <wujing50@huawei.com> - 4.0.3-2020120701
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: use path based unix domain sockets instead of abstract namespace sockets

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
