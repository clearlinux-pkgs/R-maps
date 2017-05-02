#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-maps
Version  : 3.1.1
Release  : 15
URL      : https://cran.r-project.org/src/contrib/maps_3.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/maps_3.1.1.tar.gz
Summary  : Draw Geographical Maps
Group    : Development/Tools
License  : GPL-2.0
Requires: R-maps-lib
Requires: R-mapproj
Requires: R-maptools
Requires: R-sp
BuildRequires : R-mapproj
BuildRequires : R-maptools
BuildRequires : R-sp
BuildRequires : clr-R-helpers

%description
Notes on creating new map databases.
1) See the references:
Richard A. Becker, and Allan R. Wilks,
"Maps in S",
emph{AT\&T Bell Laboratories Statistics Research Report [93.2], 1993.}

%package lib
Summary: lib components for the R-maps package.
Group: Libraries

%description lib
lib components for the R-maps package.


%prep
%setup -q -c -n maps

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492805786

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492805786
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maps
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library maps


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/maps/DESCRIPTION
/usr/lib64/R/library/maps/INDEX
/usr/lib64/R/library/maps/Meta/Rd.rds
/usr/lib64/R/library/maps/Meta/data.rds
/usr/lib64/R/library/maps/Meta/features.rds
/usr/lib64/R/library/maps/Meta/hsearch.rds
/usr/lib64/R/library/maps/Meta/links.rds
/usr/lib64/R/library/maps/Meta/nsInfo.rds
/usr/lib64/R/library/maps/Meta/package.rds
/usr/lib64/R/library/maps/NAMESPACE
/usr/lib64/R/library/maps/NEWS.Rd
/usr/lib64/R/library/maps/R/maps
/usr/lib64/R/library/maps/R/maps.rdb
/usr/lib64/R/library/maps/R/maps.rdx
/usr/lib64/R/library/maps/README.md
/usr/lib64/R/library/maps/data/Rdata.rdb
/usr/lib64/R/library/maps/data/Rdata.rds
/usr/lib64/R/library/maps/data/Rdata.rdx
/usr/lib64/R/library/maps/help/AnIndex
/usr/lib64/R/library/maps/help/aliases.rds
/usr/lib64/R/library/maps/help/maps.rdb
/usr/lib64/R/library/maps/help/maps.rdx
/usr/lib64/R/library/maps/help/paths.rds
/usr/lib64/R/library/maps/html/00Index.html
/usr/lib64/R/library/maps/html/R.css
/usr/lib64/R/library/maps/mapdata/county.G
/usr/lib64/R/library/maps/mapdata/county.L
/usr/lib64/R/library/maps/mapdata/county.N
/usr/lib64/R/library/maps/mapdata/france.G
/usr/lib64/R/library/maps/mapdata/france.L
/usr/lib64/R/library/maps/mapdata/france.N
/usr/lib64/R/library/maps/mapdata/italy.G
/usr/lib64/R/library/maps/mapdata/italy.L
/usr/lib64/R/library/maps/mapdata/italy.N
/usr/lib64/R/library/maps/mapdata/lakes.G
/usr/lib64/R/library/maps/mapdata/lakes.L
/usr/lib64/R/library/maps/mapdata/lakes.N
/usr/lib64/R/library/maps/mapdata/legacy_world.G
/usr/lib64/R/library/maps/mapdata/legacy_world.L
/usr/lib64/R/library/maps/mapdata/legacy_world.N
/usr/lib64/R/library/maps/mapdata/legacy_world2.G
/usr/lib64/R/library/maps/mapdata/legacy_world2.L
/usr/lib64/R/library/maps/mapdata/legacy_world2.N
/usr/lib64/R/library/maps/mapdata/nz.G
/usr/lib64/R/library/maps/mapdata/nz.L
/usr/lib64/R/library/maps/mapdata/nz.N
/usr/lib64/R/library/maps/mapdata/state.G
/usr/lib64/R/library/maps/mapdata/state.L
/usr/lib64/R/library/maps/mapdata/state.N
/usr/lib64/R/library/maps/mapdata/state.carto.G
/usr/lib64/R/library/maps/mapdata/state.carto.L
/usr/lib64/R/library/maps/mapdata/state.carto.N
/usr/lib64/R/library/maps/mapdata/state.vbm.G
/usr/lib64/R/library/maps/mapdata/state.vbm.L
/usr/lib64/R/library/maps/mapdata/state.vbm.N
/usr/lib64/R/library/maps/mapdata/usa.G
/usr/lib64/R/library/maps/mapdata/usa.L
/usr/lib64/R/library/maps/mapdata/usa.N
/usr/lib64/R/library/maps/mapdata/world.G
/usr/lib64/R/library/maps/mapdata/world.L
/usr/lib64/R/library/maps/mapdata/world.N
/usr/lib64/R/library/maps/mapdata/world2.G
/usr/lib64/R/library/maps/mapdata/world2.L
/usr/lib64/R/library/maps/mapdata/world2.N

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/maps/libs/maps.so
