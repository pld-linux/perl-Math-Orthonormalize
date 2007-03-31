#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Orthonormalize
Summary:	Math::Orthonormalize - Gram-Schmidt Orthonormalization of vectors
Summary(pl.UTF-8):	Math::Orthogonalize - ortogonalizacja wektorów metodą Grama-Schmidta
Name:		perl-Math-Orthonormalize
Version:	1.00
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99952630af206c46221256e32d3916ec
URL:		http://search.cpan.org/dist/Math-Orthonormalize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Symbolic >= 0.128
BuildRequires:	perl-Parse-RecDescent >= 1.8
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Orthonormalize offers subroutines to compute normalized or
non-normalized orthogonal bases of Euclidean vector spaces. That
means: Given a vector base of R^n, it computes a new base of R^n whose
individual vectors are all orthogonal. If those new base vectors all
have a length of 1, the base is orthonormalized.

The module uses the Gram-Schmidt Algorithm.

No subroutines are exported by default, but the standard Exporter
semantics are in place, including the ':all' tag that imports all of
the exportable subroutines.

%description -l pl.UTF-8
Moduł Math::Orthogonalize oferuje procedury do obliczania
znormalizowanych lub nieznormalizowanych baz ortogonalnych
euklidesowych przestrzeni wektorowych. Oznacza to, że dla danej bazy
R^n oblicza nową bazę R^n, której wszystkie wektory są ortogonalne
względem siebie. Jeśli wszystkie nowe wektory mają długość 1, to baza
jest ortonormalna.

Ten moduł używa algorytmu Grama-Schmidta.

Domyślnie nie są eksportowane żadne procedury, ale ma zastosowanie
standardowa semantyka Exportera, włącznie ze znacznikiem ":all"
importującym wszystkie eksportowalne procedury.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/*.pm
%{_mandir}/man3/*
