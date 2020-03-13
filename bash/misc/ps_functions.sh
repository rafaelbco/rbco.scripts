# Extract a PID from a line with a PID at the beginning.
function extract_pid {
    sed 's/^ *//g' | cut -d' ' -f1
}

# Given a line containing a PID at the beginning, print the full command of the process.
function print_cmd {
    local PID=$(echo $1 | extract_pid)
    ps -ww -o args ${PID} | tail -1
}

export -f extract_pid
export -f print_cmd
