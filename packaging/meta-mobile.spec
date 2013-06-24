Summary:	Tizen Mobile Package Groups and Image Configurations
Name:		meta-mobile
Version:	002
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
%attr(644,-,-) %{_datadir}/package-groups/mobile/*.yaml
/usr/share/image-configurations/mobile/*.yaml
/usr/share/image-configurations/mobile/configs/*.yaml
/usr/share/image-configurations/mobile/scripts
/usr/share/image-configurations/mobile/partitions
