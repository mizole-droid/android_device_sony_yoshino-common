LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
CUSTOMIZATION_MODEM_SYMLINKS := $(TARGET_OUT)/etc/customization/modem
$(CUSTOMIZATION_MODEM_SYMLINKS): $(LOCAL_INSTALLED_MODULE)
	@echo "Create customization modem links: $@"
	@mkdir -p $@
	$(hide) ln -sf amss_fs_empty.mbn $@/reset_modemst1
	$(hide) ln -sf amss_fs_empty.mbn $@/reset_modemst2
ifeq ($(TARGET_DEVICE),lilac)
	$(hide) ln -sf amss_fsg_lilac_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),lilac_dcm)
	$(hide) ln -sf amss_fsg_lilac_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),poplar)
	$(hide) ln -sf amss_fsg_poplar_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),poplar_canada)
	$(hide) ln -sf amss_fsg_poplar_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),poplar_dsds)
	$(hide) ln -sf amss_fsg_poplar_dsds_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),poplar_kddi)
	$(hide) ln -sf amss_fsg_poplar_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),maple)
	$(hide) ln -sf amss_fsg_maple_tar.mbn $@/default
endif
ifeq ($(TARGET_DEVICE),maple_dsds)
	$(hide) ln -sf amss_fsg_maple_dsds_tar.mbn $@/default
endif

ALL_DEFAULT_INSTALLED_MODULES += \
	$(CUSTOMIZATION_MODEM_SYMLINKS)
