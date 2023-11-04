[app]

# (str) Title of your application
title = YourAppTitle

# (str) Package name
package.name = yourappname

# (str) Package domain (reverse DNS style)
package.domain = com.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) List of source files to include
source.include_patterns = assets/*,images/*,path_to_additional_files/*

# (list) List of source files to exclude
source.exclude_patterns = 

# (list) List of directories to include (space separated)
source.include_dirs = 

# (list) List of directories to exclude (space separated)
source.exclude_dirs = 

# (list) List of framework arguments
# - sdl2 - Include SDL2 with Pygame
# - glew - Include GLEW with Pygame
# - kivy - Include Kivy with GStreamer
# - audiostream - Include audiostream
# - android - Include Android module
# For example, if you need to use Audiostream (audio streaming), add 'audiostream' here.
requirements = python3==3.11.2,kivy==2.2.1,kivymd==1.1.1

# (str) Application version
version = 1.0

# (list) Application permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to a custom distribution tool (works with `target` set to `custom`)
# android.custom_distribution = mydist

# (str) Title of the application
# (str) URL of the application
# (str) Application author's email
# (str) Application author's website
# (str) A packaging version
# (str) Application description
# (str) Application author's name
# (str) Application author's company
# (str) Configuration path
# (str) Configuration encoding
# (list) List of service to declare
# (str) com_release (will be used by "buildozer android release", for the version name)
# (str) Service name
# (str) New service
# (str) New service description
# (list) List of domain
# (list) Domain email
# (str) Debug domain
# (str) release domain
# (str) Description of the license
# (list) Application manifest for compile platform
# (list) Boot permission for compile platform
# (list) Content provider for compile platform
# (list) Service for compile platform
# (str) Add activity for compile platform
# (str) add meta-data for compile platform
# (str) Add uses-library for compile platform
# (str) Add additional activity intent filters for compile platform
# (str) Application class for compile platform
# (str) AAPT command (aapt)
# (str) DX command (dx)
# (list) android ant commands (release)
# (list) android ant commands (debug)
# (list) Logcat filters to use when running the logcat command
# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
# (list) List of requirements, like sdk, ndk, python-for-android
# (str) Android project location
# (list) Android permissions
# (str) Android presplash
# (str) Android opengles version
# (list) Android build options
# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# (str) Android NDK version to use
# (str) Android SDK version to use
# (str) The branch of python-for-android to use (defaults to master)
# (str) The build tool to use when compiling the Android app
# (int) port number to use for the Rsync copy process (the rsync module is always use)
# (int) Android logcat filters
# (list) Whitelist packages
# (list) Application intent to declare
# (list) Android services to declare
# (list) Libraries to compile (comma separated, use the recipe if it exists for it)
# (list) Application meta-data to declare
# (list) Activity intent filters, list of [filter, data, mime type, order]
# (list) Copy data to the private data directory
# (str) XML to copy to the Android data directory
# (str) Android additionnal libraries path (comma separated)
title = My App
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.include_patterns = assets/*,images/*
source.exclude_patterns = license,images/*/*.xcf
source.exclude_dirs = tests, bin
build_dir = build
bin_dir = bin
libs_dir = libs
p4a.source_dir = /home/test/source
p4a.local_recipes = /home/user/recipes
p4a.local_src = /home/user/src
p4a.arch = armeabi-v7a
p4a.ndk_dir = /home/user/ndk
p4a.sdk_dir = /home/user/android-sdk
p4a.ndk_version = r19c
p4a.sdk_version = 24
p4a.private_storage = True
android.permissions = INTERNET
android.api = 27
android.minapi = 21
android.sdk = 27
android.ndk = 19c
android.minndk = 19
android.icon = /home/user/icon.png
android.presplash = /home/user/presplash.png
android.presplash_color = #FFFFFF
android.app_spec = myapp.spec
android.requirements = python3,kivy
default_cx_freeze_profile = 1

# (int) Gradle plugin to use for the build (should be 7.0.0)
gradle = 7.0.0

# (str) Gradle dependancies to add
gradle_dependencies = 'com.android.support:appcompat-v7:28.0.0'

# (list) Application meta-data
#android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY

# (list) Gradle
