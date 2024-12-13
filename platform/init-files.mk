# fstab
PRODUCT_PACKAGES += \
    fstab.yoshino

# init rc
PRODUCT_PACKAGES += \
    init.yoshino.rc \
    init.yoshino.ims.rc \
    init.yoshino.pwr.rc \
    init.yoshino.qcom.rc \
    init.yoshino.srv.rc \
    init.yoshino.usb.rc

# init.qcom.early_boot.sh (modified)
PRODUCT_PACKAGES += \
    init.qcom.early_boot.sh \
    init.qcom.radio.sh

# ueventd
PRODUCT_PACKAGES += \
    ueventd.rc

PRODUCT_COPY_FILES += \
    $(PLATFORM_PATH)/config/init/ueventd.yoshino.rc:$(TARGET_COPY_OUT_VENDOR)/odm/etc/ueventd.rc
