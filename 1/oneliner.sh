sed -r 's/(.*)/\1\1/;s/one/o1e/g;s/two/t2o/g;s/three/t3e/g;s/four/f4/g;s/five/f5e/g;s/six/6/g;s/seven/7n/g;s/eight/e8t/g;s/nine/n9e/g;s/[a-z]//g;s/([0-9])[0-9]*([0-9])/\1\2/'|xargs|sed 's/ /+/g'|bc
