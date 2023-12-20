

target_file="./dummy-file.txt"
while read ci r t
do
	echo "-------"
	echo $ci
	echo $r
	echo $t
done < $target_file		# redirect file content
#done <<< $(cat $target_file)	# redirect command outut


