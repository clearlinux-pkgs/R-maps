#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-maps
Version  : 3.3.0
Release  : 56
URL      : https://cran.r-project.org/src/contrib/maps_3.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/maps_3.3.0.tar.gz
Summary  : Draw Geographical Maps
Group    : Development/Tools
License  : GPL-2.0
Requires: R-maps-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
separate packages ('mapproj' and 'mapdata').

%package lib
Summary: lib components for the R-maps package.
Group: Libraries

%description lib
lib components for the R-maps package.


%prep
%setup -q -c -n maps
cd %{_builddir}/maps

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589516294

%install
export SOURCE_DATE_EPOCH=1589516294
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maps
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library maps
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc maps || :


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
