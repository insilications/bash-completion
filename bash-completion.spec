#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bash-completion
Version  : 2.5
Release  : 19
URL      : https://github.com/scop/bash-completion/archive/2.5.tar.gz
Source0  : https://github.com/scop/bash-completion/archive/2.5.tar.gz
Summary  : programmable completion for the bash shell
Group    : Development/Tools
License  : GPL-2.0
Requires: bash-completion-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: stateless.patch

%description
# bash-completion
[![Build Status](https://travis-ci.org/scop/bash-completion.svg?branch=master)](https://travis-ci.org/scop/bash-completion)

%package data
Summary: data components for the bash-completion package.
Group: Data

%description data
data components for the bash-completion package.


%package dev
Summary: dev components for the bash-completion package.
Group: Development
Requires: bash-completion-data
Provides: bash-completion-devel

%description dev
dev components for the bash-completion package.


%prep
%setup -q -n bash-completion-2.5
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486511381
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1486511381
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
%exclude /usr/share/bash-completion/completions/mount
%exclude /usr/share/bash-completion/completions/umount
/usr/share/bash-completion/bash_completion
/usr/share/bash-completion/completions/2to3
/usr/share/bash-completion/completions/7z
/usr/share/bash-completion/completions/7za
/usr/share/bash-completion/completions/_cal
/usr/share/bash-completion/completions/_chfn
/usr/share/bash-completion/completions/_chsh
/usr/share/bash-completion/completions/_dmesg
/usr/share/bash-completion/completions/_eject
/usr/share/bash-completion/completions/_hexdump
/usr/share/bash-completion/completions/_hwclock
/usr/share/bash-completion/completions/_ionice
/usr/share/bash-completion/completions/_look
/usr/share/bash-completion/completions/_mock
/usr/share/bash-completion/completions/_modules
/usr/share/bash-completion/completions/_newgrp
/usr/share/bash-completion/completions/_nmcli
/usr/share/bash-completion/completions/_renice
/usr/share/bash-completion/completions/_repomanage
/usr/share/bash-completion/completions/_reptyr
/usr/share/bash-completion/completions/_rtcwake
/usr/share/bash-completion/completions/_runuser
/usr/share/bash-completion/completions/_su
/usr/share/bash-completion/completions/_svn
/usr/share/bash-completion/completions/_svnadmin
/usr/share/bash-completion/completions/_svnlook
/usr/share/bash-completion/completions/_udevadm
/usr/share/bash-completion/completions/_write
/usr/share/bash-completion/completions/_yum
/usr/share/bash-completion/completions/a2x
/usr/share/bash-completion/completions/abook
/usr/share/bash-completion/completions/aclocal
/usr/share/bash-completion/completions/aclocal-1.10
/usr/share/bash-completion/completions/aclocal-1.11
/usr/share/bash-completion/completions/aclocal-1.12
/usr/share/bash-completion/completions/aclocal-1.13
/usr/share/bash-completion/completions/aclocal-1.14
/usr/share/bash-completion/completions/aclocal-1.15
/usr/share/bash-completion/completions/acpi
/usr/share/bash-completion/completions/adb
/usr/share/bash-completion/completions/add_members
/usr/share/bash-completion/completions/alias
/usr/share/bash-completion/completions/alpine
/usr/share/bash-completion/completions/alternatives
/usr/share/bash-completion/completions/animate
/usr/share/bash-completion/completions/ant
/usr/share/bash-completion/completions/apache2ctl
/usr/share/bash-completion/completions/appdata-validate
/usr/share/bash-completion/completions/apropos
/usr/share/bash-completion/completions/apt-build
/usr/share/bash-completion/completions/apt-cache
/usr/share/bash-completion/completions/apt-get
/usr/share/bash-completion/completions/aptitude
/usr/share/bash-completion/completions/arch
/usr/share/bash-completion/completions/arm-koji
/usr/share/bash-completion/completions/arping
/usr/share/bash-completion/completions/arpspoof
/usr/share/bash-completion/completions/asciidoc
/usr/share/bash-completion/completions/asciidoc.py
/usr/share/bash-completion/completions/aspell
/usr/share/bash-completion/completions/autoconf
/usr/share/bash-completion/completions/autoheader
/usr/share/bash-completion/completions/automake
/usr/share/bash-completion/completions/automake-1.10
/usr/share/bash-completion/completions/automake-1.11
/usr/share/bash-completion/completions/automake-1.12
/usr/share/bash-completion/completions/automake-1.13
/usr/share/bash-completion/completions/automake-1.14
/usr/share/bash-completion/completions/automake-1.15
/usr/share/bash-completion/completions/autoreconf
/usr/share/bash-completion/completions/autorpm
/usr/share/bash-completion/completions/autoscan
/usr/share/bash-completion/completions/autossh
/usr/share/bash-completion/completions/autoupdate
/usr/share/bash-completion/completions/avctrl
/usr/share/bash-completion/completions/badblocks
/usr/share/bash-completion/completions/bk
/usr/share/bash-completion/completions/brctl
/usr/share/bash-completion/completions/btdownloadcurses.py
/usr/share/bash-completion/completions/btdownloadgui.py
/usr/share/bash-completion/completions/btdownloadheadless.py
/usr/share/bash-completion/completions/bts
/usr/share/bash-completion/completions/bzip2
/usr/share/bash-completion/completions/c++
/usr/share/bash-completion/completions/cancel
/usr/share/bash-completion/completions/cardctl
/usr/share/bash-completion/completions/cc
/usr/share/bash-completion/completions/ccache
/usr/share/bash-completion/completions/cdrecord
/usr/share/bash-completion/completions/cfagent
/usr/share/bash-completion/completions/cfrun
/usr/share/bash-completion/completions/chage
/usr/share/bash-completion/completions/change_pw
/usr/share/bash-completion/completions/check_db
/usr/share/bash-completion/completions/check_perms
/usr/share/bash-completion/completions/checksec
/usr/share/bash-completion/completions/chgrp
/usr/share/bash-completion/completions/chkconfig
/usr/share/bash-completion/completions/chown
/usr/share/bash-completion/completions/chpasswd
/usr/share/bash-completion/completions/chronyc
/usr/share/bash-completion/completions/chrpath
/usr/share/bash-completion/completions/ci
/usr/share/bash-completion/completions/ciptool
/usr/share/bash-completion/completions/civclient
/usr/share/bash-completion/completions/civserver
/usr/share/bash-completion/completions/cksfv
/usr/share/bash-completion/completions/cleanarch
/usr/share/bash-completion/completions/clisp
/usr/share/bash-completion/completions/clone_member
/usr/share/bash-completion/completions/clzip
/usr/share/bash-completion/completions/co
/usr/share/bash-completion/completions/colormake
/usr/share/bash-completion/completions/compare
/usr/share/bash-completion/completions/compgen
/usr/share/bash-completion/completions/complete
/usr/share/bash-completion/completions/composite
/usr/share/bash-completion/completions/config_list
/usr/share/bash-completion/completions/configure
/usr/share/bash-completion/completions/conjure
/usr/share/bash-completion/completions/convert
/usr/share/bash-completion/completions/cowsay
/usr/share/bash-completion/completions/cowthink
/usr/share/bash-completion/completions/cpan2dist
/usr/share/bash-completion/completions/cpio
/usr/share/bash-completion/completions/cppcheck
/usr/share/bash-completion/completions/createdb
/usr/share/bash-completion/completions/createuser
/usr/share/bash-completion/completions/crontab
/usr/share/bash-completion/completions/cryptsetup
/usr/share/bash-completion/completions/curl
/usr/share/bash-completion/completions/cvs
/usr/share/bash-completion/completions/cvsps
/usr/share/bash-completion/completions/dcop
/usr/share/bash-completion/completions/dd
/usr/share/bash-completion/completions/declare
/usr/share/bash-completion/completions/deja-dup
/usr/share/bash-completion/completions/desktop-file-validate
/usr/share/bash-completion/completions/dfutool
/usr/share/bash-completion/completions/dhclient
/usr/share/bash-completion/completions/dict
/usr/share/bash-completion/completions/display
/usr/share/bash-completion/completions/dnsspoof
/usr/share/bash-completion/completions/dot
/usr/share/bash-completion/completions/dpkg
/usr/share/bash-completion/completions/dpkg-deb
/usr/share/bash-completion/completions/dpkg-query
/usr/share/bash-completion/completions/dpkg-reconfigure
/usr/share/bash-completion/completions/dpkg-source
/usr/share/bash-completion/completions/dropdb
/usr/share/bash-completion/completions/dropuser
/usr/share/bash-completion/completions/dselect
/usr/share/bash-completion/completions/dsniff
/usr/share/bash-completion/completions/dumpdb
/usr/share/bash-completion/completions/dumpe2fs
/usr/share/bash-completion/completions/e2freefrag
/usr/share/bash-completion/completions/e2label
/usr/share/bash-completion/completions/edquota
/usr/share/bash-completion/completions/eog
/usr/share/bash-completion/completions/ether-wake
/usr/share/bash-completion/completions/evince
/usr/share/bash-completion/completions/explodepkg
/usr/share/bash-completion/completions/export
/usr/share/bash-completion/completions/f77
/usr/share/bash-completion/completions/f95
/usr/share/bash-completion/completions/faillog
/usr/share/bash-completion/completions/fbgs
/usr/share/bash-completion/completions/fbi
/usr/share/bash-completion/completions/feh
/usr/share/bash-completion/completions/file
/usr/share/bash-completion/completions/file-roller
/usr/share/bash-completion/completions/filebucket
/usr/share/bash-completion/completions/filefrag
/usr/share/bash-completion/completions/filesnarf
/usr/share/bash-completion/completions/find
/usr/share/bash-completion/completions/find_member
/usr/share/bash-completion/completions/flake8
/usr/share/bash-completion/completions/freebsd-update
/usr/share/bash-completion/completions/freeciv-gtk2
/usr/share/bash-completion/completions/freeciv-sdl
/usr/share/bash-completion/completions/freeciv-server
/usr/share/bash-completion/completions/freeciv-xaw
/usr/share/bash-completion/completions/function
/usr/share/bash-completion/completions/fusermount
/usr/share/bash-completion/completions/g++
/usr/share/bash-completion/completions/g4
/usr/share/bash-completion/completions/g77
/usr/share/bash-completion/completions/g95
/usr/share/bash-completion/completions/gcc
/usr/share/bash-completion/completions/gcj
/usr/share/bash-completion/completions/gcl
/usr/share/bash-completion/completions/gdb
/usr/share/bash-completion/completions/genaliases
/usr/share/bash-completion/completions/gendiff
/usr/share/bash-completion/completions/genisoimage
/usr/share/bash-completion/completions/getent
/usr/share/bash-completion/completions/gfortran
/usr/share/bash-completion/completions/gkrellm
/usr/share/bash-completion/completions/gkrellm2
/usr/share/bash-completion/completions/gmake
/usr/share/bash-completion/completions/gmplayer
/usr/share/bash-completion/completions/gnatmake
/usr/share/bash-completion/completions/gnokii
/usr/share/bash-completion/completions/gnome-mplayer
/usr/share/bash-completion/completions/gnumake
/usr/share/bash-completion/completions/gpasswd
/usr/share/bash-completion/completions/gpc
/usr/share/bash-completion/completions/gpg
/usr/share/bash-completion/completions/gpg2
/usr/share/bash-completion/completions/gphoto2
/usr/share/bash-completion/completions/gprof
/usr/share/bash-completion/completions/groupadd
/usr/share/bash-completion/completions/groupdel
/usr/share/bash-completion/completions/groupmems
/usr/share/bash-completion/completions/groupmod
/usr/share/bash-completion/completions/growisofs
/usr/share/bash-completion/completions/grpck
/usr/share/bash-completion/completions/gzip
/usr/share/bash-completion/completions/hciattach
/usr/share/bash-completion/completions/hciconfig
/usr/share/bash-completion/completions/hcitool
/usr/share/bash-completion/completions/hd
/usr/share/bash-completion/completions/hddtemp
/usr/share/bash-completion/completions/hid2hci
/usr/share/bash-completion/completions/host
/usr/share/bash-completion/completions/hostname
/usr/share/bash-completion/completions/hping
/usr/share/bash-completion/completions/hping2
/usr/share/bash-completion/completions/hping3
/usr/share/bash-completion/completions/htop
/usr/share/bash-completion/completions/htpasswd
/usr/share/bash-completion/completions/iconv
/usr/share/bash-completion/completions/id
/usr/share/bash-completion/completions/identify
/usr/share/bash-completion/completions/idn
/usr/share/bash-completion/completions/ifdown
/usr/share/bash-completion/completions/ifstatus
/usr/share/bash-completion/completions/iftop
/usr/share/bash-completion/completions/ifup
/usr/share/bash-completion/completions/import
/usr/share/bash-completion/completions/info
/usr/share/bash-completion/completions/inject
/usr/share/bash-completion/completions/insmod
/usr/share/bash-completion/completions/insmod.static
/usr/share/bash-completion/completions/installpkg
/usr/share/bash-completion/completions/interdiff
/usr/share/bash-completion/completions/invoke-rc.d
/usr/share/bash-completion/completions/ip
/usr/share/bash-completion/completions/iperf
/usr/share/bash-completion/completions/ipmitool
/usr/share/bash-completion/completions/ipsec
/usr/share/bash-completion/completions/iptables
/usr/share/bash-completion/completions/ipv6calc
/usr/share/bash-completion/completions/iscsiadm
/usr/share/bash-completion/completions/isql
/usr/share/bash-completion/completions/iwconfig
/usr/share/bash-completion/completions/iwlist
/usr/share/bash-completion/completions/iwpriv
/usr/share/bash-completion/completions/iwspy
/usr/share/bash-completion/completions/jar
/usr/share/bash-completion/completions/jarsigner
/usr/share/bash-completion/completions/java
/usr/share/bash-completion/completions/javac
/usr/share/bash-completion/completions/javadoc
/usr/share/bash-completion/completions/javaws
/usr/share/bash-completion/completions/jpegoptim
/usr/share/bash-completion/completions/jps
/usr/share/bash-completion/completions/jshint
/usr/share/bash-completion/completions/k3b
/usr/share/bash-completion/completions/kcov
/usr/share/bash-completion/completions/kill
/usr/share/bash-completion/completions/killall
/usr/share/bash-completion/completions/kldload
/usr/share/bash-completion/completions/kldunload
/usr/share/bash-completion/completions/koji
/usr/share/bash-completion/completions/kplayer
/usr/share/bash-completion/completions/ktutil
/usr/share/bash-completion/completions/l2ping
/usr/share/bash-completion/completions/larch
/usr/share/bash-completion/completions/lastlog
/usr/share/bash-completion/completions/lbzip2
/usr/share/bash-completion/completions/ldapadd
/usr/share/bash-completion/completions/ldapcompare
/usr/share/bash-completion/completions/ldapdelete
/usr/share/bash-completion/completions/ldapmodify
/usr/share/bash-completion/completions/ldapmodrdn
/usr/share/bash-completion/completions/ldappasswd
/usr/share/bash-completion/completions/ldapsearch
/usr/share/bash-completion/completions/ldapvi
/usr/share/bash-completion/completions/ldapwhoami
/usr/share/bash-completion/completions/lftp
/usr/share/bash-completion/completions/lftpget
/usr/share/bash-completion/completions/lilo
/usr/share/bash-completion/completions/links
/usr/share/bash-completion/completions/lintian
/usr/share/bash-completion/completions/lintian-info
/usr/share/bash-completion/completions/lisp
/usr/share/bash-completion/completions/list_admins
/usr/share/bash-completion/completions/list_lists
/usr/share/bash-completion/completions/list_members
/usr/share/bash-completion/completions/list_owners
/usr/share/bash-completion/completions/lpq
/usr/share/bash-completion/completions/lpr
/usr/share/bash-completion/completions/lrzip
/usr/share/bash-completion/completions/lsof
/usr/share/bash-completion/completions/lua
/usr/share/bash-completion/completions/luac
/usr/share/bash-completion/completions/luseradd
/usr/share/bash-completion/completions/luserdel
/usr/share/bash-completion/completions/lusermod
/usr/share/bash-completion/completions/lvchange
/usr/share/bash-completion/completions/lvcreate
/usr/share/bash-completion/completions/lvdisplay
/usr/share/bash-completion/completions/lvextend
/usr/share/bash-completion/completions/lvm
/usr/share/bash-completion/completions/lvmdiskscan
/usr/share/bash-completion/completions/lvreduce
/usr/share/bash-completion/completions/lvremove
/usr/share/bash-completion/completions/lvrename
/usr/share/bash-completion/completions/lvresize
/usr/share/bash-completion/completions/lvs
/usr/share/bash-completion/completions/lvscan
/usr/share/bash-completion/completions/lz4
/usr/share/bash-completion/completions/lz4c
/usr/share/bash-completion/completions/lzip
/usr/share/bash-completion/completions/lzma
/usr/share/bash-completion/completions/lzop
/usr/share/bash-completion/completions/macof
/usr/share/bash-completion/completions/mailmanctl
/usr/share/bash-completion/completions/mailsnarf
/usr/share/bash-completion/completions/make
/usr/share/bash-completion/completions/makepkg
/usr/share/bash-completion/completions/man
/usr/share/bash-completion/completions/mc
/usr/share/bash-completion/completions/mcrypt
/usr/share/bash-completion/completions/mdadm
/usr/share/bash-completion/completions/mdecrypt
/usr/share/bash-completion/completions/mdtool
/usr/share/bash-completion/completions/medusa
/usr/share/bash-completion/completions/mencoder
/usr/share/bash-completion/completions/mii-diag
/usr/share/bash-completion/completions/mii-tool
/usr/share/bash-completion/completions/minicom
/usr/share/bash-completion/completions/mkinitrd
/usr/share/bash-completion/completions/mkisofs
/usr/share/bash-completion/completions/mktemp
/usr/share/bash-completion/completions/mmsitepass
/usr/share/bash-completion/completions/modinfo
/usr/share/bash-completion/completions/modprobe
/usr/share/bash-completion/completions/mogrify
/usr/share/bash-completion/completions/monodevelop
/usr/share/bash-completion/completions/montage
/usr/share/bash-completion/completions/mount.linux
/usr/share/bash-completion/completions/mplayer
/usr/share/bash-completion/completions/mplayer2
/usr/share/bash-completion/completions/mr
/usr/share/bash-completion/completions/msgsnarf
/usr/share/bash-completion/completions/msynctool
/usr/share/bash-completion/completions/mtx
/usr/share/bash-completion/completions/munin-node-configure
/usr/share/bash-completion/completions/munin-run
/usr/share/bash-completion/completions/munin-update
/usr/share/bash-completion/completions/munindoc
/usr/share/bash-completion/completions/mussh
/usr/share/bash-completion/completions/mutt
/usr/share/bash-completion/completions/muttng
/usr/share/bash-completion/completions/mysql
/usr/share/bash-completion/completions/mysqladmin
/usr/share/bash-completion/completions/nc
/usr/share/bash-completion/completions/ncal
/usr/share/bash-completion/completions/ncftp
/usr/share/bash-completion/completions/nethogs
/usr/share/bash-completion/completions/newlist
/usr/share/bash-completion/completions/newusers
/usr/share/bash-completion/completions/ngrep
/usr/share/bash-completion/completions/nmap
/usr/share/bash-completion/completions/nslookup
/usr/share/bash-completion/completions/ntpdate
/usr/share/bash-completion/completions/openssl
/usr/share/bash-completion/completions/opera
/usr/share/bash-completion/completions/optipng
/usr/share/bash-completion/completions/p4
/usr/share/bash-completion/completions/pack200
/usr/share/bash-completion/completions/passwd
/usr/share/bash-completion/completions/patch
/usr/share/bash-completion/completions/pbzip2
/usr/share/bash-completion/completions/pccardctl
/usr/share/bash-completion/completions/pdftotext
/usr/share/bash-completion/completions/pdlzip
/usr/share/bash-completion/completions/perl
/usr/share/bash-completion/completions/perldoc
/usr/share/bash-completion/completions/pgrep
/usr/share/bash-completion/completions/phing
/usr/share/bash-completion/completions/pidof
/usr/share/bash-completion/completions/pigz
/usr/share/bash-completion/completions/pine
/usr/share/bash-completion/completions/pinfo
/usr/share/bash-completion/completions/ping
/usr/share/bash-completion/completions/ping6
/usr/share/bash-completion/completions/pkg-config
/usr/share/bash-completion/completions/pkg-get
/usr/share/bash-completion/completions/pkg_deinstall
/usr/share/bash-completion/completions/pkg_delete
/usr/share/bash-completion/completions/pkg_info
/usr/share/bash-completion/completions/pkgadd
/usr/share/bash-completion/completions/pkgrm
/usr/share/bash-completion/completions/pkgtool
/usr/share/bash-completion/completions/pkgutil
/usr/share/bash-completion/completions/pkill
/usr/share/bash-completion/completions/plague-client
/usr/share/bash-completion/completions/plzip
/usr/share/bash-completion/completions/pm-hibernate
/usr/share/bash-completion/completions/pm-is-supported
/usr/share/bash-completion/completions/pm-powersave
/usr/share/bash-completion/completions/pm-suspend
/usr/share/bash-completion/completions/pm-suspend-hybrid
/usr/share/bash-completion/completions/pmake
/usr/share/bash-completion/completions/pngfix
/usr/share/bash-completion/completions/portinstall
/usr/share/bash-completion/completions/portsnap
/usr/share/bash-completion/completions/portupgrade
/usr/share/bash-completion/completions/postalias
/usr/share/bash-completion/completions/postcat
/usr/share/bash-completion/completions/postconf
/usr/share/bash-completion/completions/postfix
/usr/share/bash-completion/completions/postmap
/usr/share/bash-completion/completions/postsuper
/usr/share/bash-completion/completions/povray
/usr/share/bash-completion/completions/ppc-koji
/usr/share/bash-completion/completions/prelink
/usr/share/bash-completion/completions/protoc
/usr/share/bash-completion/completions/psql
/usr/share/bash-completion/completions/puppet
/usr/share/bash-completion/completions/puppetca
/usr/share/bash-completion/completions/puppetd
/usr/share/bash-completion/completions/puppetdoc
/usr/share/bash-completion/completions/puppetmasterd
/usr/share/bash-completion/completions/puppetqd
/usr/share/bash-completion/completions/puppetrun
/usr/share/bash-completion/completions/pvchange
/usr/share/bash-completion/completions/pvcreate
/usr/share/bash-completion/completions/pvdisplay
/usr/share/bash-completion/completions/pvmove
/usr/share/bash-completion/completions/pvremove
/usr/share/bash-completion/completions/pvs
/usr/share/bash-completion/completions/pvscan
/usr/share/bash-completion/completions/pwck
/usr/share/bash-completion/completions/pwd
/usr/share/bash-completion/completions/pwdx
/usr/share/bash-completion/completions/pwgen
/usr/share/bash-completion/completions/pxz
/usr/share/bash-completion/completions/pydoc
/usr/share/bash-completion/completions/pydoc3
/usr/share/bash-completion/completions/pyflakes
/usr/share/bash-completion/completions/pylint
/usr/share/bash-completion/completions/pypy
/usr/share/bash-completion/completions/pypy3
/usr/share/bash-completion/completions/python
/usr/share/bash-completion/completions/python2
/usr/share/bash-completion/completions/python3
/usr/share/bash-completion/completions/pyvenv
/usr/share/bash-completion/completions/pyvenv-3.4
/usr/share/bash-completion/completions/pyvenv-3.5
/usr/share/bash-completion/completions/qdbus
/usr/share/bash-completion/completions/qemu
/usr/share/bash-completion/completions/qemu-kvm
/usr/share/bash-completion/completions/qemu-system-i386
/usr/share/bash-completion/completions/qemu-system-x86_64
/usr/share/bash-completion/completions/qrunner
/usr/share/bash-completion/completions/querybts
/usr/share/bash-completion/completions/quota
/usr/share/bash-completion/completions/quotacheck
/usr/share/bash-completion/completions/quotaoff
/usr/share/bash-completion/completions/quotaon
/usr/share/bash-completion/completions/ralsh
/usr/share/bash-completion/completions/rcs
/usr/share/bash-completion/completions/rcsdiff
/usr/share/bash-completion/completions/rdesktop
/usr/share/bash-completion/completions/rdict
/usr/share/bash-completion/completions/remove_members
/usr/share/bash-completion/completions/removepkg
/usr/share/bash-completion/completions/reportbug
/usr/share/bash-completion/completions/repquota
/usr/share/bash-completion/completions/resolvconf
/usr/share/bash-completion/completions/rfcomm
/usr/share/bash-completion/completions/rfkill
/usr/share/bash-completion/completions/ri
/usr/share/bash-completion/completions/rlog
/usr/share/bash-completion/completions/rmlist
/usr/share/bash-completion/completions/rmmod
/usr/share/bash-completion/completions/route
/usr/share/bash-completion/completions/rpcdebug
/usr/share/bash-completion/completions/rpm
/usr/share/bash-completion/completions/rpm2targz
/usr/share/bash-completion/completions/rpm2tgz
/usr/share/bash-completion/completions/rpm2txz
/usr/share/bash-completion/completions/rpmbuild
/usr/share/bash-completion/completions/rpmbuild-md5
/usr/share/bash-completion/completions/rpmcheck
/usr/share/bash-completion/completions/rrdtool
/usr/share/bash-completion/completions/rsync
/usr/share/bash-completion/completions/s390-koji
/usr/share/bash-completion/completions/sbcl
/usr/share/bash-completion/completions/sbcl-mt
/usr/share/bash-completion/completions/sbopkg
/usr/share/bash-completion/completions/scp
/usr/share/bash-completion/completions/screen
/usr/share/bash-completion/completions/sdptool
/usr/share/bash-completion/completions/setquota
/usr/share/bash-completion/completions/sftp
/usr/share/bash-completion/completions/sh
/usr/share/bash-completion/completions/sidedoor
/usr/share/bash-completion/completions/sitecopy
/usr/share/bash-completion/completions/slackpkg
/usr/share/bash-completion/completions/slapt-get
/usr/share/bash-completion/completions/slapt-src
/usr/share/bash-completion/completions/slogin
/usr/share/bash-completion/completions/smartctl
/usr/share/bash-completion/completions/smbcacls
/usr/share/bash-completion/completions/smbclient
/usr/share/bash-completion/completions/smbcquotas
/usr/share/bash-completion/completions/smbget
/usr/share/bash-completion/completions/smbpasswd
/usr/share/bash-completion/completions/smbtar
/usr/share/bash-completion/completions/smbtree
/usr/share/bash-completion/completions/snownews
/usr/share/bash-completion/completions/sparc-koji
/usr/share/bash-completion/completions/spovray
/usr/share/bash-completion/completions/sqlite3
/usr/share/bash-completion/completions/ss
/usr/share/bash-completion/completions/ssh
/usr/share/bash-completion/completions/ssh-add
/usr/share/bash-completion/completions/ssh-copy-id
/usr/share/bash-completion/completions/ssh-keygen
/usr/share/bash-completion/completions/sshfs
/usr/share/bash-completion/completions/sshmitm
/usr/share/bash-completion/completions/sshow
/usr/share/bash-completion/completions/strace
/usr/share/bash-completion/completions/stream
/usr/share/bash-completion/completions/strings
/usr/share/bash-completion/completions/sudo
/usr/share/bash-completion/completions/sudoedit
/usr/share/bash-completion/completions/svcadm
/usr/share/bash-completion/completions/svk
/usr/share/bash-completion/completions/sync_members
/usr/share/bash-completion/completions/synclient
/usr/share/bash-completion/completions/sysbench
/usr/share/bash-completion/completions/sysctl
/usr/share/bash-completion/completions/tar
/usr/share/bash-completion/completions/tcpdump
/usr/share/bash-completion/completions/tcpkill
/usr/share/bash-completion/completions/tcpnice
/usr/share/bash-completion/completions/tightvncviewer
/usr/share/bash-completion/completions/timeout
/usr/share/bash-completion/completions/tipc
/usr/share/bash-completion/completions/tracepath
/usr/share/bash-completion/completions/tracepath6
/usr/share/bash-completion/completions/tshark
/usr/share/bash-completion/completions/tune2fs
/usr/share/bash-completion/completions/typeset
/usr/share/bash-completion/completions/umount.linux
/usr/share/bash-completion/completions/unace
/usr/share/bash-completion/completions/unpack200
/usr/share/bash-completion/completions/unrar
/usr/share/bash-completion/completions/unshunt
/usr/share/bash-completion/completions/update-alternatives
/usr/share/bash-completion/completions/update-rc.d
/usr/share/bash-completion/completions/upgradepkg
/usr/share/bash-completion/completions/urlsnarf
/usr/share/bash-completion/completions/useradd
/usr/share/bash-completion/completions/userdel
/usr/share/bash-completion/completions/usermod
/usr/share/bash-completion/completions/valgrind
/usr/share/bash-completion/completions/vgcfgbackup
/usr/share/bash-completion/completions/vgcfgrestore
/usr/share/bash-completion/completions/vgchange
/usr/share/bash-completion/completions/vgck
/usr/share/bash-completion/completions/vgconvert
/usr/share/bash-completion/completions/vgcreate
/usr/share/bash-completion/completions/vgdisplay
/usr/share/bash-completion/completions/vgexport
/usr/share/bash-completion/completions/vgextend
/usr/share/bash-completion/completions/vgimport
/usr/share/bash-completion/completions/vgmerge
/usr/share/bash-completion/completions/vgmknodes
/usr/share/bash-completion/completions/vgreduce
/usr/share/bash-completion/completions/vgremove
/usr/share/bash-completion/completions/vgrename
/usr/share/bash-completion/completions/vgs
/usr/share/bash-completion/completions/vgscan
/usr/share/bash-completion/completions/vgsplit
/usr/share/bash-completion/completions/vigr
/usr/share/bash-completion/completions/vipw
/usr/share/bash-completion/completions/vmstat
/usr/share/bash-completion/completions/vncviewer
/usr/share/bash-completion/completions/vpnc
/usr/share/bash-completion/completions/watch
/usr/share/bash-completion/completions/webmitm
/usr/share/bash-completion/completions/wget
/usr/share/bash-completion/completions/whatis
/usr/share/bash-completion/completions/wine
/usr/share/bash-completion/completions/withlist
/usr/share/bash-completion/completions/wodim
/usr/share/bash-completion/completions/wol
/usr/share/bash-completion/completions/wsimport
/usr/share/bash-completion/completions/wtf
/usr/share/bash-completion/completions/wvdial
/usr/share/bash-completion/completions/xfreerdp
/usr/share/bash-completion/completions/xgamma
/usr/share/bash-completion/completions/xhost
/usr/share/bash-completion/completions/xm
/usr/share/bash-completion/completions/xmllint
/usr/share/bash-completion/completions/xmlwf
/usr/share/bash-completion/completions/xmms
/usr/share/bash-completion/completions/xmodmap
/usr/share/bash-completion/completions/xpovray
/usr/share/bash-completion/completions/xrandr
/usr/share/bash-completion/completions/xrdb
/usr/share/bash-completion/completions/xsltproc
/usr/share/bash-completion/completions/xvnc4viewer
/usr/share/bash-completion/completions/xxd
/usr/share/bash-completion/completions/xz
/usr/share/bash-completion/completions/xzdec
/usr/share/bash-completion/completions/ypcat
/usr/share/bash-completion/completions/ypmatch
/usr/share/bash-completion/completions/yum-arch
/usr/share/bash-completion/completions/zopfli
/usr/share/bash-completion/completions/zopflipng
/usr/share/bash-completion/helpers/perl
/usr/share/cmake/*
/usr/share/defaults/etc/profile.d/bash_completion.sh

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/bash-completion.pc
