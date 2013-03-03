#!/bin/bash

case "$1" in
    start)
        synclient TouchPadOff=0
	    ;;
    stop)
        synclient TouchPadOff=1
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac

