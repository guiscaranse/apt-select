SUPPORTED_KERNEL = 'Linux'
SUPPORTED_DISTRIBUTION_TYPE = 'Ubuntu'

UNAME = 'uname'
KERNEL_COMMAND = (UNAME, '-s')
MACHINE_COMMAND = (UNAME, '-m')
RELEASE_COMMAND = ('lsb_release', '-ics')
RELEASE_FILE = '/etc/lsb-release'

LAUNCHPAD_ARCH_32 = 'i386'
LAUNCHPAD_ARCH_64 = 'amd64'
LAUNCHPAD_ARCHES = frozenset([
    LAUNCHPAD_ARCH_32,
    LAUNCHPAD_ARCH_64
])