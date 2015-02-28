#!/bin/bash

#Tweet用の画像ファイルを格納
#ご褒美用
Goodfolder="path/goodimage/"
Goodfiles="path/goodimage/*"
#お説教用
Badfolder="path/badimage/"
Badfiles="path/badimage/*"

countg=`ls -1 $Goodfolder | wc -l`
countb=`ls -1 $Badfolder | wc -l`

echo "countg" $countg
echo "countb" $countb

count=0
filenameg=""
filenameb=""

numb=`expr $RANDOM % $countb`
echo $numb
#お説教
for filepath in $Badfiles

do
if [ $count -eq $numb ]; then
	filenameb=`basename ${filepath}`
	echo $filenameb
fi
	count=`expr $count \+ 1`
done

count=0

numg=`expr $RANDOM % $countg`
	#ご褒美
for filepath in ${Goodfiles}

do
if [ $count -eq $numg ]; then
	filenameg=`basename ${filepath}`
	echo $filenameg
fi
	count=`expr $count \+ 1`
done


var=`find ./* -mtime -1 -type f|wc -l`
echo $var
#更新されているファイルが1個未満つまり０個
if [ $var -lt 1 ]; then
	
echo ${Badfolder}${filenameb}
python img-merge.py ${Badfolder}${filenameb} 0

  python tweet-proceed1.py 進捗なんにもないです…
  echo "今日進捗無い…？"
else
	
echo ${Goodfolder}${filenameg}
python img-merge.py ${Goodfolder}${filenameg} 1

  python tweet-proceed1.py 進捗ありました！
  echo "褒美をやろう"
fi

rm -rf ./output.png

exit 0