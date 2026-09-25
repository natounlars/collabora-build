# 动态版本号宏 - 从本地 git 仓库提取
%global git_repo ~/vcs/libreoffice-git/core
%global _enable_gdb_index 0
%global debug_package %{nil}
%global __desktop_provides %{nil}
# 提取版本信息（类似 PKGBUILD 的 pkgver()）
%global git_desc %(cd %{git_repo} && git describe --long --tags 2>/dev/null || echo "libreoffice-0.0.0-0-gunknown")
%global libo_major %(echo %{git_desc} | sed -E 's/^libreoffice-([0-9]+)-?([0-9]+)?.*/\\1.\\2/' | sed 's/\\.$/.0/')
%global git_rev_count %(cd %{git_repo} && git rev-list --count HEAD)
%global git_short_hash %(cd %{git_repo} && git rev-parse --short HEAD)

Name:           libreoffice-git
Epoch:          1
# 使用 git describe 提取的主版本号.提交次数.g短哈希
Version:        %{libo_major}.r%{git_rev_count}.g%{git_short_hash}
Release:	1%{?dist}
Summary:        A powerful office suite with full features (local git build)
License:        MPL-2.0 AND Apache-2.0 AND LGPL-3.0-only AND LGPL-3.0-or-later AND CC0-1.0 AND BSD-3-Clause
URL:            https://www.libreoffice.org/

# 无 Source0 - 使用本地 git 仓库
Source0:        %{git_repo}

BuildArch:      x86_64

# 构建依赖（保持你原来的精简列表，补充必要的）
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  hunspell-devel
BuildRequires:  hyphen-devel
BuildRequires:  icu
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mythes-devel
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  patch
BuildRequires:  perl
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(mariadb)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  rust
BuildRequires:  unixODBC-devel
BuildRequires:  zip
BuildRequires:  git 

%ifarch x86_64
BuildRequires:  junit
BuildRequires:  hamcrest
BuildRequires:  cargo
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libdrm-devel
BuildRequires:  gobject-introspection-devel
# 添加这些缺失的构建依赖
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  libtool-ltdl-devel
BuildRequires:  boost-devel
BuildRequires:  glm-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  lpsolve-devel
BuildRequires:  libnumbertext-devel
BuildRequires:  zxcvbn-c-devel
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libcmis-0.6)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libexttextcat)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(redland)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmlsec1-nss)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zxing)
BuildRequires:  pkgconfig(cppunit) >= 1.14.0
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(mythes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  dragonbox-static
BuildRequires:  fast_float-devel
BuildRequires:  frozen-static
BuildRequires:  Box2D-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel 

# KF5 集成依赖
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdelibs4support-devel 
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwindowsystem-devel

# KF6 集成依赖
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  hamcrest
BuildRequires:  nasm
BuildRequires:  meson
%endif

# 运行时依赖
Requires:       liberation-fonts
Requires:       dejavu-fonts-all

Provides:       libreoffice = %{epoch}:%{version}-%{release}
Provides:       libreoffice-fresh = %{epoch}:%{version}-%{release}
Conflicts:      libreoffice
Conflicts:      libreoffice-fresh
Conflicts:      libreoffice-still

%description
LibreOffice is an Open Source, community-developed, office productivity suite.
This package is built from local git repository with maximum features
and performance optimizations enabled.

%prep
# 清理并复制本地 git 仓库到构建目录
rm -rf %{_builddir}/%{name}-%{version}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{git_repo}
git clone --local --no-hardlinks . %{_builddir}/%{name}-%{version}
rm -rf %{_builddir}/%{name}-%{version}/.git
%setup -q -T -D -n %{name}-%{version}

%build
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-$(date +%s)}
echo "SOURCE_DATE_EPOCH set to: $SOURCE_DATE_EPOCH"  # 调试输出
# 设置编译标志
export CFLAGS="-O2 -pipe -Wall -Wno-error"
export CXXFLAGS="-O2 -pipe -Wall -Wno-error"
export LDFLAGS="-Wl,-z,relro -Wl,--as-needed"
export CC=clang
export CXX=clang++

export CCACHE_BASEDIR="$PWD"
export CCACHE_COMPRESS=1
export CCACHE_MAXSIZE=50G
echo "lo_sources_ver=26.2.3.1" > sources.ver
export PYTHONPATH=$PYTHONPATH:/home/natounlars/rpmbuild/BUILD/libreoffice-git-26.8.r%{git_rev_count}.g%{git_short_hash}-build/onlineupdate/source/update/updater
# 配置 - 功能最全 + 性能最佳
./autogen.sh \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/libreoffice \
    \
    --enable-release-build \
    --disable-online-update \
    --enable-optimized=yes \
    --enable-pch=full \
    --enable-mergelibs=more \
    --enable-split-debug \
    --enable-runtime-optimizations \
    \
    --enable-python=internal \
    --enable-odk \
    --enable-introspection \
    --enable-extension-integration \
    \
    --enable-gtk3 \
    --enable-gtk4 \
    --enable-qt5 \
    --enable-qt6 \
    --enable-kf5 \
    --enable-kf6 \
    --enable-gen \
    --enable-headless \
    \
    --enable-dbus \
    --enable-gio \
    --enable-avahi \
    --enable-gstreamer-1-0 \
    --enable-avmedia \
    --enable-opengl \
    --enable-opencl \
    --enable-skia \
    --enable-cairo-canvas \
    --enable-cairo-rgba \
    \
    --enable-database-connectivity \
    --enable-mariadb-sdbc \
    --enable-postgresql-sdbc \
    --enable-firebird-sdbc \
    --enable-report-builder \
    --enable-extension-update \
    --enable-ext-wiki-publisher \
    --enable-ext-nlpsolver \
    \
    --enable-pdfimport \
    --enable-pdfium \
    --enable-eot \
    --enable-librelogo \
    --enable-ldap \
    --enable-cups \
    --enable-gpgmepp \
    --enable-xmlhelp \
    \
    --enable-scripting \
    --enable-scripting-beanshell \
    --enable-scripting-javascript \
    --enable-rust-uno \
    --enable-cli \
    \
    --enable-symbols \
    \
    --with-java=java \
    \
    --with-lang=ALL \
    --with-galleries=build \
    --with-fonts \
    --with-myspell-dicts \
    --with-theme="breeze breeze_dark breeze_dark_svg breeze_svg colibre colibre_svg colibre_dark colibre_dark_svg elementary elementary_svg karasa_jaga karasa_jaga_svg sifr sifr_dark sifr_dark_svg sifr_svg sukapura sukapura_dark sukapura_dark_svg sukapura_svg" \
    \
    --with-parallelism=$(nproc) \
    --with-product-name="LibreOfficeDev" \
    --with-privacy-policy-url="https://www.libreoffice.org/privacy" \
    --without-system-harfbuzz \
    --with-system-icu \
    --enable-ccache

# 编译

%make_build -j$(nproc)

%install
# 安装
make DESTDIR=%{buildroot} distro-pack-install

for app in base calc draw impress math writer web fromtemplate; do
    ln -sf libreoffice %{buildroot}%{_bindir}/libreoffice-${app}
done

# 安装配置文件
install -dm755 %{buildroot}%{_sysconfdir}/libreoffice
for file in bootstraprc sofficerc; do
    src=$(find %{buildroot} -name "$file" -path "*/program/$file" | head -1)
    if [ -n "$src" ]; then
        install -m644 "$src" %{buildroot}%{_sysconfdir}/libreoffice/
        # 创建符号链接
        dir=$(dirname "$src")
        ln -sf %{_sysconfdir}/libreoffice/$file "$dir/$file"
    fi
done
src=$(find %{buildroot} -name "psprint.conf" | head -1)
if [ -n "$src" ]; then
    install -m644 "$src" %{buildroot}%{_sysconfdir}/libreoffice/
    dir=$(dirname "$src")
    ln -sf %{_sysconfdir}/libreoffice/psprint.conf "$dir/psprint.conf"
fi



# 安装 Python 绑定到 site-packages
install -dm755 %{buildroot}%{python3_sitearch}

pushd %{buildroot}%{python3_sitearch}
    echo "import sys, os" > uno.py
    echo "sys.path.append('%{_prefix}/lib/libreoffice/program/')" >> uno.py
    echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{_prefix}/lib/libreoffice/program/fundamentalrc')" >> uno.py
    cat %{buildroot}%{_prefix}/lib/libreoffice/program/uno.py >> uno.py
    rm -f %{buildroot}%{_prefix}/lib/libreoffice/program/uno.py*
    mv -f %{buildroot}%{_prefix}/lib/libreoffice/program/unohelper.py* . 2>/dev/null || true
    mv -f %{buildroot}%{_prefix}/lib/libreoffice/program/officehelper.py* . 2>/dev/null || true
popd

# 创建 LibreOfficeKit 符号链接
ln -sf %{_prefix}/lib/libreoffice/program/liblibreofficekitgtk.so \
    %{buildroot}%{_libdir}/liblibreofficekitgtk.so

# 安装 metainfo
install -dm755 %{buildroot}%{_datadir}/metainfo
install -v -m644 sysui/desktop/appstream-appdata/*.xml \
    %{buildroot}%{_datadir}/metainfo/ 2>/dev/null || true

# 安装模板
install -dm755 %{buildroot}%{_datadir}/templates/.source
if [[ -f extras/source/shellnew/soffice.odt ]]; then
    install -v -m644 extras/source/shellnew/soffice.{odt,ods,odp,odg} \
        %{buildroot}%{_datadir}/templates/.source/
fi

# 清理不需要的文件
rm -f %{buildroot}%{_prefix}/lib/libreoffice/program/classes/smoketest.jar

find %{buildroot} -type f \( -name "*.py" -o -name "*-gdb.py" \) \
    -exec sed -i '1s|#!/usr/bin/python$|#!/usr/bin/python3|' {} + 2>/dev/null || true

# 修复 .desktop 文件的 Exec= 指向
for desktop in %{buildroot}%{_datadir}/applications/libreoffice-*.desktop; do
    [ -f "$desktop" ] || continue
    
    # 获取应用名称（如 writer, calc, impress 等）
    basename=$(basename "$desktop" .desktop)
    app=${basename#libreoffice-}
    
    # 将 libreofficedev26.8 替换为对应的 lo* 启动器
    case "$app" in
        writer)   launcher="lowriter" ;;
        calc)     launcher="localc" ;;
        impress)  launcher="loimpress" ;;
        draw)     launcher="lodraw" ;;
        math)     launcher="lomath" ;;
        base)     launcher="lobase" ;;
        startcenter) launcher="loffice" ;;
        xsltfilter)  launcher="loffice" ;;
        *)        launcher="loffice" ;;
    esac

# 动态匹配 libreofficedev + 任意数字/点，替换为正确的启动器
    sed -i -E "s|Exec=libreofficedev[0-9.]+|Exec=$launcher|g" "$desktop"
    # 同时处理可能的其他变体
    sed -i -E "s|Exec=libreoffice[0-9]*\.?[0-9]*|Exec=$launcher|g" "$desktop"    
done

%files
%license %{_prefix}/lib/libreoffice/LICENSE
%doc %{_prefix}/lib/libreoffice/CREDITS.fodt
%doc %{_prefix}/lib/libreoffice/NOTICE

%{_bindir}/lobase
%{_bindir}/localc
%{_bindir}/lodraw
%{_bindir}/lomath
%{_bindir}/loimpress
%{_bindir}/loweb
%{_bindir}/lowriter
%{_bindir}/lofromtemplate
%{_bindir}/loffice
%{_bindir}/libreoffice
%{_bindir}/libreoffice-*
%{_bindir}/unopkg

%dir %{_prefix}/lib/libreoffice
%{_prefix}/lib/libreoffice/program/
%{_prefix}/lib/libreoffice/share/
%{_libdir}/liblibreofficekitgtk.so

# === 新增：SDK 头文件 ===
%{_includedir}/libreoffice/
%{_datadir}/doc/libreoffice/

# === 新增：bash 补全 ===
%{_datadir}/bash-completion/completions/libreoffice.sh

# === 新增：SDK Java classes ===
%{_datadir}/libreoffice/sdk/classes/

# === 新增：man 页面 ===
%{_mandir}/man1/unopkg.1.gz

# === 新增：metainfo ===
%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml

%{_prefix}/lib64/*

%{_prefix}/lib/libreoffice/LICENSE.html

%{_bindir}/soffice

%dir %{_prefix}/lib/libreoffice
%{_prefix}/lib/libreoffice/**/*

%dir %{_sysconfdir}/libreoffice
%config(noreplace) %{_sysconfdir}/libreoffice/bootstraprc
%config(noreplace) %{_sysconfdir}/libreoffice/sofficerc
%config(noreplace) %{_sysconfdir}/libreoffice/psprint.conf

%{_datadir}/applications/libreoffice-*.desktop
%{_datadir}/icons/hicolor/*/apps/libreoffice-*.png
%{_datadir}/icons/hicolor/*/apps/libreoffice-*.svg
%{_datadir}/icons/hicolor/*/mimetypes/libreoffice-*.png
%{_datadir}/metainfo/libreoffice-*.appdata.xml
%{_datadir}/mime/packages/libreoffice.xml

%{_datadir}/templates/.source/

%{_mandir}/man1/libreoffice.1*
%{_mandir}/man1/lo*.1*

%{python3_sitearch}/uno.py*
%{python3_sitearch}/unohelper.py*
%{python3_sitearch}/officehelper.py*

%changelog
* Mon Apr 20 2026 Custom Builder <builder@localhost> - %{epoch}:%{version}-%{release}
- Local git build with dynamic version from git describe
- Full feature build with maximum performance optimizations
