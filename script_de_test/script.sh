#!/bin/bash

aMin=($(sort -g -k 1 resR.txt | sed -n '1p;$p' | cut -d' ' -f1))
aMax=($(sort -g -k 1 -r resR.txt | sed -n '1p;$p' | cut -d' ' -f1))

xmin=0
xmax=$aMax
 
bMin=($(sort -g -k 2 resR.txt | sed -n '1p;$p' | cut -d' ' -f2))
bMax=($(sort -g -k 2 -r resR.txt | sed -n '1p;$p' | cut -d' ' -f2))

ymin=0
ymax=$bMax+1
   


echo "$aMin"
echo "$aMax"
echo "$bMin"
echo "$bMax"
  
echo "set terminal png size 800,500 enhanced background rgb 'white'" > gnuplot_script
echo "set style line 1 lt 1 lw 1.5 pt 3 linecolor rgb '#ff00ff'" >> gnuplot_script
echo "set output 'graphe_2.png'" >> gnuplot_script
echo "set autoscale" >> gnuplot_script
echo "set xtic auto" >> gnuplot_script
echo "set ytic auto" >> gnuplot_script 
echo "set title 'Temps moyen d une requête en fonction du nombre de requêtes effectuées" >> gnuplot_script
echo 'set ylabel "Temps moyen d une requête (en ms)" ' >> gnuplot_script
echo "set xlabel 'Nombre de requête'" >> gnuplot_script
echo "set xr [$xmin:$xmax]" >> gnuplot_script
echo "set yr [$ymin:$ymax]" >> gnuplot_script
echo "set nokey" >> gnuplot_script
echo "set multiplot" >> gnuplot_script
echo "plot 'resR.txt' with lines lw 2 lc rgb \"red\" " >> gnuplot_script
#echo "plot 'resG.txt' with lines lw 2 lc rgb \"blue\"" >> gnuplot_script  
#echo "plot 'resB.txt' with lines lw 2 lc rgb \"green\"" >> gnuplot_script  

gnuplot gnuplot_script 
rm gnuplot_script 


# '#0072bd' # blue
# '#d95319' # orange
# '#edb120' # yellow
# '#7e2f8e' # purple
# '#77ac30' # green
# '#4dbeee' # light-blue
# '#a2142f' # red