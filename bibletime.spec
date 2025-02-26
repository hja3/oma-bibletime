%define Werror_cflags %nil
Name:		bibletime
Version:		3.1.0
Release:		1
Summary:		Easy to use Bible study tool
License:		GPLv2+
Url:		https://www.bibletime.info/
Group:		Text tools
Source0:	https://github.com/bibletime/bibletime/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-xsl
BuildRequires:	pkgconfig(libclucene-core) >= 2.0
BuildRequires:	pkgconfig(sword) >= 1.8.1
BuildRequires:	po4a
BuildRequires:	xsltproc
Requires:	sword >= 1.8.1

%description
BibleTime is a free and easy to use bible study tool built with Qt.

BibleTime provides easy handling of digitized texts (Bibles, commentaries 
and lexicons) and powerful features to work with these texts (search in 
texts, write own notes, save, print etc.). Bibletime is a frontend for 
the SWORD Bible Framework.

%prep
%setup -qn %{name}-%{version}

%build
%cmake -G Ninja \
	     -DBUILD_HANDBOOK_PDF=OFF \
	     -DBUILD_HOWTO_PDF=OFF \
	     -DBUILD_HANDBOOK_HTML=OFF
%ninja

%install
%ninja_install -C build

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category="Office" \
	%{buildroot}%{_datadir}/applications/*.desktop


%files
%doc LICENSE README.md
%doc %{_datadir}/doc/bibletime/howto/html*
%{_bindir}/bibletime
%{_datadir}/bibletime
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/info.bibletime.BibleTime.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/info.bibletime.BibleTime.svg




