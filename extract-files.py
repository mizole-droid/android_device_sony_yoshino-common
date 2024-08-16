#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/sony/yoshino-common',
    'hardware/qcom-caf/msm8998',
    'hardware/qcom-caf/wlan',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
    ): lib_fixup_vendor_suffix,
    (
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/ffu': blob_fixup()
        .binary_regex_replace(b'/lib/firmware/ufs', b'/etc/firmware/ufs'),
    (
        'product/etc/permissions/vendor.qti.hardware.data.connection-V1.0-java.xml',
        'product/etc/permissions/vendor.qti.hardware.data.connection-V1.1-java.xml',
    ): blob_fixup()
        .binary_regex_replace(b'version="2.0"', b'version="1.0"'),
    'vendor/etc/init/taimport_vendor.rc': blob_fixup()
        .binary_regex_replace(b'mkdir /persist/wlan 0755 root shell', b'mkdir /persist/wlan 0755 root shell\nrestorecon /persist/wlan'),
    'system_ext/lib64/lib-imsvideocodec.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    (
        'system/lib/libjni_imageutil.so',
        'system/lib/libjni_snapcammosaic.so',
        'system/lib/libjni_snapcamtinyplanet.so',
        'system/lib/libseemore.so',
        'system/lib64/libseemore.so',
        'vendor/lib/libsomc_alfortlp.so',
        'vendor/lib/libsomc_alfortlpserv.so',
        'vendor/lib/libsomc_alfortrsc.so',
        'vendor/lib/libsomc_bordeauxrsc.so',
        'vendor/lib/libsomc_buttercakersc.so',
        'vendor/lib/libsomc_canelersc.so',
        'vendor/lib/libsomc_cheesesconersc.so',
        'vendor/lib/libsomc_dars.so',
        'vendor/lib/libsomc_darsrsc.so',
        'vendor/lib/libsomc_marblersc.so',
        'vendor/lib/libsomc_melonpanrsc.so',
        'vendor/lib/libsomc_mugichocorsc.so',
        'vendor/lib/libsomc_pretzchocorsc.so',
        'vendor/lib/libsomc_raisinrsc.so',
        'vendor/lib/libsomc_shortcakersc.so',
        'vendor/lib/libsomc_spicarsc.so',
        'vendor/lib/libsomc_sumomolpserv.so',
        'vendor/lib/libsomc_sumomorsc.so',
        'vendor/lib/libsomc_topporsc.so',
        'vendor/lib/libsomc_yummyrsc.so',
        'vendor/lib/libsony_fooddetect.so',
        'vendor/lib/libsony_naruto.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    (
        'system/bin/sony-modem-switcher',
        'system/lib/com.qualcomm.qti.ant@1.0.so',
        'system/lib/com.qualcomm.qti.bluetooth_audio@1.0.so',
        'system/lib/libMiscTaWrapper.so',
        'system/lib/vendor.qti.hardware.qteeconnector@1.0.so',
        'system/lib/vendor.qti.hardware.tui_comm@1.0.so',
        'system/lib/vendor.qti.hardware.vpp@1.1.so',
        'system/lib/vendor.semc.hardware.light@1.0.so',
        'system/lib/vendor.semc.system.idd@1.0.so',
        'system/lib/vendor.somc.hardware.camera.cacao@1.0.so',
        'system/lib/vendor.somc.hardware.camera.cacao@2.0.so',
        'system/lib/vendor.somc.hardware.camera.cacao@3.0.so',
        'system/lib/vendor.somc.hardware.camera.cacao@3.1.so',
        'system/lib/vendor.somc.hardware.camera.device@1.0.so',
        'system/lib/vendor.somc.hardware.camera.provider@1.0.so',
        'system/lib64/com.qualcomm.qti.ant@1.0.so',
        'system/lib64/com.qualcomm.qti.bluetooth_audio@1.0.so',
        'system/lib64/libMiscTaWrapper.so',
        'system/lib64/vendor.display.color@1.0.so',
        'system/lib64/vendor.display.color@1.1.so',
        'system/lib64/vendor.display.color@1.2.so',
        'system/lib64/vendor.display.postproc@1.0.so',
        'system/lib64/vendor.qti.esepowermanager@1.0.so',
        'system/lib64/vendor.qti.hardware.qdutils_disp@1.0.so',
        'system/lib64/vendor.qti.hardware.qteeconnector@1.0.so',
        'system/lib64/vendor.qti.hardware.tui_comm@1.0.so',
        'system/lib64/vendor.qti.hardware.vpp@1.1.so',
        'system/lib64/vendor.semc.hardware.light@1.0.so',
        'system/lib64/vendor.semc.system.idd@1.0.so',
        'system/lib64/vendor.somc.hardware.security.secd@1.0.so',
    ): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/etc/init/android.hardware.drm@1.1-service.widevine.rc': blob_fixup()
        .regex_replace('writepid /dev/cpuset/foreground/tasks', 'task_profiles ProcessCapacityHigh'),
    (
        'vendor/etc/init/init.illumination_service.rc',
        'vendor/etc/init/init.touchbacklightd.rc',
    ): blob_fixup()
        .regex_replace('writepid /dev/cpuset/system-background/tasks', 'task_profiles ServiceCapacityLow'),
    'vendor/etc/init/vendor.somc.hardware.camera.provider@1.0-service.rc': blob_fixup()
        .regex_replace('writepid /dev/cpuset/camera-daemon/tasks', 'task_profiles CameraServiceCapacity MaxPerformance'),
}  # fmt: skip

module = ExtractUtilsModule(
    'yoshino-common',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
