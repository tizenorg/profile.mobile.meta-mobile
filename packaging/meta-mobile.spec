Summary:	Tizen Mobile Package Groups and Image Configurations
Name:		meta-mobile
Version:	003
Release:	1
License:	GPL-2.0
Group:		System/Base
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2

%description
Tizen Mobile Package Groups and Image Configurations

%prep
%setup -q

%build
make 

%install
%make_install


%files
%{_datadir}/package-groups/mobile/*.yaml
%{_datadir}/image-configurations/mobile/*.yaml
%{_datadir}/image-configurations/mobile/configs/*.yaml
%{_datadir}/image-configurations/mobile/scripts
%{_datadir}/image-configurations/mobile/partitions
