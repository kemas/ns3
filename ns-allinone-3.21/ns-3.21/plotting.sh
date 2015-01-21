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
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d2_a4_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in scale-free service network' \
-x 0 0.5 1 1.5 \
-m black- -loc 2 -v simdata/plotfunceff_sf_a1_a4.json

python scratch/plot.py -e \
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in onential service network' \
-x 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 \
-m black- -loc 4 -v simdata/plotfunceff_sf_d2_d11.json

python scratch/plot.py -e \
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in onential service network' \
-x 1 1.5 2 2.5 3 3.5 4 \
-m black- -loc 4 -v simdata/plotfunceff_sf_d2_d8.json

python scratch/plot.py -e \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in exponential service network' \
-x 0 0.5 1 1.5 \
-m black- -loc 2 -v simdata/plotfunceff_exp_a1_a4.json

python scratch/plot.py -e \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in exponential service network' \
-x 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 \
-m black- -loc 4 -v simdata/plotfunceff_exp_d2_d11.json

python scratch/plot.py -e \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in exponential service network' \
-x 1 1.5 2 2.5 3 3.5 4 \
-m black- -loc 4 -v simdata/plotfunceff_exp_d2_d8.json

python scratch/plot.py -e \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in random service network' \
-x 0 0.5 1 1.5 \
-m black- -loc 2 -v simdata/plotfunceff_rand_a1_a4.json

python scratch/plot.py -e \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in random service network' \
-x 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 \
-m black- -loc 2 -v simdata/plotfunceff_rand_d2_d11.json

python scratch/plot.py -e \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of dependency $\langle dep \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of $\langle dep \rangle$ on cascading failure in random service network' \
-x 1 1.5 2 2.5 3 3.5 4 \
-m black- -loc 4 -v simdata/plotfunceff_rand_d2_d8.json

python scratch/plot.py -e \
    simdata/pwsvcsim_avg1_16.json \
    simdata/pwsvcsim_a2_avg1_16.json \
    simdata/pwsvcsim_a3_avg1_16.json \
    simdata/pwsvcsim_a4_avg1_16.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in ProgrammableWeb service network' \
-x 0 0.5 1 1.5 \
-m black- -loc 2 -v simdata/plotfunceff_pw_a1_a4.json

python scratch/plot.py -e \
    simdata/lgsvcsim_a1_avg1_16.json \
    simdata/lgsvcsim_a2_avg1_16.json \
    simdata/lgsvcsim_a3_avg1_16.json \
    simdata/lgsvcsim_a4_avg1_16.json \
-r 0.1 0.2 0.3 0.4 0.5 0.6 0.7 \
-l r=0.1 r=0.2 r=0.3 r=0.4 r=0.5 r=0.6 r=0.7 \
-xl 'Degree of alternative $\langle alt \rangle$' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'The effect of degree of alternative on cascading failure in scale-free service network' \
-x 0 0.5 1 1.5 \
-m black- -loc 2 -v simdata/plotfunceff_lg_a1_a4.json

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
python scratch/plot.py -di simdata/lg_comp.json -m black -logx 1 -logy 1 -t 'In-degree distribution of the Language Grid service network' -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$'
python scratch/plot.py -li simdata/pwsvcsim_1.json -m black -logx 1 -logy 1 -t 'In-degree distribution of ProgrammableWeb APIs' -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -lb 1.21
python scratch/plot.py -di simdata/rsvcsim_10k_10k_d3_a5_i10_1d.json -m black -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Exponential" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large
python scratch/plot.py -di simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json -m black -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Random" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a3_i10_5.json -m black- -logx 1 -logy 1 -xlim 1 500 -ylim 1e-6 1 -t "Scale-free" -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -axisfsize large
python scratch/plot.py -pl simdata/plotfunceff_all_a1_a4.json -m trifive- -t 'The effect of degree of alternative on cascading failure in service networks' -xl 'Degree of alternative $\langle alt \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random PW LG
python scratch/plot.py -pl simdata/plotfunceff_nolg_a1_a4.json -m trifive- -t 'The effect of $\langle alt \rangle$ on cascading failure in service networks' -xl 'Degree of alternative $\langle alt \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random PW
python scratch/plot.py -pl simdata/plotfunceff_tri_d2_d8.json -m trifive- -t 'The effect of $\langle dep \rangle$ on cascading failure in service networks' -xl 'Degree of dependency $\langle dep \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random -loc 2

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
-t 'Cascading failure with different $\langle{dep}\rangle$ on generated networks' \
-m tricol

# the effect of degree of dependency <dep> on cascading failure in color
python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
-xl 'Random failed services $n_r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different $\langle{dep}\rangle$ on generated networks' \
-m tricol \
-l 'sf, $\langle{dep}\rangle=1$' 'exp, $\langle{dep}\rangle=1$' 'rand, $\langle{dep}\rangle=1$' 'sf, $\langle{dep}\rangle=1.5$' 'exp, $\langle{dep}\rangle=1.5$' 'rand, $\langle{dep}\rangle=1.5$' 'sf, $\langle{dep}\rangle=2$' 'exp, $\langle{dep}\rangle=2$' 'rand, $\langle{dep}\rangle=2$' \
-loc 2 -axisfsize large -ylim 0.36
# set ncol = 3, prop size = 14, numpoints = 1

# the effect of degree of dependency <dep> on cascading failure in color
python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
-xl 'Random failed services $n_r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different $\langle{dep}\rangle$ on generated networks' \
-m tricol \
-l \
    'sf, $\langle{dep}\rangle=1$' \
    'sf, $\langle{dep}\rangle=1.5$' \
    'sf, $\langle{dep}\rangle=2$' \
    'exp, $\langle{dep}\rangle=1$' \
    'exp, $\langle{dep}\rangle=1.5$' \
    'exp, $\langle{dep}\rangle=2$' \
    'rand, $\langle{dep}\rangle=1$' \
    'rand, $\langle{dep}\rangle=1.5$' \
    'rand, $\langle{dep}\rangle=2$' \
-loc 2 -axisfsize large -ylim 0.36
# set ncol = 3, prop size = 14, numpoints = 1

#    simdata/svcsimn_10k_10k_d5_a1_i10_avg1_8.json \
#    simdata/expsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
#    simdata/randsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
#    simdata/svcsimn_10k_10k_d6_a1_i10_avg1_8.json \
#    simdata/expsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
#    simdata/randsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \

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

python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d2_a4_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
-xl 'Random failed services $n_r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different $\langle{alt}\rangle$ on generated networks' \
-m tricol \
-l 'sf, $\langle{alt}\rangle=0$' 'exp, $\langle{alt}\rangle=0$' 'rand, $\langle{alt}\rangle=0$' 'sf, $\langle{alt}\rangle=0.5$' 'exp, $\langle{alt}\rangle=0.5$' 'rand, $\langle{alt}\rangle=0.5$' 'sf, $\langle{alt}\rangle=1$' 'exp, $\langle{alt}\rangle=1$' 'rand, $\langle{alt}\rangle=1$' \
-loc 2 -axisfsize large -ylim 0.18
# set ncol = 3, prop size = 14, numpoints = 1

#    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
#    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
#    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \

python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d7_a1_i10_1.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_2.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_3.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_4.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_5.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_6.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_7.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_8.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 avg

python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d8_a1_i10_1.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_2.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_3.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_4.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_5.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_6.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_7.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_8.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 avg

python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d9_a1_i10_1.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_2.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_3.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_4.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_5.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_6.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_7.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_8.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 avg

python scratch/plot.py -fc \
    simdata/svcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/svcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-l 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 \
-m black- -loc 2

python scratch/plot.py -fc \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_1.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_2.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_3.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_4.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_5.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_6.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_7.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_8.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 avg -loc 4

python scratch/plot.py -fc \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-m tricol -l 2 3 4 5 6 7 8 9 10 11 -loc 4

python scratch/plot.py -fc \
    simdata/randsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a5_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a6_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a7_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a8_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a9_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a10_i10_avg1_8.json \
    simdata/randsvcsimn_10k_10k_d2_a11_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 9 10 11 -loc 2

python scratch/plot.py -fc \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_1.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_2.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_3.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_4.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_5.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_6.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_7.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_8.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 avg -loc 4

python scratch/plot.py -fc \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d3_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d4_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d5_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d6_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d7_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d8_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d9_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d10_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d11_a1_i10_avg1_8.json \
-m tricol -l 2 3 4 5 6 7 8 9 10 11 -loc 4

python scratch/plot.py -fc \
    simdata/expsvcsimn_10k_10k_d2_a1_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a2_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a3_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a4_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a5_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a6_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a7_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a8_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a9_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a10_i10_avg1_8.json \
    simdata/expsvcsimn_10k_10k_d2_a11_i10_avg1_8.json \
-m tricol -l 1 2 3 4 5 6 7 8 9 10 11 -loc 2

python scratch/plot.py -fc \
    simdata/pwsvcsim_avg1_8.json \
    simdata/pwsvcsim_avg9_16.json \
    simdata/pwsvcsim_a2_avg1_8.json \
    simdata/pwsvcsim_a3_avg1_8.json \
    simdata/pwsvcsim_a3_avg9_16.json \
    simdata/pwsvcsim_a4_avg1_8.json \
    simdata/pwsvcsim_a4_avg9_16.json \
-m tricol -l 1 1 2 3 3 4 4 -loc 2

python scratch/plot.py -fc \
    simdata/pwsvcsim_avg1_16.json \
    simdata/pwsvcsim_a2_avg1_16.json \
    simdata/pwsvcsim_a3_avg1_16.json \
    simdata/pwsvcsim_a4_avg1_16.json \
-m tricol -l 1  2  3  4 -loc 2 -j 500

python scratch/plot.py -fc \
    simdata/pwsvcsim_avg1_16.json \
    simdata/pwsvcsim_a2_avg1_16.json \
    simdata/pwsvcsim_a3_avg1_16.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different $\langle{alt}\rangle$ on real networks' \
-m green -j 500

python scratch/plot.py -fc \
    simdata/pwsvcsim_avg1_16.json \
    simdata/pwsvcsim_d2_avg1_16.json \
    simdata/pwsvcsim_d3_avg1_16.json \
    simdata/pwsvcsim_d4_avg1_16.json \
-m tricol -l 1 2 3 4 -loc 2 -j 500

python scratch/plot.py -fc \
    simdata/pwsvcsim_avg1_16.json \
    simdata/pwsvcsim_d2_avg1_16.json \
    simdata/pwsvcsim_d3_avg1_16.json \
-xl 'Random failed services $r$ (in fraction)' \
-yl 'Cascade failed services $n_c$ (in fraction)' \
-t 'Cascading failure with different $\langle{dep}\rangle$ on real networks' \
-m white -j 500

python scratch/plot.py -fc \
    simdata/lgsvcsim_avg1_16.json \
    simdata/lgsvcsim_a1_avg1_16.json \
    simdata/lgsvcsim_a2_avg1_16.json \
    simdata/lgsvcsim_a3_avg1_16.json \
    simdata/lgsvcsim_a4_avg1_16.json -j 10 \
-m tricol- -l a0 a1 a2 a3 a4 -loc 4

python scratch/plot.py -fc \
    simdata/lgsvcsim_avg1_16.json \
    simdata/lgsvcsim_a2_avg1_16.json \
    simdata/lgsvcsim_a3_avg1_16.json \
-m magenta -j 10

