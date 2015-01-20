# this assumes you're in a ploneintranet.suite buildout
GENERATED=../ploneintranet.theme/src/ploneintranet/theme/static/generated
TARGET=src/plonesocial/core/browser/

default: sync

sync:
	rsync -av --exclude colours.css $(GENERATED)/style/ $(TARGET)/stylesheets/
	cat $(GENERATED)/bundles/ploneintranet.min.js > $(TARGET)/javascripts/ploneintranet.min.js

