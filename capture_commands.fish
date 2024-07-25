# Path to store the logs
set -g LOGFILE "$HOME/.command_history_log"

# Create or clear the logfile
echo "Command History Log" > $LOGFILE

function fish_preexec --on-event fish_preexec
    set -g last_command (history | head -n 1 | string trim)
end

function fish_postexec --on-event fish_postexec
    echo -e "\nCOMMAND: $last_command" >> $LOGFILE
    eval "$last_command" | tee -a $LOGFILE
end