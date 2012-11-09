Summary:	Tizen Package Groups for Base OS
Name:		patterns-base
Version:	001
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2




%description
Tizen Package Groups for Base OS

%prep
%setup -q

%build
make 

%install
%make_install


%files
/usr/share/package-groups/patterns/*.yaml
