#!/usr/bin/zsh

mktemp -p pdf_files
for v in ../diagram_files/*.tex
do
  theroot=`echo  $v | sed "s/.tex//" | sed "s/.*\.\///"`
  myvar=$(mktemp --suffix=".tex")      # TODO: going to mktemp -d would be much safer!
  thetarget=`echo  $myvar | sed "s/.tex//"`
  cat minimal_head >> $myvar
  echo "\\input{" $theroot.tex "}" >> $myvar
  cat minimal_tail >> $myvar
  cp $v /tmp/
  cd /tmp/
  pdflatex $myvar
  mpost $theroot
  pdflatex $myvar
  pdflatex $myvar
  pdfcrop $thetarget.pdf
  mv $thetarget-crop.pdf $OLDPWD/../pdf_files/$theroot.pdf
  rm $thetarget.*
  rm $theroot.*
  cd -
done
