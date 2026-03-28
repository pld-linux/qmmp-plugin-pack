%define	qmmp_ver	1.6.0
Summary:	Qmmp Plugin Pack
Summary(pl.UTF-8):	Zestaw wtyczek dla odtwarzacza Qmmp
Name:		qmmp-plugin-pack
Version:	2.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://qmmp.ylsoftware.com/files/qmmp-plugin-pack/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	ec219e524e099f8ccb6f8fad8d08b63f
URL:		http://qmmp.ylsoftware.com/plugins.php
BuildRequires:	Qt5Sql-devel >= 5.4.0
BuildRequires:	Qt5Widgets-devel >= 5.4.0
BuildRequires:	cmake >= 2.8.11
# libavcodec>=57.48.101 libavformat>=57.40.101 libavutil>=55.27.100 libswscale>=4.1.100
BuildRequires:	ffmpeg-devel >= 3.1
BuildRequires:	libmpg123-devel >= 1.13.0
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	pkgconfig
BuildRequires:	qmmp-devel >= %{qmmp_ver}
BuildRequires:	qt5-build >= 5.4.0
BuildRequires:	qt5-linguist >= 5.4.0
BuildRequires:	taglib-devel >= 1.10
%ifarch %{ix86} %{x8664} x32
BuildRequires:	yasm
%endif
Requires:	qmmp-effect-srconverter = %{version}-%{release}
Requires:	qmmp-engine-ffvideo = %{version}-%{release}
Requires:	qmmp-input-ffap = %{version}-%{release}
Requires:	qmmp-visual-goom = %{version}-%{release}
Obsoletes:	qmmp-effect-srconverter < 2.3.0-1
Obsoletes:	qmmp-engine-ffvideo < 2.3.0-1
Obsoletes:	qmmp-general-history < 1.3.1-1
Obsoletes:	qmmp-input-ffap < 2.3.0-1
Obsoletes:	qmmp-input-mpg123 < 1.3.1-1
Obsoletes:	qmmp-visual-goom < 2.3.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin Pack is a set of extra plugins for Qmmp:
- Sample Rate Converter - resampler based on libsamplerate library
- FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and
  embedded cue support)
- MPG123 - MPEG v1/2 layer1/2/3 decoder with use of the libmpg123
  library

%description -l pl.UTF-8
Plugin Pack to zestaw dodatkowych wtyczek dla odtwarzacza Qmmp:
- Sample Rate Converter - resampler oparty na bibliotece libsamplerate
- FFap - rozszerzony dekoder Monkey's Audio (APE) (24-bitowe próbki
  oraz obsługa wbudowanych metadanych cue)
- MPG123 - dekoder MPEG v1/2 layer1/2/3 wykorzystujący bibliotekę
  libmpg123

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog.svn
%lang(ru) %doc ChangeLog.rus README.RUS
%{_libdir}/qmmp-2.3/Effect/libsrconverter.so
%{_libdir}/qmmp-2.3/Engines/libffvideo.so
%{_libdir}/qmmp-2.3/Engines/libmplayer.so
%{_libdir}/qmmp-2.3/Input/libffap.so
%{_libdir}/qmmp-2.3/Input/libmodplug.so
%{_libdir}/qmmp-2.3/Transports/libmms.so
%{_libdir}/qmmp-2.3/Transports/libytb.so
%{_libdir}/qmmp-2.3/Visual/libgoom.so
%{_metainfodir}/qmmp-plugin-pack.appdata.xml
