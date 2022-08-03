#/bin/bash

# When it finds a true , it skips until the next '&&'  <-> if true , then its all true unless there is an '&&'
# When it finds a false, it skips until the next '||'  <-> if false, then its all false unless there is an '||'
echo -n "1: "; true || echo "skipped" || echo "skipped" || echo "skipped" || echo "skipped" && echo "not skiped"
echo -n "2: "; false && echo "skipped" && echo "skipped" && echo "skipped" && echo "skipped" || echo "not skiped"

## mixed weird logics:
# Should print ABCD
echo -n "3: "; false || echo -n 'A' && false || echo -n 'B' && false || echo -n 'C' && false || echo 'D'

# Should print AD
echo -n "4: "; false || echo -n 'A' && true || echo -n 'B' && true || echo -n 'C' && false || echo 'D'
