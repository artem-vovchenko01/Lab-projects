for var in {1..128} 
do
  echo `info bash -o -|shuf -n50|sed 's/  */ /g;s/^ //'|fmt -w 90` >> ${var}.txt 
done


