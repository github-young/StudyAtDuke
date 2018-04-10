set term pdf enh color solid
set output 'transfer.pdf'
datafile = 'IdVg.txt'

#set logscale y
set grid

set title 'transfer curve'
set xlabel 'V_{gs}'
set ylabel 'I_d'

plot datafile using 1:2 w lp notitle 