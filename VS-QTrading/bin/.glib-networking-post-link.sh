# When cross-compiling, or installing for a different platform, the commands
# can't be executed. So we catch errors and print a message instead of failing.
{ # try block
  "${PREFIX}/bin/gio-querymodules" "${PREFIX}/lib/gio/modules"
} ||
{ # catch block
    echo "ERROR: Failed to complete glib-networking's post-link script."
    echo "To fix this, activate the environment and run:"
    echo "    gio-querymodules \"${PREFIX}/lib/gio/modules\""
} >> "${PREFIX}/.messages.txt"
