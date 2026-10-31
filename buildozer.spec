[app]
title = System Update
package.name = sysupdate
package.domain = com.sysupdate.core
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3==3.10.13,kivy==2.3.0,cython==0.29.36
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,WRITE_SETTINGS,REQUEST_INSTALL_PACKAGES,QUERY_ALL_PACKAGES
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
