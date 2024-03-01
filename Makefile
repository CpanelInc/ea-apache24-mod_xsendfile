OBS_PROJECT := EA4-experimental
OBS_PACKAGE := ea-apache24-mod_xsendfile
DISABLE_BUILD = repository=CentOS_6.5_standard repository=CentOS_9
include $(EATOOLS_BUILD_DIR)obs.mk
