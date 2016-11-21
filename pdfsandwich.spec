%define debug_package  %{nil}

Summary:	A tool to make sandwich OCR pdf files
Name:		pdfsandwich
Version:	0.1.5
Release:	0
Group:		Graphics
License:	GPLv2
Url:		http://www.tobias-elze.de/pdfsandwich/
Source0:	http://sourceforge.net/projects/pdfsandwich/files/%{name}-%{version}.tar.bz2

BuildRequires:	ocaml-compiler

Requires:	unpaper
Suggests:	tesseract >= 3.03
#Optional:	exact-image

%description
# from the homepage
pdfsandwich generates "sandwich" OCR pdf files, i.e. pdf files which contain
only images (but no editable text) will be processed by optical character
recognition (OCR) and the text will be added to each page invisibly "behind"
the images.

pdfsandwich is a command line tool which is supposed to be useful to OCR
scanned books or journals. It is able to recognize the page layout even for
multicolumn text.

Essentially, pdfsandwich is a wrapper script which calls the following
binaries: convert, unpaper, tesseract, gs, and hocr2pdf (if
tesseract < 3.03). It is known to run on Unix systems and has been tested on
Linux and MacOS X. It supports parallel processing on multiprocessor
systems.

In contrast to most competing sandwich programs, it performs preprocessing
of the scanned images, such as de-skewing or removal of dark edges etc.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc changelog
%doc copyright

#--------------------------------------------------------------------

%prep
%setup -q

%build
# NOTE: actually ./configure only accepts --prefix=,
#       so all other errors can be safely ignored
%configure 
%make

%install
%makeinstall_std

