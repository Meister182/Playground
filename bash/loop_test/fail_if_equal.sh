#set -euxo pipefail
echo "Starting"

if [ "$1" -eq "$2" ]; then
        echo "Failing: $1 == $2"	
        exit 1
else
	echo "Succes: $1 != $2"
fi
