for i in {1..10}; do
	# clear
	echo "----- $i -----"

	./fail_if_equal.sh $i 5 || break
	# an equivalent test would be
	# test $i -eq 5 && break
done

# There should be some check based on the last return code
echo "=== failed at: $i ==="

