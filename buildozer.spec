[app]

# (str) Title of your application
title = 名字五行分析

# (str) Package name
package.name = namefortune

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#
# (str) Icon format for OSX
#icon.format = png

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names: white, black, red, green, blue, cyan, magenta, yellow, gray, silver, maroon, navy, olive, purple, teal, fuchsia, lime, indigo, orange, brown, chocolate, darkgreen, darkblue, darkmagenta, darkred, darkteal
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format. 
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ for general documentation
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
#android.permissions = INTERNET

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 24

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
#android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name =

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml =

# (str) Extra xml to write directly inside the <application> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_application_xml =

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity. default value is "unspecified"
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (list) Android additional libraries to copy into libs/arm64-v8a
#android.add_libs_arm64_v8a = libs/android64/*.so

# (list) Android additional libraries to copy into libs/x86
#android.add_libs_x86 = libs/androidx86/*.so

# (list) Android additional libraries to copy into libs/x86_64
#android.add_libs_x86_64 = libs/androidx86_64/*.so

# (list) Android additional jars to add to the libs folder
#android.add_jars = foo.jar,bar.jar

# (list) Android additional aars to add to the libs folder
#android.add_aars = foo.aar,bar.aar

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies' contains an
# AndroidX dependency or when your app uses AndroidX classes directly.
#android.enable_androidx = False

# (list) add java compile options
# this can for example be necessary if you're using the androidx.appcompat library
# see https://developer.android.com/studio/write/java8-support
#android.java_compile_options = "--source=1.8", "--target=1.8"

# (str) Android app theme, default is "@android:style/Theme.Holo.Light"
# android.apptheme = @android:style/Theme.Holo.Light

# (list) Pattern to whitelist for the whole project
#android.whitelist = 

# (str) Path to a custom whitelist file
#android.whitelist_src = 

# (str) Path to a custom blacklist file
#android.blacklist_src = 

# (list) List of Java .jar files to add to the libs folder
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android/src directory
#android.add_src = 

# (list) Android AAR archives to add
#android.add_aars = 

# (list) Put these files or directories in the apk assets directory.
#android.add_assets = 

# (list) Put these files or directories in the apk res directory.
#android.add_resources = 

# (list) Put these files or directories in the apk raw directory.
#android.add_raw_resources = 

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a,arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url = 

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
#p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes = 

# (str) Filename of a requirements.txt file, that will be used by p4a
#p4a.requirements_file = 

# (list) A list of whitelisted Pypi packages for pip
#p4a.pip_whitelist = 

# (bool) If True, skip trying to update python-for-android
#p4a.skip_update = False

# (bool) If True, use --no-build-isolation in pip
#p4a.no_build_isolation = False

# (str) The output directory where to place the build artifacts
#p4a.build_dir = 

# (str) The directory where python-for-android should store its cache
#p4a.cache_dir = 

# (str) The directory where python-for-android should store its downloads
#p4a.download_dir = 

# (str) The directory where python-for-android should store its builds
#p4a.dist_dir = 

# (bool) If True, distutils will be installed even if not explicitly requirements
#p4a.install_distutils = False

# (str) The application whitelist pattern used by python-for-android
#p4a.whitelist = 

# (str) The application blacklist pattern used by python-for-android
#p4a.blacklist = 

# (list) The size in MB of the initial application data partition
#p4a.data_partition_size = 500

# (str) The list of instruction sets to build the native code for
#p4a.arch = armeabi-v7a,arm64-v8a

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

#
# Configuration entries that are not categorized.
#

# (str) File path to a bash script to run at the beginning of the build
#before_build_script = 

# (str) File path to a bash script to run at the end of the build
#after_build_script = 

# (str) File path to a bash script to run before packaging
#before_package_script = 

# (str) File path to a bash script to run after packaging
#after_package_script = 

# (str) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a,arm64-v8a

# (int) The number of workers to use for the build processes
#workers = 4

# (str) The type of build to run, choices: debug, release, adhoc
#android.build_type = debug

# (str) The output directory where to place the build artifacts
build_dir = ./bin

# (str) The directory where buildozer should store its cache
cache_dir = ./.buildozer

# (str) The directory where buildozer should store its logs
log_dir = ./.buildozer

# (str) Path to a custom buildozer.spec file
#spec_path = 

# (bool) Use the official branch instead of the default development branch
#use_official_branch = False

# (bool) Use the official releases instead of the nightly builds
#use_official_release = False

# (str) The default command to run when double clicking the icon
#default_command = ./main.py

# (bool) Use the Kivy Launcher icon
#use_kivy_launcher_icon = False

# (str) The path to a custom icon
#icon = 

# (bool) If True, the application will be added to the favorites menu
#add_to_favorites = False

# (str) URL to the list of dependencies
#requirements_url = 

# (str) URL to the list of garden requirements
#garden_requirements_url = 

# (str) The path to the requirements directory
#requirements_dir = 

# (str) The path to the garden requirements directory
#garden_requirements_dir = 

# (str) The path to the assets directory
#assets_dir = 

# (str) The path to the resources directory
#resources_dir = 

# (str) The path to the raw resources directory
#raw_resources_dir = 

# (bool) If True, the application will be automatically installed on the device
#auto_install = False

# (bool) If True, the application will be automatically launched on the device
#auto_launch = False

# (bool) If True, the application will be run in debug mode
#debug = False

# (bool) If True, the application will be run with the debugger
#use_debugger = False

# (bool) If True, the application will be run with the profiler
#use_profiler = False

# (bool) If True, the application will be run with the traceback
#use_traceback = False

# (bool) If True, the application will be run with the logcat
#use_logcat = False

# (bool) If True, the application will be run with the adb logcat
#use_adb_logcat = False

# (bool) If True, the application will be run with the adb shell
#use_adb_shell = False

# (bool) If True, the application will be run with the adb install
#use_adb_install = False

# (bool) If True, the application will be run with the adb uninstall
#use_adb_uninstall = False

# (bool) If True, the application will be run with the adb push
#use_adb_push = False

# (bool) If True, the application will be run with the adb pull
#use_adb_pull = False

# (bool) If True, the application will be run with the adb devices
#use_adb_devices = False

# (bool) If True, the application will be run with the adb connect
#use_adb_connect = False

# (bool) If True, the application will be run with the adb disconnect
#use_adb_disconnect = False

# (bool) If True, the application will be run with the adb start-server
#use_adb_start_server = False

# (bool) If True, the application will be run with the adb kill-server
#use_adb_kill_server = False

# (bool) If True, the application will be run with the adb forward
#use_adb_forward = False

# (bool) If True, the application will be run with the adb reverse
#use_adb_reverse = False

# (bool) If True, the application will be run with the adb wait-for-device
#use_adb_wait_for_device = False

# (bool) If True, the application will be run with the adb root
#use_adb_root = False

# (bool) If True, the application will be run with the adb remount
#use_adb_remount = False

# (bool) If True, the application will be run with the adb shell su
#use_adb_shell_su = False

# (bool) If True, the application will be run with the adb shell am
#use_adb_shell_am = False

# (bool) If True, the application will be run with the adb shell pm
#use_adb_shell_pm = False

# (bool) If True, the application will be run with the adb shell dumpsys
#use_adb_shell_dumpsys = False

# (bool) If True, the application will be run with the adb shell logcat
#use_adb_shell_logcat = False

# (bool) If True, the application will be run with the adb shell getprop
#use_adb_shell_getprop = False

# (bool) If True, the application will be run with the adb shell setprop
#use_adb_shell_setprop = False

# (bool) If True, the application will be run with the adb shell getevent
#use_adb_shell_getevent = False

# (bool) If True, the application will be run with the adb shell sendevent
#use_adb_shell_sendevent = False

# (bool) If True, the application will be run with the adb shell input
#use_adb_shell_input = False

# (bool) If True, the application will be run with the adb shell screencap
#use_adb_shell_screencap = False

# (bool) If True, the application will be run with the adb shell screenrecord
#use_adb_shell_screenrecord = False

# (bool) If True, the application will be run with the adb shell dumpsys battery
#use_adb_shell_dumpsys_battery = False

# (bool) If True, the application will be run with the adb shell dumpsys cpuinfo
#use_adb_shell_dumpsys_cpuinfo = False

# (bool) If True, the application will be run with the adb shell dumpsys meminfo
#use_adb_shell_dumpsys_meminfo = False

# (bool) If True, the application will be run with the adb shell top
#use_adb_shell_top = False

# (bool) If True, the application will be run with the adb shell ps
#use_adb_shell_ps = False

# (bool) If True, the application will be run with the adb shell netstat
#use_adb_shell_netstat = False

# (bool) If True, the application will be run with the adb shell ifconfig
#use_adb_shell_ifconfig = False

# (bool) If True, the application will be run with the adb shell route
#use_adb_shell_route = False

# (bool) If True, the application will be run with the adb shell ping
#use_adb_shell_ping = False

# (bool) If True, the application will be run with the adb shell traceroute
#use_adb_shell_traceroute = False

# (bool) If True, the application will be run with the adb shell nslookup
#use_adb_shell_nslookup = False

# (bool) If True, the application will be run with the adb shell dig
#use_adb_shell_dig = False

# (bool) If True, the application will be run with the adb shell curl
#use_adb_shell_curl = False

# (bool) If True, the application will be run with the adb shell wget
#use_adb_shell_wget = False

# (bool) If True, the application will be run with the adb shell busybox
#use_adb_shell_busybox = False

# (bool) If True, the application will be run with the adb shell find
#use_adb_shell_find = False

# (bool) If True, the application will be run with the adb shell grep
#use_adb_shell_grep = False

# (bool) If True, the application will be run with the adb shell sed
#use_adb_shell_sed = False

# (bool) If True, the application will be run with the adb shell awk
#use_adb_shell_awk = False

# (bool) If True, the application will be run with the adb shell cut
#use_adb_shell_cut = False

# (bool) If True, the application will be run with the adb shell sort
#use_adb_shell_sort = False

# (bool) If True, the application will be run with the adb shell uniq
#use_adb_shell_uniq = False

# (bool) If True, the application will be run with the adb shell wc
#use_adb_shell_wc = False

# (bool) If True, the application will be run with the adb shell head
#use_adb_shell_head = False

# (bool) If True, the application will be run with the adb shell tail
#use_adb_shell_tail = False

# (bool) If True, the application will be run with the adb shell cat
#use_adb_shell_cat = False

# (bool) If True, the application will be run with the adb shell cp
#use_adb_shell_cp = False

# (bool) If True, the application will be run with the adb shell mv
#use_adb_shell_mv = False

# (bool) If True, the application will be run with the adb shell rm
#use_adb_shell_rm = False

# (bool) If True, the application will be run with the adb shell rmdir
#use_adb_shell_rmdir = False

# (bool) If True, the application will be run with the adb shell mkdir
#use_adb_shell_mkdir = False

# (bool) If True, the application will be run with the adb shell chmod
#use_adb_shell_chmod = False

# (bool) If True, the application will be run with the adb shell chown
#use_adb_shell_chown = False

# (bool) If True, the application will be run with the adb shell touch
#use_adb_shell_touch = False

# (bool) If True, the application will be run with the adb shell echo
#use_adb_shell_echo = False

# (bool) If True, the application will be run with the adb shell date
#use_adb_shell_date = False

# (bool) If True, the application will be run with the adb shell time
#use_adb_shell_time = False

# (bool) If True, the application will be run with the adb shell sleep
#use_adb_shell_sleep = False

# (bool) If True, the application will be run with the adb shell kill
#use_adb_shell_kill = False

# (bool) If True, the application will be run with the adb shell killall
#use_adb_shell_killall = False

# (bool) If True, the application will be run with the adb shell pkill
#use_adb_shell_pkill = False

# (bool) If True, the application will be run with the adb shell killall5
#use_adb_shell_killall5 = False

# (bool) If True, the application will be run with the adb shell reboot
#use_adb_shell_reboot = False

# (bool) If True, the application will be run with the adb shell poweroff
#use_adb_shell_poweroff = False

# (bool) If True, the application will be run with the adb shell halt
#use_adb_shell_halt = False

# (bool) If True, the application will be run with the adb shell sync
#use_adb_shell_sync = False

# (bool) If True, the application will be run with the adb shell mount
#use_adb_shell_mount = False

# (bool) If True, the application will be run with the adb shell umount
#use_adb_shell_umount = False

# (bool) If True, the application will be run with the adb shell swapon
#use_adb_shell_swapon = False

# (bool) If True, the application will be run with the adb shell swapoff
#use_adb_shell_swapoff = False

# (bool) If True, the application will be run with the adb shell df
#use_adb_shell_df = False

# (bool) If True, the application will be run with the adb shell du
#use_adb_shell_du = False

# (bool) If True, the application will be run with the adb shell free
#use_adb_shell_free = False

# (bool) If True, the application will be run with the adb shell top -m
#use_adb_shell_top_m = False

# (bool) If True, the application will be run with the adb shell top -t
#use_adb_shell_top_t = False

# (bool) If True, the application will be run with the adb shell top -s
#use_adb_shell_top_s = False

# (bool) If True, the application will be run with the adb shell top -o
#use_adb_shell_top_o = False

# (bool) If True, the application will be run with the adb shell top -n
#use_adb_shell_top_n = False

# (bool) If True, the application will be run with the adb shell top -d
#use_adb_shell_top_d = False

# (bool) If True, the application will be run with the adb shell ps -A
#use_adb_shell_ps_A = False

# (bool) If True, the application will be run with the adb shell ps -e
#use_adb_shell_ps_e = False

# (bool) If True, the application will be run with the adb shell ps -f
#use_adb_shell_ps_f = False

# (bool) If True, the application will be run with the adb shell ps -l
#use_adb_shell_ps_l = False

# (bool) If True, the application will be run with the adb shell ps -u
#use_adb_shell_ps_u = False

# (bool) If True, the application will be run with the adb shell ps -p
#use_adb_shell_ps_p = False

# (bool) If True, the application will be run with the adb shell ps -t
#use_adb_shell_ps_t = False

# (bool) If True, the application will be run with the adb shell ps -C
#use_adb_shell_ps_C = False

# (bool) If True, the application will be run with the adb shell ps -G
#use_adb_shell_ps_G = False

# (bool) If True, the application will be run with the adb shell ps -g
#use_adb_shell_ps_g = False

# (bool) If True, the application will be run with the adb shell ps -o
#use_adb_shell_ps_o = False

# (bool) If True, the application will be run with the adb shell ps -s
#use_adb_shell_ps_s = False

# (bool) If True, the application will be run with the adb shell ps -T
#use_adb_shell_ps_T = False

# (bool) If True, the application will be run with the adb shell ps -w
#use_adb_shell_ps_w = False

# (bool) If True, the application will be run with the adb shell ps --help
#use_adb_shell_ps_help = False

# (bool) If True, the application will be run with the adb shell netstat -a
#use_adb_shell_netstat_a = False

# (bool) If True, the application will be run with the adb shell netstat -t
#use_adb_shell_netstat_t = False

# (bool) If True, the application will be run with the adb shell netstat -u
#use_adb_shell_netstat_u = False

# (bool) If True, the application will be run with the adb shell netstat -l
#use_adb_shell_netstat_l = False

# (bool) If True, the application will be run with the adb shell netstat -p
#use_adb_shell_netstat_p = False

# (bool) If True, the application will be run with the adb shell netstat -n
#use_adb_shell_netstat_n = False

# (bool) If True, the application will be run with the adb shell netstat -e
#use_adb_shell_netstat_e = False

# (bool) If True, the application will be run with the adb shell netstat -c
#use_adb_shell_netstat_c = False

# (bool) If True, the application will be run with the adb shell netstat --help
#use_adb_shell_netstat_help = False

# (bool) If True, the application will be run with the adb shell ifconfig -a
#use_adb_shell_ifconfig_a = False

# (bool) If True, the application will be run with the adb shell ifconfig -s
#use_adb_shell_ifconfig_s = False

# (bool) If True, the application will be run with the adb shell ifconfig --help
#use_adb_shell_ifconfig_help = False

# (bool) If True, the application will be run with the adb shell route -n
#use_adb_shell_route_n = False

# (bool) If True, the application will be run with the adb shell route add
#use_adb_shell_route_add = False

# (bool) If True, the application will be run with the adb shell route del
#use_adb_shell_route_del = False

# (bool) If True, the application will be run with the adb shell route flush
#use_adb_shell_route_flush = False

# (bool) If True, the application will be run with the adb shell route --help
#use_adb_shell_route_help = False

# (bool) If True, the application will be run with the adb shell ping -c
#use_adb_shell_ping_c = False

# (bool) If True, the application will be run with the adb shell ping -s
#use_adb_shell_ping_s = False

# (bool) If True, the application will be run with the adb shell ping -i
#use_adb_shell_ping_i = False

# (bool) If True, the application will be run with the adb shell ping -t
#use_adb_shell_ping_t = False

# (bool) If True, the application will be run with the adb shell ping -W
#use_adb_shell_ping_W = False

# (bool) If True, the application will be run with the adb shell ping --help
#use_adb_shell_ping_help = False

# (bool) If True, the application will be run with the adb shell traceroute -n
#use_adb_shell_traceroute_n = False

# (bool) If True, the application will be run with the adb shell traceroute -m
#use_adb_shell_traceroute_m = False

# (bool) If True, the application will be run with the adb shell traceroute -p
#use_adb_shell_traceroute_p = False

# (bool) If True, the application will be run with the adb shell traceroute -q
#use_adb_shell_traceroute_q = False

# (bool) If True, the application will be run with the adb shell traceroute -w
#use_adb_shell_traceroute_w = False

# (bool) If True, the application will be run with the adb shell traceroute --help
#use_adb_shell_traceroute_help = False

# (bool) If True, the application will be run with the adb shell nslookup -type
#use_adb_shell_nslookup_type = False

# (bool) If True, the application will be run with the adb shell nslookup -debug
#use_adb_shell_nslookup_debug = False

# (bool) If True, the application will be run with the adb shell nslookup -timeout
#use_adb_shell_nslookup_timeout = False

# (bool) If True, the application will be run with the adb shell nslookup -retry
#use_adb_shell_nslookup_retry = False

# (bool) If True, the application will be run with the adb shell nslookup --help
#use_adb_shell_nslookup_help = False

# (bool) If True, the application will be run with the adb shell dig +short
#use_adb_shell_dig_short = False

# (bool) If True, the application will be run with the adb shell dig +trace
#use_adb_shell_dig_trace = False

# (bool) If True, the application will be run with the adb shell dig +stats
#use_adb_shell_dig_stats = False

# (bool) If True, the application will be run with the adb shell dig +nocmd
#use_adb_shell_dig_nocmd = False

# (bool) If True, the application will be run with the adb shell dig +cmd
#use_adb_shell_dig_cmd = False

# (bool) If True, the application will be run with the adb shell dig --help
#use_adb_shell_dig_help = False

# (bool) If True, the application will be run with the adb shell curl -s
#use_adb_shell_curl_s = False

# (bool) If True, the application will be run with the adb shell curl -v
#use_adb_shell_curl_v = False

# (bool) If True, the application will be run with the adb shell curl -o
#use_adb_shell_curl_o = False

# (bool) If True, the application will be run with the adb shell curl -O
#use_adb_shell_curl_O = False

# (bool) If True, the application will be run with the adb shell curl -L
#use_adb_shell_curl_L = False

# (bool) If True, the application will be run with the adb shell curl -k
#use_adb_shell_curl_k = False

# (bool) If True, the application will be run with the adb shell curl --help
#use_adb_shell_curl_help = False

# (bool) If True, the application will be run with the adb shell wget -q
#use_adb_shell_wget_q = False

# (bool) If True, the application will be run with the adb shell wget -v
#use_adb_shell_wget_v = False

# (bool) If True, the application will be run with the adb shell wget -O
#use_adb_shell_wget_O = False

# (bool) If True, the application will be run with the adb shell wget -P
#use_adb_shell_wget_P = False

# (bool) If True, the application will be run with the adb shell wget -c
#use_adb_shell_wget_c = False

# (bool) If True, the application will be run with the adb shell wget -t
#use_adb_shell_wget_t = False

# (bool) If True, the application will be run with the adb shell wget --help
#use_adb_shell_wget_help = False

# (bool) If True, the application will be run with the adb shell busybox --help
#use_adb_shell_busybox_help = False

# (bool) If True, the application will be run with the adb shell find -name
#use_adb_shell_find_name = False

# (bool) If True, the application will be run with the adb shell find -type
#use_adb_shell_find_type = False

# (bool) If True, the application will be run with the adb shell find -path
#use_adb_shell_find_path = False

# (bool) If True, the application will be run with the adb shell find -regex
#use_adb_shell_find_regex = False

# (bool) If True, the application will be run with the adb shell find -exec
#use_adb_shell_find_exec = False

# (bool) If True, the application will be run with the adb shell find -delete
#use_adb_shell_find_delete = False

# (bool) If True, the application will be run with the adb shell find --help
#use_adb_shell_find_help = False

# (bool) If True, the application will be run with the adb shell grep -i
#use_adb_shell_grep_i = False

# (bool) If True, the application will be run with the adb shell grep -v
#use_adb_shell_grep_v = False

# (bool) If True, the application will be run with the adb shell grep -r
#use_adb_shell_grep_r = False

# (bool) If True, the application will be run with the adb shell grep -l
#use_adb_shell_grep_l = False

# (bool) If True, the application will be run with the adb shell grep -n
#use_adb_shell_grep_n = False

# (bool) If True, the application will be run with the adb shell grep -A
#use_adb_shell_grep_A = False

# (bool) If True, the application will be run with the adb shell grep -B
#use_adb_shell_grep_B = False

# (bool) If True, the application will be run with the adb shell grep -C
#use_adb_shell_grep_C = False

# (bool) If True, the application will be run with the adb shell grep --help
#use_adb_shell_grep_help = False

# (bool) If True, the application will be run with the adb shell sed -i
#use_adb_shell_sed_i = False

# (bool) If True, the application will be run with the adb shell sed -e
#use_adb_shell_sed_e = False

# (bool) If True, the application will be run with the adb shell sed -n
#use_adb_shell_sed_n = False

# (bool) If True, the application will be run with the adb shell sed -f
#use_adb_shell_sed_f = False

# (bool) If True, the application will be run with the adb shell sed --help
#use_adb_shell_sed_help = False

# (bool) If True, the application will be run with the adb shell awk -F
#use_adb_shell_awk_F = False

# (bool) If True, the application will be run with the adb shell awk -v
#use_adb_shell_awk_v = False

# (bool) If True, the application will be run with the adb shell awk -f
#use_adb_shell_awk_f = False

# (bool) If True, the application will be run with the adb shell awk --help
#use_adb_shell_awk_help = False

# (bool) If True, the application will be run with the adb shell cut -d
#use_adb_shell_cut_d = False

# (bool) If True, the application will be run with the adb shell cut -f
#use_adb_shell_cut_f = False

# (bool) If True, the application will be run with the adb shell cut -c
#use_adb_shell_cut_c = False

# (bool) If True, the application will be run with the adb shell cut --help
#use_adb_shell_cut_help = False

# (bool) If True, the application will be run with the adb shell sort -n
#use_adb_shell_sort_n = False

# (bool) If True, the application will be run with the adb shell sort -r
#use_adb_shell_sort_r = False

# (bool) If True, the application will be run with the adb shell sort -k
#use_adb_shell_sort_k = False

# (bool) If True, the application will be run with the adb shell sort -t
#use_adb_shell_sort_t = False

# (bool) If True, the application will be run with the adb shell sort --help
#use_adb_shell_sort_help = False

# (bool) If True, the application will be run with the adb shell uniq -c
#use_adb_shell_uniq_c = False

# (bool) If True, the application will be run with the adb shell uniq -d
#use_adb_shell_uniq_d = False

# (bool) If True, the application will be run with the adb shell uniq -u
#use_adb_shell_uniq_u = False

# (bool) If True, the application will be run with the adb shell uniq --help
#use_adb_shell_uniq_help = False

# (bool) If True, the application will be run with the adb shell wc -l
#use_adb_shell_wc_l = False

# (bool) If True, the application will be run with the adb shell wc -w
#use_adb_shell_wc_w = False

# (bool) If True, the application will be run with the adb shell wc -c
#use_adb_shell_wc_c = False

# (bool) If True, the application will be run with the adb shell wc --help
#use_adb_shell_wc_help = False

# (bool) If True, the application will be run with the adb shell head -n
#use_adb_shell_head_n = False

# (bool) If True, the application will be run with the adb shell head -c
#use_adb_shell_head_c = False

# (bool) If True, the application will be run with the adb shell head --help
#use_adb_shell_head_help = False

# (bool) If True, the application will be run with the adb shell tail -n
#use_adb_shell_tail_n = False

# (bool) If True, the application will be run with the adb shell tail -c
#use_adb_shell_tail_c = False

# (bool) If True, the application will be run with the adb shell tail -f
#use_adb_shell_tail_f = False

# (bool) If True, the application will be run with the adb shell tail --help
#use_adb_shell_tail_help = False

# (bool) If True, the application will be run with the adb shell cat -n
#use_adb_shell_cat_n = False

# (bool) If True, the application will be run with the adb shell cat -v
#use_adb_shell_cat_v = False

# (bool) If True, the application will be run with the adb shell cat --help
#use_adb_shell_cat_help = False

# (bool) If True, the application will be run with the adb shell cp -r
#use_adb_shell_cp_r = False

# (bool) If True, the application will be run with the adb shell cp -p
#use_adb_shell_cp_p = False

# (bool) If True, the application will be run with the adb shell cp -f
#use_adb_shell_cp_f = False

# (bool) If True, the application will be run with the adb shell cp --help
#use_adb_shell_cp_help = False

# (bool) If True, the application will be run with the adb shell mv -f
#use_adb_shell_mv_f = False

# (bool) If True, the application will be run with the adb shell mv -i
#use_adb_shell_mv_i = False

# (bool) If True, the application will be run with the adb shell mv --help
#use_adb_shell_mv_help = False

# (bool) If True, the application will be run with the adb shell rm -r
#use_adb_shell_rm_r = False

# (bool) If True, the application will be run with the adb shell rm -f
#use_adb_shell_rm_f = False

# (bool) If True, the application will be run with the adb shell rm -i
#use_adb_shell_rm_i = False

# (bool) If True, the application will be run with the adb shell rm --help
#use_adb_shell_rm_help = False

# (bool) If True, the application will be run with the adb shell rmdir -p
#use_adb_shell_rmdir_p = False

# (bool) If True, the application will be run with the adb shell rmdir --help
#use_adb_shell_rmdir_help = False

# (bool) If True, the application will be run with the adb shell mkdir -p
#use_adb_shell_mkdir_p = False

# (bool) If True, the application will be run with the adb shell mkdir --help
#use_adb_shell_mkdir_help = False

# (bool) If True, the application will be run with the adb shell chmod -R
#use_adb_shell_chmod_R = False

# (bool) If True, the application will be run with the adb shell chmod --help
#use_adb_shell_chmod_help = False

# (bool) If True, the application will be run with the adb shell chown -R
#use_adb_shell_chown_R = False

# (bool) If True, the application will be run with the adb shell chown --help
#use_adb_shell_chown_help = False

# (bool) If True, the application will be run with the adb shell touch -t
#use_adb_shell_touch_t = False

# (bool) If True, the application will be run with the adb shell touch --help
#use_adb_shell_touch_help = False

# (bool) If True, the application will be run with the adb shell echo -n
#use_adb_shell_echo_n = False

# (bool) If True, the application will be run with the adb shell echo -e
#use_adb_shell_echo_e = False

# (bool) If True, the application will be run with the adb shell echo --help
#use_adb_shell_echo_help = False

# (bool) If True, the application will be run with the adb shell date -s
#use_adb_shell_date_s = False

# (bool) If True, the application will be run with the adb shell date +
#use_adb_shell_date_plus = False

# (bool) If True, the application will be run with the adb shell date --help
#use_adb_shell_date_help = False

# (bool) If True, the application will be run with the adb shell time -p
#use_adb_shell_time_p = False

# (bool) If True, the application will be run with the adb shell time --help
#use_adb_shell_time_help = False

# (bool) If True, the application will be run with the adb shell sleep --help
#use_adb_shell_sleep_help = False

# (bool) If True, the application will be run with the adb shell kill -s
#use_adb_shell_kill_s = False

# (bool) If True, the application will be run with the adb shell kill -l
#use_adb_shell_kill_l = False

# (bool) If True, the application will be run with the adb shell kill --help
#use_adb_shell_kill_help = False

# (bool) If True, the application will be run with the adb shell killall -s
#use_adb_shell_killall_s = False

# (bool) If True, the application will be run with the adb shell killall -l
#use_adb_shell_killall_l = False

# (bool) If True, the application will be run with the adb shell killall --help
#use_adb_shell_killall_help = False

# (bool) If True, the application will be run with the adb shell pkill -s
#use_adb_shell_pkill_s = False

# (bool) If True, the application will be run with the adb shell pkill -l
#use_adb_shell_pkill_l = False

# (bool) If True, the application will be run with the adb shell pkill --help
#use_adb_shell_pkill_help = False

# (bool) If True, the application will be run with the adb shell killall5 --help
#use_adb_shell_killall5_help = False

# (bool) If True, the application will be run with the adb shell reboot -p
#use_adb_shell_reboot_p = False

# (bool) If True, the application will be run with the adb shell reboot -f
#use_adb_shell_reboot_f = False

# (bool) If True, the application will be run with the adb shell reboot --help
#use_adb_shell_reboot_help = False

# (bool) If True, the application will be run with the adb shell poweroff --help
#use_adb_shell_poweroff_help = False

# (bool) If True, the application will be run with the adb shell halt --help
#use_adb_shell_halt_help = False

# (bool) If True, the application will be run with the adb shell sync --help
#use_adb_shell_sync_help = False

# (bool) If True, the application will be run with the adb shell mount -t
#use_adb_shell_mount_t = False

# (bool) If True, the application will be run with the adb shell mount -o
#use_adb_shell_mount_o = False

# (bool) If True, the application will be run with the adb shell mount --help
#use_adb_shell_mount_help = False

# (bool) If True, the application will be run with the adb shell umount -f
#use_adb_shell_umount_f = False

# (bool) If True, the application will be run with the adb shell umount -l
#use_adb_shell_umount_l = False

# (bool) If True, the application will be run with the adb shell umount --help
#use_adb_shell_umount_help = False

# (bool) If True, the application will be run with the adb shell swapon -a
#use_adb_shell_swapon_a = False

# (bool) If True, the application will be run with the adb shell swapon -s
#use_adb_shell_swapon_s = False

# (bool) If True, the application will be run with the adb shell swapon --help
#use_adb_shell_swapon_help = False

# (bool) If True, the application will be run with the adb shell swapoff -a
#use_adb_shell_swapoff_a = False

# (bool) If True, the application will be run with the adb shell swapoff --help
#use_adb_shell_swapoff_help = False

# (bool) If True, the application will be run with the adb shell df -h
#use_adb_shell_df_h = False

# (bool) If True, the application will be run with the adb shell df -T
#use_adb_shell_df_T = False

# (bool) If True, the application will be run with the adb shell df --help
#use_adb_shell_df_help = False

# (bool) If True, the application will be run with the adb shell du -h
#use_adb_shell_du_h = False

# (bool) If True, the application will be run with the adb shell du -s
#use_adb_shell_du_s = False

# (bool) If True, the application will be run with the adb shell du --help
#use_adb_shell_du_help = False

# (bool) If True, the application will be run with the adb shell free -h
#use_adb_shell_free_h = False

# (bool) If True, the application will be run with the adb shell free -m
#use_adb_shell_free_m = False

# (bool) If True, the application will be run with the adb shell free --help
#use_adb_shell_free_help = False

# (bool) If True, the application will be run with the adb shell top -m 10
#use_adb_shell_top_m_10 = False

# (bool) If True, the application will be run with the adb shell top -t -n 1
#use_adb_shell_top_t_n_1 = False

# (bool) If True, the application will be run with the adb shell top -s cpu
#use_adb_shell_top_s_cpu = False

# (bool) If True, the application will be run with the adb shell top -o %CPU
#use_adb_shell_top_o_cpu = False

# (bool) If True, the application will be run with the adb shell top -n 5
#use_adb_shell_top_n_5 = False

# (bool) If True, the application will be run with the adb shell top -d 2
#use_adb_shell_top_d_2 = False

# (bool) If True, the application will be run with the adb shell ps -A | grep
#use_adb_shell_ps_A_grep = False

# (bool) If True, the application will be run with the adb shell ps -e | grep
#use_adb_shell_ps_e_grep = False

# (bool) If True, the application will be run with the adb shell ps -f | grep
#use_adb_shell_ps_f_grep = False

# (bool) If True, the application will be run with the adb shell ps -l | grep
#use_adb_shell_ps_l_grep = False

# (bool) If True, the application will be run with the adb shell ps -u | grep
#use_adb_shell_ps_u_grep = False

# (bool) If True, the application will be run with the adb shell ps -p | grep
#use_adb_shell_ps_p_grep = False

# (bool) If True, the application will be run with the adb shell ps -t | grep
#use_adb_shell_ps_t_grep = False

# (bool) If True, the application will be run with the adb shell ps -C | grep
#use_adb_shell_ps_C_grep = False

# (bool) If True, the application will be run with the adb shell ps -G | grep
#use_adb_shell_ps_G_grep = False

# (bool) If True, the application will be run with the adb shell ps -g | grep
#use_adb_shell_ps_g_grep = False

# (bool) If True, the application will be run with the adb shell ps -o | grep
#use_adb_shell_ps_o_grep = False

# (bool) If True, the application will be run with the adb shell ps -s | grep
#use_adb_shell_ps_s_grep = False

# (bool) If True, the application will be run with the adb shell ps -T | grep
#use_adb_shell_ps_T_grep = False

# (bool) If True, the application will be run with the adb shell ps -w | grep
#use_adb_shell_ps_w_grep = False

# (bool) If True, the application will be run with the adb shell netstat -a | grep
#use_adb_shell_netstat_a_grep = False

# (bool) If True, the application will be run with the adb shell netstat -t | grep
#use_adb_shell_netstat_t_grep = False

# (bool) If True, the application will be run with the adb shell netstat -u | grep
#use_adb_shell_netstat_u_grep = False

# (bool) If True, the application will be run with the adb shell netstat -l | grep
#use_adb_shell_netstat_l_grep = False

# (bool) If True, the application will be run with the adb shell netstat -p | grep
#use_adb_shell_netstat_p_grep = False

# (bool) If True, the application will be run with the adb shell netstat -n | grep
#use_adb_shell_netstat_n_grep = False

# (bool) If True, the application will be run with the adb shell netstat -e | grep
#use_adb_shell_netstat_e_grep = False

# (bool) If True, the application will be run with the adb shell netstat -c | grep
#use_adb_shell_netstat_c_grep = False

# (bool) If True, the application will be run with the adb shell ifconfig -a | grep
#use_adb_shell_ifconfig_a_grep = False

# (bool) If True, the application will be run with the adb shell ifconfig -s | grep
#use_adb_shell_ifconfig_s_grep = False

# (bool) If True, the application will be run with the adb shell route -n | grep
#use_adb_shell_route_n_grep = False

# (bool) If True, the application will be run with the adb shell ping -c 4
#use_adb_shell_ping_c_4 = False

# (bool) If True, the application will be run with the adb shell ping -s 56
#use_adb_shell_ping_s_56 = False

# (bool) If True, the application will be run with the adb shell ping -i 1
#use_adb_shell_ping_i_1 = False

# (bool) If True, the application will be run with the adb shell ping -t 255
#use_adb_shell_ping_t_255 = False

# (bool) If True, the application will be run with the adb shell ping -W 1
#use_adb_shell_ping_W_1 = False

# (bool) If True, the application will be run with the adb shell traceroute -n | grep
#use_adb_shell_traceroute_n_grep = False

# (bool) If True, the application will be run with the adb shell traceroute -m 30 | grep
#use_adb_shell_traceroute_m_30_grep = False

# (bool) If True, the application will be run with the adb shell traceroute -p 80 | grep
#use_adb_shell_traceroute_p_80_grep = False

# (bool) If True, the application will be run with the adb shell traceroute -q 1 | grep
#use_adb_shell_traceroute_q_1_grep = False

# (bool) If True, the application will be run with the adb shell traceroute -w 1 | grep
#use_adb_shell_traceroute_w_1_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=A | grep
#use_adb_shell_nslookup_type_A_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=AAAA | grep
#use_adb_shell_nslookup_type_AAAA_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=MX | grep
#use_adb_shell_nslookup_type_MX_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=NS | grep
#use_adb_shell_nslookup_type_NS_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=SOA | grep
#use_adb_shell_nslookup_type_SOA_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -type=TXT | grep
#use_adb_shell_nslookup_type_TXT_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -debug | grep
#use_adb_shell_nslookup_debug_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -timeout=5 | grep
#use_adb_shell_nslookup_timeout_5_grep = False

# (bool) If True, the application will be run with the adb shell nslookup -retry=3 | grep
#use_adb_shell_nslookup_retry_3_grep = False

# (bool) If True, the application will be run with the adb shell dig +short | grep
#use_adb_shell_dig_short_grep = False

# (bool) If True, the application will be run with the adb shell dig +trace | grep
#use_adb_shell_dig_trace_grep = False

# (bool) If True, the application will be run with the adb shell dig +stats | grep
#use_adb_shell_dig_stats_grep = False

# (bool) If True, the application will be run with the adb shell dig +nocmd | grep
#use_adb_shell_dig_nocmd_grep = False

# (bool) If True, the application will be run with the adb shell dig +cmd | grep
#use_adb_shell_dig_cmd_grep = False

# (bool) If True, the application will be run with the adb shell curl -s | grep
#use_adb_shell_curl_s_grep = False

# (bool) If True, the application will be run with the adb shell curl -v | grep
#use_adb_shell_curl_v_grep = False

# (bool) If True, the application will be run with the adb shell curl -o | grep
#use_adb_shell_curl_o_grep = False

# (bool) If True, the application will be run with the adb shell curl -O | grep
#use_adb_shell_curl_O_grep = False

# (bool) If True, the application will be run with the adb shell curl -L | grep
#use_adb_shell_curl_L_grep = False

# (bool) If True, the application will be run with the adb shell curl -k | grep
#use_adb_shell_curl_k_grep = False

# (bool) If True, the application will be run with the adb shell wget -q | grep
#use_adb_shell_wget_q_grep = False

# (bool) If True, the application will be run with the adb shell wget -v | grep
#use_adb_shell_wget_v_grep = False

# (bool) If True, the application will be run with the adb shell wget -O | grep
#use_adb_shell_wget_O_grep = False

# (bool) If True, the application will be run with the adb shell wget -P | grep
#use_adb_shell_wget_P_grep = False

# (bool) If True, the application will be run with the adb shell wget -c | grep
#use_adb_shell_wget_c_grep = False

# (bool) If True, the application will be run with the adb shell wget -t 3 | grep
#use_adb_shell_wget_t_3_grep = False

# (bool) If True, the application will be run with the adb shell busybox | grep
#use_adb_shell_busybox_grep = False

# (bool) If True, the application will be run with the adb shell find -name | grep
#use_adb_shell_find_name_grep = False

# (bool) If True, the application will be run with the adb shell find -type | grep
#use_adb_shell_find_type_grep = False

# (bool) If True, the application will be run with the adb shell find -path | grep
#use_adb_shell_find_path_grep = False

# (bool) If True, the application will be run with the adb shell find -regex | grep
#use_adb_shell_find_regex_grep = False

# (bool) If True, the application will be run with the adb shell find -exec | grep
#use_adb_shell_find_exec_grep = False

# (bool) If True, the application will be run with the adb shell find -delete | grep
#use_adb_shell_find_delete_grep = False

# (bool) If True, the application will be run with the adb shell grep -i | grep
#use_adb_shell_grep_i_grep = False

# (bool) If True, the application will be run with the adb shell grep -v | grep
#use_adb_shell_grep_v_grep = False

# (bool) If True, the application will be run with the adb shell grep -r | grep
#use_adb_shell_grep_r_grep = False

# (bool) If True, the application will be run with the adb shell grep -l | grep
#use_adb_shell_grep_l_grep = False

# (