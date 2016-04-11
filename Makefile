TARGET = /usr/bin/gpm
PACKAGE_PATH /usr/lib/pathon2.7/site-package

.PHYON
install:
    cp -r bpm $(PACKAGE_PATH)
    ln -s $(PACKAGE_PATH)/gpm/gom.py $(TARGET)

.PHYON
test:
    export PYTHONPATH=$PYTHONPATH:./test:.
    python test/test.py
