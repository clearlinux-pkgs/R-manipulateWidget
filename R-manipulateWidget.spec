#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-manipulateWidget
Version  : 0.11.1
Release  : 55
URL      : https://cran.r-project.org/src/contrib/manipulateWidget_0.11.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/manipulateWidget_0.11.1.tar.gz
Summary  : Add Even More Interactivity to Interactive Charts
Group    : Development/Tools
License  : GPL-2.0+ MIT
Requires: R-base64enc
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-knitr
Requires: R-miniUI
Requires: R-shiny
Requires: R-shinyjs
Requires: R-webshot
BuildRequires : R-base64enc
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-knitr
BuildRequires : R-miniUI
BuildRequires : R-shiny
BuildRequires : R-shinyjs
BuildRequires : R-webshot
BuildRequires : buildreq-R

%description
helps to easily add controls like sliders, pickers, checkboxes, etc. that 
    can be used to modify the input data or the parameters of an interactive 
    chart created with package 'htmlwidgets'.

%prep
%setup -q -c -n manipulateWidget
cd %{_builddir}/manipulateWidget

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641052826

%install
export SOURCE_DATE_EPOCH=1641052826
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulateWidget
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulateWidget
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulateWidget
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc manipulateWidget || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/manipulateWidget/DESCRIPTION
/usr/lib64/R/library/manipulateWidget/INDEX
/usr/lib64/R/library/manipulateWidget/LICENSE
/usr/lib64/R/library/manipulateWidget/Meta/Rd.rds
/usr/lib64/R/library/manipulateWidget/Meta/data.rds
/usr/lib64/R/library/manipulateWidget/Meta/features.rds
/usr/lib64/R/library/manipulateWidget/Meta/hsearch.rds
/usr/lib64/R/library/manipulateWidget/Meta/links.rds
/usr/lib64/R/library/manipulateWidget/Meta/nsInfo.rds
/usr/lib64/R/library/manipulateWidget/Meta/package.rds
/usr/lib64/R/library/manipulateWidget/Meta/vignette.rds
/usr/lib64/R/library/manipulateWidget/NAMESPACE
/usr/lib64/R/library/manipulateWidget/NEWS.md
/usr/lib64/R/library/manipulateWidget/R/manipulateWidget
/usr/lib64/R/library/manipulateWidget/R/manipulateWidget.rdb
/usr/lib64/R/library/manipulateWidget/R/manipulateWidget.rdx
/usr/lib64/R/library/manipulateWidget/data/Rdata.rdb
/usr/lib64/R/library/manipulateWidget/data/Rdata.rds
/usr/lib64/R/library/manipulateWidget/data/Rdata.rdx
/usr/lib64/R/library/manipulateWidget/doc/index.html
/usr/lib64/R/library/manipulateWidget/doc/manipulateWidgets.R
/usr/lib64/R/library/manipulateWidget/doc/manipulateWidgets.Rmd
/usr/lib64/R/library/manipulateWidget/doc/manipulateWidgets.html
/usr/lib64/R/library/manipulateWidget/help/AnIndex
/usr/lib64/R/library/manipulateWidget/help/aliases.rds
/usr/lib64/R/library/manipulateWidget/help/manipulateWidget.rdb
/usr/lib64/R/library/manipulateWidget/help/manipulateWidget.rdx
/usr/lib64/R/library/manipulateWidget/help/paths.rds
/usr/lib64/R/library/manipulateWidget/html/00Index.html
/usr/lib64/R/library/manipulateWidget/html/R.css
/usr/lib64/R/library/manipulateWidget/htmlwidgets/combineWidgets.css
/usr/lib64/R/library/manipulateWidget/htmlwidgets/combineWidgets.js
/usr/lib64/R/library/manipulateWidget/htmlwidgets/combineWidgets.yaml
/usr/lib64/R/library/manipulateWidget/lib/export/Blob/Blob.js
/usr/lib64/R/library/manipulateWidget/lib/export/Blob/LICENSE.md
/usr/lib64/R/library/manipulateWidget/lib/export/FileSaver/FileSaver.min.js
/usr/lib64/R/library/manipulateWidget/lib/export/FileSaver/LICENSE.md
/usr/lib64/R/library/manipulateWidget/lib/export/canvas-toBlob/LICENSE.md
/usr/lib64/R/library/manipulateWidget/lib/export/canvas-toBlob/canvas-toBlob.js
/usr/lib64/R/library/manipulateWidget/lib/export/html2canvas/html2canvas.js
/usr/lib64/R/library/manipulateWidget/manipulate_widget/manipulate_widget.css
/usr/lib64/R/library/manipulateWidget/manipulate_widget/manipulate_widget.js
/usr/lib64/R/library/manipulateWidget/tests/testthat.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/helper-input_class.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-controller.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-get_output_and_render_func.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-input_class.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-input_env.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-input_list_class.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-inputs.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-manipulate_widget.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-mwGroup.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-mwModuleUI.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-on_done.R
/usr/lib64/R/library/manipulateWidget/tests/testthat/test-staticPlot.R
