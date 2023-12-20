target_path="./target.txt"

echo "------------------------------"
echo "with $"
# Tries to call the output!
# It needs to be converted to a string and
# then use test
echo "------------------------------"
if [ -n "$(grep "target" $target_path)" ]; then
	echo "target found"
else
	echo "target not found"
fi



echo "------------------------------"
echo "without $"
# Makes use of the command exit code
# Seems equivalent to not using parenthesis
echo "------------------------------"
if (grep "target" $target_path); then
	echo "target found"
else
	echo "target not found"
fi


echo "------------------------------"
echo "without $ and parenthesis"
echo "------------------------------"
if grep "target" $target_path; then
	echo "target found"
else
	echo "target not found"
fi

