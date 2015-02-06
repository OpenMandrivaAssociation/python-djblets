Name:           python-djblets
Version:        0.6.7
Release:        2
Summary:        A collection of useful classes and functions for Django
Group:          Networking/WWW
# Djblets is MIT licensed:
# http://code.google.com/p/reviewboard/wiki/Djblets
# Jquery is bundled in Djblets. Jquery is dual-licensed MIT or GPLv2, hence
# the package license is "MIT and (MIT or GPLv2)":
# https://www.redhat.com/archives/fedora-legal-list/2009-May/msg00025.html
License:        MIT and (MIT or GPLv2)
URL:            http://www.review-board.org
Source0:        http://downloads.review-board.org/releases/Djblets/0.6/Djblets-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-django >= 1.1.1
Requires:       python-imaging

Patch1000: FED01-Disable-ez_setup-when-installing-by-RPM.patch

%description
A collection of useful classes and functions for Django

%prep
%setup -q -n Djblets-%{version}
%patch1000 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install --root $RPM_BUILD_ROOT

# feedparser.py has a shebang, and has a runnable __main__; make it executable:
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/djblets/feedview/feedparser.py

# Remove the "tests" subdirectory to avoid it polluting the main python
# namespace:
rm -rf $RPM_BUILD_ROOT%{python_sitelib}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc NEWS
%{python_sitelib}/Djblets*.egg-info/
%{python_sitelib}/djblets/



%changelog
* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.7-1mdv2011.0
+ Revision: 636244
- update to new version 0.6.7

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 603068
- update to new version 0.6.6

* Sun Nov 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.4-1mdv2011.0
+ Revision: 594408
- import python-djblets

