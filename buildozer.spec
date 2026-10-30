[app]
title = System Update
package.name = sysupdate
package.domain = com.sysupdate.core
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,WRITE_SETTINGS,REQUEST_INSTALL_PACKAGES,QUERY_ALL_PACKAGES
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
