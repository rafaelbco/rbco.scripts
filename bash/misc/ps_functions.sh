# Read a line from stdin and extract the PID from the beginning of the line.
function extract_pid {
    sed 's/^ *//g' | cut -d' ' -f1
}

# Given a line containing a PID at the beginning, print the full command of the process.
function print_cmd {
    local PID=$(echo $1 | extract_pid)
    cat /proc/${PID}/cmdline | xargs --null
}

export -f extract_pid
export -f print_cmd
