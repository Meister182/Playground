set -euxo pipefail
echo "Starting"

# simulates a command that succed
(exit 0)
echo "Last command was OK!"

# simulates a command that failed
#   - Stop when `set -o pipefail`
(exit 1)
echo "Last command was NOK!"
