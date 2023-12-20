set -e
target_dir="$1"

echo "Target: ${target_dir}"

has_subdirs=$(find "${target_dir}/"* -maxdepth 1 -type d)
echo "SubDirs: ${has_subdirs}"
if [ -n "${has_subdirs}" ]; then
	echo "Has subdirs, using new method"
	for s in ${has_subdirs}; do
		echo "-- subdir: ${s}"
		for i in $(ls ${s}); do
			echo "---- file: ${i}"
		done
	done
else
	echo "Doesn't have subdirs, using OLD method"
	for i in $(ls ${target_dir}); do
		echo "---- file: ${i}"
	done
fi
