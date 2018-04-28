%define	qmmp_ver	1.2.0
Summary:	Qmmp Plugin Pack
Summary(pl.UTF-8):	Zestaw wtyczek dla odtwarzacza Qmmp
Name:		qmmp-plugin-pack
Version:	1.2.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	458117797da6d2d388edc600a6169869
Patch0:		%{name}-x32.patch
URL:		http://qmmp.ylsoftware.com/plugins.php
BuildRequires:	Qt5Sql-devel >= 5.4.0
BuildRequires:	Qt5Widgets-devel >= 5.4.0
BuildRequires:	cmake >= 2.8.11
# libavcodec>=57.48.101 libavformat>=57.40.101 libavutil>=55.27.100 libswscale>=4.1.100
BuildRequires:	ffmpeg-devel >= 3.1
BuildRequires:	libmpg123-devel >= 1.13.0
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libxmp-devel >= 4.2.0
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
Requires:	qmmp-general-history = %{version}-%{release}
Requires:	qmmp-input-ffap = %{version}-%{release}
Requires:	qmmp-input-mpg123 = %{version}-%{release}
Requires:	qmmp-input-xmp = %{version}-%{release}
Requires:	qmmp-visual-goom = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin Pack is a set of extra plugins for Qmmp:
- Sample Rate Converter - resampler based on libsamplerate library
- FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and
  embedded cue support)
- MPG123 - MPEG v1/2 layer1/2/3 decoder with use of the libmpg123
  library
- XMP - module player with use of the libxmp library

%description -l pl.UTF-8
Plugin Pack to zestaw dodatkowych wtyczek dla odtwarzacza Qmmp:
- Sample Rate Converter - resampler oparty na bibliotece libsamplerate
- FFap - rozszerzony dekoder Monkey's Audio (APE) (24-bitowe próbki
  oraz obsługa wbudowanych metadanych cue)
- MPG123 - dekoder MPEG v1/2 layer1/2/3 wykorzystujący bibliotekę
  libmpg123
- XMP - odtwarzacz modułów wykorzystujący bibliotekę libxmp

%package -n qmmp-effect-srconverter
Summary:	Sample Rate Converter module for Qmmp
Summary(pl.UTF-8):	Moduł resamplujący dla Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	libsamplerate >= 0.1.2
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-effect-srconverter
Sample Rate Converter plugin is a resampler based on libsamplerate
library.

%description -n qmmp-effect-srconverter -l pl.UTF-8
Wtyczka Sample Rate Converter to resampler oparty na bibliotece
libsamplerate.

%package -n qmmp-engine-ffvideo
Summary:	FFVideo engine for Qmmp
Summary(pl.UTF-8):	Wtyczka silnika FFVideo dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	ffmpeg-libs >= 3.1
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-engine-ffvideo
FFmpeg-based video engine plugin for Qmmp.

%description -n qmmp-engine-ffvideo -l pl.UTF-8
Wtyczka silnika obrazu opartego na bibliotece FFmpeg dla odtwarzacza
Qmmp.

%package -n qmmp-general-history
Summary:	History general plugin for Qmmp
Summary(pl.UTF-8):	Wtyczka ogólna historii dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Sql >= 5.4.0
Requires:	Qt5Widgets >= 5.4.0
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-general-history
Listening History general plugin for Qmmp.

%description -n qmmp-general-history -l pl.UTF-8
Wtyczka ogólna z historią odtwarzania dla odtwarzacza Qmmp.

%package -n qmmp-input-ffap
Summary:	FFap input plugin for Qmmp
Summary(pl.UTF-8):	Wtyczka wejściowa FFap dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	qmmp >= %{qmmp_ver}
Requires:	taglib >= 1.10

%description -n qmmp-input-ffap
FFap input plugin is an enhanced Monkey's Audio (APE) decoder with
24-bit samples and embedded cue support.

%description -n qmmp-input-ffap -l pl.UTF-8
Wtyczka wejściowa FFap to rozszerzony dekoder Monkey's Audio (APE),
obsługujący 24-bitowe próbki oraz wbudowane metadane cue.

%package -n qmmp-input-mpg123
Summary:	MPG123 input plugin for Qmmp
Summary(pl.UTF-8):	Wtyczka wejściowa MPG123 dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	libmpg123 >= 1.13.0
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-input-mpg123
MPG123 input plugin is an MPEG v1/2 layer1/2/3 decoder with use of the
libmpg123 library.

%description -n qmmp-input-mpg123
Wtyczka wejściowa MPG123 to dekoder MPEG v1/2 layer1/2/3,
wykorzystujący bibliotekę libmpg123.

%package -n qmmp-input-xmp
Summary:	XMP input plugin for Qmmp
Summary(pl.UTF-8):	Wtyczka wejściowa XMP dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	libxmp >= 4.2.0
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-input-xmp
XMP input plugin is a module player with use of the libxmp library.

%description -n qmmp-input-xmp -l pl.UTF-8
Wtyczka wejściowa XMP to odtwarzacz modułów wykorzystujący bibliotekę
libxmp.

%package -n qmmp-visual-goom
Summary:	Goom visualization plugin for Qmmp
Summary(pl.UTF-8):	Wtyczka wizualizacji Goom dla odtwarzacza Qmmp
Group:		Libraries
Requires:	Qt5Widgets >= 5.4.0
Requires:	qmmp >= %{qmmp_ver}

%description -n qmmp-visual-goom
Goom visualization plugin for Qmmp.

%description -n qmmp-visual-goom -l pl.UTF-8
Wtyczka wizualizacji Goom dla odtwarzacza Qmmp.

%prep
%setup -q
%patch0 -p1

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

%files -n qmmp-effect-srconverter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/Effect/libsrconverter.so

%files -n qmmp-engine-ffvideo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/Engines/libffvideo.so

%files -n qmmp-general-history
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/General/libhistory.so

%files -n qmmp-input-ffap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/Input/libffap.so

%files -n qmmp-input-mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/Input/libmpg123.so

%files -n qmmp-input-xmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qmmp/Input/libxmp.so

%files -n qmmp-visual-goom
%defattr(644,root,root,755)
%doc src/Visual/goom/CHANGES
%attr(755,root,root) %{_libdir}/qmmp/Visual/libgoom.so
