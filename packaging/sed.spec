%define _bindir /bin

Name:       sed
Summary:    A GNU stream text editor
Version:    4.1.5
Release:    1
Group:      Applications/Text
License:    GPLv2+
URL:        http://sed.sourceforge.net/
Source0:    ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz


%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.




%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static \
    --without-included-regex \
    --disable-nls

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs


%check
make check

%files
%{_bindir}/sed


