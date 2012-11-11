Summary:	Tizen Package Groups and Images Configurations
Name:		meta-base
Version:	001
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2

%description
Tizen Package Groups and Image Configurations for Base OS

%prep
%setup -q

%build
make 

%install
%make_install


%files
/usr/share/package-groups/base/*.yaml
/usr/share/image-configurations/base/*.yaml
/usr/share/image-configurations/base/configs/*.yaml
/usr/share/image-configurations/base/custom
