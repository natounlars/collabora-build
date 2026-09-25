# ---- 基础配置 ----------------------------------------------------------
%global base_version %(cat %{_sourcedir}/version.txt 2>/dev/null || echo 25.04.7.8.1)
%global appname      collabora-office
%global _builddir_c  %{_builddir}/collabora-office
%global _package_note_flags %{nil}
%global _annotated_build %{nil}
%global _hardened_build 0
%global _hardening_cflags %{nil}
%global _hardening_ldflags %{nil}
%global optflags %(echo %{optflags} | sed 's|-specs=/usr/lib/rpm/redhat/redhat-hardened-cc1||g; s|-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1||g; s|-specs=/usr/lib/rpm/redhat/redhat-package-notes||g')


Name:           collabora-office
Version:        %{base_version}
# 用 copr_commit 让每个 COPR 构建唯一；不在 COPR 时降级到 %{?dist}
Release:        1%{?copr_commit:.%{copr_commit}}%{?dist}
Summary:        Collabora Office - LibreOffice-based desktop office suite
License:        MPL-2.0 AND LGPL-3.0-or-later
URL:            https://www.collaboraoffice.com/

# 关键：Source 是脚本，不是 tarball
Source0:        get_collabora.sh
Source1:        get_translations.sh
Source2:        version.txt

# 关闭 strip / debuginfo 以减小构建产物
%global debug_package         %{nil}
%global __strip               /bin/true
%global __brp_mangle_shebangs %{nil}
%global __brp_check_rpaths    %{nil}
%define _unpackaged_files_terminate_build 0

# ---- 构建依赖 ----------------------------------------------------------
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libcap-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  npm
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl-JSON-PP
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3-lxml
BuildRequires:  python3-polib
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  desktop-file-utils
BuildRequires:  rpm-build

# ---- 运行时依赖 --------------------------------------------------------
Requires: glibc
Requires: libX11
Requires: libXcomposite
Requires: libXdamage
Requires: libXext
Requires: libXfixes
Requires: libXrandr
Requires: libXcursor
Requires: libXi
Requires: libXScrnSaver
Requires: libxkbfile
Requires: libsecret
Requires: gtk3
Requires: nss
Requires: alsa-lib
Requires: libdrm
Requires: mesa-libgbm
Requires: cups-libs

%description
Collabora Office is a LibreOffice-based desktop office suite built on Qt6 WebEngine.
This package is built directly from the upstream main branch of the Gerrit
monorepo at build time.

%prep
export RPM_ARCH="$(uname -m)"
export RPM_PACKAGE_NAME="%{name}"
export RPM_PACKAGE_VERSION="%{version}"
export RPM_PACKAGE_RELEASE="%{release}"
export RPM_BUILD_DIR="%{_builddir}"
# 清理历史构建（COPR 可能缓存 build 目录）
rm -rf %{_builddir_c}
rm -f  %{_builddir}/version.txt

# 把 Source2 放到位（供 %prep 内的 shell 脚本使用）
cp -f %{SOURCE2} %{_builddir}/version.txt

# 调用脚本拉取源码（需要 --enable-net on）
bash %{SOURCE0} %{_builddir}
bash %{SOURCE1} %{_builddir_c}

%build
cd %{_builddir_c}/engine
./autogen.sh \
    --with-distro=CPLinux-LOKit \
    --without-package-format \
    --with-system-nss \
    --with-lang=zh-CN
make -j$(nproc) %{?_smp_mflags}

cd %{_builddir_c}
./autogen.sh --enable-qtapp --disable-server
make -j$(nproc) %{?_smp_mflags}

%install
rm -rf %{buildroot}

# 安装 coda-qt
install -Dm 755 %{_builddir_c}/qt/coda-qt \
    %{buildroot}%{_bindir}/%{appname}

# 安装 engine 运行时
mkdir -p %{buildroot}%{_libdir}/%{appname}
cp -a %{_builddir_c}/engine/instdir/. %{buildroot}%{_libdir}/%{appname}/

# 启动脚本
cat > %{buildroot}%{_bindir}/%{appname} <<'EOF'
#!/bin/bash
export LD_LIBRARY_PATH="/usr/lib64/collabora-office/program${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
exec /usr/lib64/collabora-office/program/coda-qt "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{appname}

# 桌面文件、图标、metainfo
install -Dm 644 %{_builddir_c}/qt/desktop/com.collaboraoffice.Office.desktop \
    %{buildroot}%{_datadir}/applications/com.collaboraoffice.Office.desktop
install -Dm 644 %{_builddir_c}/qt/desktop/com.collaboraoffice.Office.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/com.collaboraoffice.Office.metainfo.xml

# 图标
find %{_builddir_c}/qt/desktop -maxdepth 2 -name '*.svg' | while read -r icon; do
    install -Dm 644 "$icon" \
        "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/$(basename "$icon")"
done

%files
%{_bindir}/%{appname}
%{_libdir}/%{appname}
%{_datadir}/applications/com.collaboraoffice.Office.desktop
%{_datadir}/metainfo/com.collaboraoffice.Office.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%changelog
* Fri Sep 25 2026 Your Name <you@example.com> - %{version}-1
- Built from Collabora Office main branch via COPR SCM
