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
BuildRequires:  perl-FindBin
BuildRequires:  perl-Time-Piece
BuildRequires:  perl
BuildRequires:  perl-core
BuildRequires:  gperf
# ---- 编译工具链 ----
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  patch
BuildRequires:  pkgconf-pkg-config
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  which

# ---- Perl（LibreOffice 大量依赖）----
BuildRequires:  perl
BuildRequires:  perl-core
BuildRequires:  perl-FindBin
BuildRequires:  perl-Time-Piece
BuildRequires:  perl-Archive-Zip
BuildRequires:  perl-JSON-PP
BuildRequires:  perl-Digest-MD5
BuildRequires:  perl-Data-Dump
BuildRequires:  perl-Locale-gettext

# ---- Python ----
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-polib
BuildRequires:  python3-setuptools

# ---- 构建辅助 ----
BuildRequires:  bc
BuildRequires:  findutils
BuildRequires:  git
BuildRequires:  rsync
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  cppunit-devel

# ---- 必需的开发库（engine 依赖）----
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libcap-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  expat-devel
BuildRequires:  dbus-devel
BuildRequires:  cups-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXi-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  nss-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  graphite2-devel
BuildRequires:  libicu-devel
BuildRequires:  lcms2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  libcurl-devel
BuildRequires:  boost-devel
BuildRequires:  glm-devel
BuildRequires:  libatomic

# ---- Qt6（Collabora Office 桌面版必需）----
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel

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

# ---- 构建工具 ----
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  hunspell-en-US
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  patch
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  glibc-all-langpacks
BuildRequires:  libappstream-glib
BuildRequires:  zip

# ---- Python ----
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-lxml
BuildRequires:  python3-polib

# ---- 通用库 / 头文件 ----
BuildRequires:  Box2D-devel
BuildRequires:  boost-devel
BuildRequires:  cups-devel
BuildRequires:  dragonbox-static
BuildRequires:  fast_float-devel
BuildRequires:  fontpackages-devel
BuildRequires:  frozen-static
BuildRequires:  glm-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  hyphen-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libnumbertext-devel
BuildRequires:  lpsolve-devel
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  zxcvbn-c-devel
BuildRequires:  unixODBC-devel

# ---- pkgconfig 依赖 ----
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(cppunit) >= 1.14.0
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libcmis-0.6)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libeot)
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libexttextcat)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(liborcus-0.21)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(mythes)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(redland)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmlsec1-nss)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zxing)

# ---- 字体（engine 的 cppunit 测试用）----
BuildRequires:  dejavu-fonts-all
BuildRequires:  google-carlito-fonts
BuildRequires:  google-rubik-fonts
BuildRequires:  google-crosextra-caladea-fonts
BuildRequires:  google-noto-fonts-all
BuildRequires:  amiri-fonts
BuildRequires:  amiri-quran-fonts
BuildRequires:  liberation-mono-fonts
BuildRequires:  liberation-narrow-fonts
BuildRequires:  liberation-sans-fonts
BuildRequires:  liberation-serif-fonts
BuildRequires:  linux-libertine-fonts

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
BuildRequires:  npm
BuildRequires:  git

BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(icu-io)

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
