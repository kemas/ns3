# script to plot the simulation result data

# plotting scale-free network with <dep> = 1 <alt> = no alt, 1-5
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
-l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"

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
-l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"

python scratch/plot.py -f \
    simdata/svcsim_10k_10k_d3_a8_i10.json \
    simdata/svcsim_10k_10k_d3_a8_i10_2.json \
    simdata/svcsim_10k_10k_d3_a8_i10_3.json \
    simdata/svcsim_10k_10k_d3_a8_i10_4.json \
    simdata/svcsim_10k_10k_d3_a8_i10_avg1_4.json \

# plotting scale-free network with <alt> = 1, <dep> from 1 to 5
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
-l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"

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
-l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"

# plotting exponential network with <dep> = 1 <alt> = no alt, 1-5
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
-l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"

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
-l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"

# plotting exponential network with <alt> = 1, <dep> from 1 to 5
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
-l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"

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
-l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"

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
-l "No alt" "No alt" "<alt>=0.5" "<alt>=0.5" "<alt>=1" "<alt>=1" "<alt>=1.5" "<alt>=1.5" "<alt>=2" "<alt>=2" \
    "<alt>=2.5" "<alt>=2.5" "<alt>=3" "<alt>=3" "<alt>=3.5" "<alt>=3.5" "<alt>=4" "<alt>=4" "<alt>=4.5" "<alt>=4.5" "<alt>=5" "<alt>=5" \
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
-l "<dep>=1" "<dep>=1" "<dep>=1.5" "<dep>=1.5" "<dep>=2" "<dep>=2" "<dep>=2.5" "<dep>=2.5" "<dep>=3" "<dep>=3" \
    "<dep>=3.5" "<dep>=3.5" "<dep>=4" "<dep>=4" "<dep>=4.5" "<dep>=4.5" "<dep>=5" "<dep>=5" \
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
-xl "Number of nodes fail randomly (fraction)" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "Cascading failure in service networks with different degree of alternative <alt>" \
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
-xl "Number of nodes fail randomly (fraction)" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "Cascading failure in service networks with different degree of dependency <dep>" \
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
-xl "Degree of alternative <alt>" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "The effect of degree of alternative on cascading failure in scale-free service network" \
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
-xl "Degree of dependency <dep>" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "The effect of degree of dependency on cascading failure in scale-free service network" \
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
-xl "Degree of alternative <alt>" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "The effect of degree of alternative on cascading failure in exponential service network" \
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
-xl "Degree of dependency <dep>" \
-yl "Number of cascaded fail nodes (fraction)" \
-t "The effect of degree of dependency on cascading failure in exponential service network" \
-x 1 1.5 2 2.5 3 3.5 4 4.5 \
-m black- -loc 2

