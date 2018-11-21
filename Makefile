VERSION := $(shell sed -nr 's/Version:\s*(([0-9]+\.?)+).*$$/\1/p' preupgrade-assistant-al1toal2.spec)
NAME := preupgrade-assistant-al1toal2-${VERSION}
DISTTAG := .amzn1

sources:
	mkdir -p ${NAME}
	cp -r preupgrade-assistant-al1toal2.spec AL1_AL2 LICENSE ${NAME}
	tar -cvzf ${NAME}.tar.gz ${NAME}
	rm -rf ${NAME}
clean:
	rm -rf ${NAME}.tar.gz
	rm -rf ${NAME}-*.src.rpm
srpm: sources
	rpmbuild -bs --define "dist ${DISTTAG}" --define "_topdir ${shell pwd}" --define "_sourcedir %{_topdir}" --define "_srcrpmdir %{_topdir}" preupgrade-assistant-al1toal2.spec
.PHONY: sources clean srpm
