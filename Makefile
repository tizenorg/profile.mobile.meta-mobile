# ex: set tabstop=4 noexpandtab: 
VERSION = $(shell cat VERSION)
NAME=meta-mobile
TAGVER = $(shell cat VERSION | sed -e "s/\([0-9\.]*\).*/\1/")
DESTDIR=
ARCH=i586

ifeq ($(VERSION), $(TAGVER))
        TAG = $(TAGVER)
else
        TAG = "HEAD"
endif

all:

install:
	install -d ${DESTDIR}/usr/share/image-configurations/mobile/configs
	install -d ${DESTDIR}/usr/share/image-configurations/mobile/custom
	install -d ${DESTDIR}/usr/share/image-configurations/mobile/scripts
	install -d ${DESTDIR}/usr/share/image-configurations/mobile/partitions
	install -d ${DESTDIR}/usr/share/package-groups/mobile
	install -m 644 mobile.yaml ${DESTDIR}/usr/share/image-configurations/mobile
	install -m 644 mobile-repos.yaml ${DESTDIR}/usr/share/image-configurations/mobile
	install -m 644 ks/*.yaml ${DESTDIR}/usr/share/image-configurations/mobile/configs
	install -D partitions/* ${DESTDIR}/usr/share/image-configurations/mobile/partitions
	install -D scripts/* ${DESTDIR}/usr/share/image-configurations/mobile/scripts
	install -m 644 patterns/*.yaml ${DESTDIR}/usr/share/package-groups/mobile

test:
	merge-patterns -o output/ -p patterns -s
	kickstarter -c mobile.yaml -e ks -r mobile-repos.yaml

tag:
	git tag -a $(VERSION) -m "$(VERSION)"
	git push --tags

changelog:
	python ./scripts/gitlog2changelog.py


dist-bz2:
	git archive --format=tar --prefix=$(NAME)-$(VERSION)/ $(TAG) | \
		bzip2  > $(NAME)-$(VERSION).tar.bz2

dist-gz:
	git archive --format=tar --prefix=$(NAME)-$(VERSION)/ $(TAG) | \
		gzip  > $(NAME)-$(VERSION).tar.gz

dist: dist-bz2

clean:
	rm -rf patterns.xml INDEX.xml group.xml *.xml
