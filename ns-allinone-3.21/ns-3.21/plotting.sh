# script to plot the simulation result data

# plotting scale-free network with $\langle dep \rangle$ = 1 $\langle alt \rangle$ = no alt, 1-5
python scratch/plot.py -li \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a11_i10_avg1_4.json \
-l 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5'

python scratch/plot.py -f \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a11_i10_avg1_4.json \
-l 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5'

#python scratch/plot.py -f \
#    simdata/svcsim_10k_10k_d3_a8_i10.json \
#    simdata/svcsim_10k_10k_d3_a8_i10_2.json \
#    simdata/svcsim_10k_10k_d3_a8_i10_3.json \
#    simdata/svcsim_10k_10k_d3_a8_i10_4.json \
#    simdata/svcsim_10k_10k_d3_a8_i10_avg1_4.json \

# plotting scale-free network with $\langle alt \rangle$ = 1, $\langle dep \rangle$ from 1 to 5
python scratch/plot.py -li \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d7_a3_i10_avg23456.json \
    simdata/svcsim_10k_10k_d8_a3_i10_avg1456.json \
    simdata/svcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d11_a3_i10_avg12346.json \
-l '$\langle dep \rangle$=1' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=3' '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=5'

python scratch/plot.py -f \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d7_a3_i10_avg23456.json \
    simdata/svcsim_10k_10k_d8_a3_i10_avg1456.json \
    simdata/svcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d11_a3_i10_avg12346.json \
-l '$\langle dep \rangle$=1' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=3' '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=5'

# plotting exponential network with $\langle dep \rangle$ = 1 $\langle alt \rangle$ = no alt, 1-5
python scratch/plot.py -li \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a11_i10_avg1_4.json \
-l 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5'

python scratch/plot.py -f \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a11_i10_avg1_4.json \
-l 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5'

# plotting exponential network with $\langle alt \rangle$ = 1, $\langle dep \rangle$ from 1 to 5
python scratch/plot.py -li \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d7_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d8_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d11_a3_i10_avg1_4.json \
-l '$\langle dep \rangle$=1' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=3' '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=5'

python scratch/plot.py -f \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d7_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d8_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d11_a3_i10_avg1_4.json \
-l '$\langle dep \rangle$=1' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=3' '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=5'

# scale-free vs exponential
python scratch/plot.py -f \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a10_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a11_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a11_i10_avg1_4.json \
-l 'No alt' 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2' \
    '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5' '$\langle alt \rangle$=5' \
-m sym

python scratch/plot.py -f \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d7_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d7_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d8_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d8_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d10_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d11_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d11_a3_i10_avg1_4.json \
-l '$\langle dep \rangle$=1' '$\langle dep \rangle$=1' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=1.5' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=2.5' '$\langle dep \rangle$=3' '$\langle dep \rangle$=3' \
    '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=3.5' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=4.5' '$\langle dep \rangle$=5' '$\langle dep \rangle$=5' \
-m sym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-m sym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m sym

python scratch/plot.py -e \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d3_a10_i10_avg1_6.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in scale-free service network' \
-x 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 1

python scratch/plot.py -e \
    simdata/svcsim_10k_10k_d3_a3_i10_avg268910.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1456.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/svcsim_10k_10k_d7_a3_i10_avg23456.json \
    simdata/svcsim_10k_10k_d8_a3_i10_avg1567.json \
    simdata/svcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/svcsim_10k_10k_d10_a3_i10_avg1_6.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of dependency on cascading failure in scale-free service network' \
-x 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 2

python scratch/plot.py -e \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a6_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a7_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a8_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a9_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a10_i10_avg1_6.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in exponential service network' \
-x 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 1

python scratch/plot.py -e \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d7_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d8_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d10_a3_i10_avg1_6.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of dependency on cascading failure in exponential service network' \
-x 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 2

python scratch/plot.py -e \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a6_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a7_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a8_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a9_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a10_i10_1d.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in random service network' \
-x 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 1

python scratch/plot.py -e \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d7_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d8_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d9_a3_i10_1d.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of dependency on cascading failure in random service network' \
-x 1 1.5 2 2.5 3 3.5 4 \
-m black- -loc 2

## the effect of degree of dependency in exponential network
#python scratch/plot.py -e \
#    simdata/rsvcsim_10k_10k_d3_a3_i10_1d.json \
#    simdata/rsvcsim_10k_10k_d4_a3_i10_1d.json \
#    simdata/rsvcsim_10k_10k_d5_a3_i10_1d.json \
#    simdata/rsvcsim_10k_10k_d6_a3_i10_1d.json \
#    simdata/rsvcsim_10k_10k_d7_a3_i10_1d.json \
#    simdata/rsvcsim_10k_10k_d8_a3_i10_avg1_6.json \
#    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
#-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
#-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
#-xl 'Degree of dependency $\langle dep \rangle$' \
#-yl 'Cascade failed services $n_c$ (in fraction)' \
#-t 'The effect of degree of dependency on cascading failure in exponential service network' \
#-x 1 1.5 2 2.5 3 3.5 4 4.5 \
#-m black- -loc 2

#python scratch/plot.py -e \
#    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
#    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a6_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a7_i10_avg1_4.json \
#    simdata/svcsim_10k_10k_d3_a8_i10_avg1_6.json \
#    simdata/svcsim_10k_10k_d3_a9_i10_avg1_6.json \
#    simdata/svcsim_10k_10k_d3_a10_i10_avg1_6.json \
#-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
#-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
#-xl 'Degree of alternative $\langle alt \rangle$' \
#-yl 'Cascade failed services $n_c$ (in fraction)' \
#-t 'The effect of degree of alternative on cascading failure in scale-free service network' \
#-x 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 \
#-m black- -loc 1

# plotting random network with $\langle dep \rangle$ = 1 $\langle alt \rangle$ = no alt, 1-5
python scratch/plot.py -li \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a6_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a7_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a8_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a9_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a10_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a11_i10_1d.json \
-l 'No alt' '$\langle alt \rangle$=0.5' '$\langle alt \rangle$=1' '$\langle alt \rangle$=1.5' '$\langle alt \rangle$=2' '$\langle alt \rangle$=2.5' '$\langle alt \rangle$=3' '$\langle alt \rangle$=3.5' '$\langle alt \rangle$=4' '$\langle alt \rangle$=4.5' '$\langle alt \rangle$=5' \
-m var

# scale-free vs random network
python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-m sym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m sym

# exponential vs random network
python scratch/plot.py -fc \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-m sym

python scratch/plot.py -fc \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m sym

# scale-free vs exponential vs random network
python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-l scale-free exponential random \
-m white -loc 4

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_avg1_6.json \
    simdata/randsvcsim_10k_10k_d9_a3_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-l scale-free exponential random \
-m white -loc 4

#python scratch/plot.py -fc \
#    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
#    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
#    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
#    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
#    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
#    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
#    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
#    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
#    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
#    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
#    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
#    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
#    simdata/svcsim_10k_10k_d3_a5_i10_avg1_4.json \
#    simdata/rsvcsim_10k_10k_d3_a5_i10_avg1_4.json \
#    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
#-xl 'Random failed services $r$ (in fraction)' \
#-yl 'Cascade failed services $n_c$ (in fraction)' \
#-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
#-m trisym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg268910.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-m trisym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m trisym

python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d4_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d4_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d4_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d5_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d5_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d5_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d6_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d6_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d6_a1_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m trisym

# depth scale-free
python scratch/plot.py -pd \
    simdata/svcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a5_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a6_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a7_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a8_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a9_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a10_i10_1d.json \
-s simdata/depth_sf_altvar.csv

python scratch/plot.py -pd \
    simdata/svcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d6_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d7_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d8_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d9_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d10_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d11_a3_i10_1d.json \
-s simdata/depth_sf_depvar.csv

# depth exponential
python scratch/plot.py -pd \
    simdata/rsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a5_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a6_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a7_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a8_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a9_i10_1d.json \
    simdata/rsvcsim_10k_10k_d3_a10_i10_1d.json \
-s simdata/depth_exp_altvar.csv

python scratch/plot.py -pd \
    simdata/rsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d7_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d8_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d9_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d10_a3_i10_1d.json \
    simdata/rsvcsim_10k_10k_d11_a3_i10_1d.json \
-s simdata/depth_exp_depvar.csv

# depth random
python scratch/plot.py -pd \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a6_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a7_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a8_i10_1d.json \
    simdata/randsvcsim_10k_10k_d3_a9_i10_1d.json \
-s simdata/depth_rand_altvar.csv

python scratch/plot.py -pd \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d7_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d8_a3_i10_1d.json \
    simdata/randsvcsim_10k_10k_d9_a3_i10_1d.json \
-s simdata/depth_rand_depvar.csv

python scratch/plot.py -pl simdata/plotfunceff.json -m black- -t 'The effect of degree of dependency on cascading failure in service networks' -xl 'Degree of dependency $\langle dep \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random -loc 2
# color
python scratch/plot.py -pl simdata/plotfunceff.json -m tricol- -t 'The effect of degree of dependency on cascading failure in service networks' -xl 'Degree of dependency $\langle dep \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random -loc 2
python scratch/plot.py -pl simdata/plotfunceffalt.json -m black- -t 'The effect of degree of alternative on cascading failure in service networks' -xl 'Degree of alternative $\langle alt \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random
# color
python scratch/plot.py -pl simdata/plotfunceffalt.json -m tricol- -t 'The effect of degree of alternative on cascading failure in service networks' -xl 'Degree of alternative $\langle alt \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random
python scratch/plot.py -di simdata/lg_comp.json -m black -logx 1 -logy 1 -t 'Degree distribution of the Language Grid service network' -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$'
python scratch/plot.py -di simdata/rsvcsim_10k_10k_d3_a5_i10_1d.json -m black -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Exponential" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large
python scratch/plot.py -di simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json -m black -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Random" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a3_i10_5.json -m black- -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Scale-free" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large

# the effect of degree of dependency <dep> on cascading failure in color
python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a3_i10_avg1_6.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d4_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d4_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d5_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d5_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d6_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d6_a3_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of dependency $\langle dep \rangle$' \
-m tricol

# the effect of degree of alternative <alt> on cascading failure in color
python scratch/plot.py -fc \
    simdata/svcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a1_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a1_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a2_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a2_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a3_i10_avg268910.json \
    simdata/rsvcsim_10k_10k_d3_a3_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a3_i10_1d.json \
    simdata/svcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/rsvcsim_10k_10k_d3_a4_i10_avg1_4.json \
    simdata/randsvcsim_10k_10k_d3_a4_i10_1d.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different degree of alternative $\langle alt \rangle$' \
-m tricol

### check degree distribution
python scratch/plot.py -li \
    simdata/svcsimn_10k_10k_d2_a1_i10_1.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_2.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_3.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_4.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_5.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_6.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_7.json \
    simdata/svcsimn_10k_10k_d2_a1_i10_8.json \
-m black-
