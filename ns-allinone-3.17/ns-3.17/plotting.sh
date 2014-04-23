# script to plot the simulation result data

# plotting preferential service network with <dep> = 1 <alt> = no alt, 1-5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a2_i10.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a4_i10.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a6_i10.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a8_i10.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a10_i10.json simdata/svcsim_10k_10k_d3_a11_i10.json -l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a2_i10.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a4_i10.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a6_i10.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a8_i10.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a10_i10.json simdata/svcsim_10k_10k_d3_a11_i10.json -l "No alt" "<alt>=0.5" "<alt>=1" "<alt>=1.5" "<alt>=2" "<alt>=2.5" "<alt>=3" "<alt>=3.5" "<alt>=4" "<alt>=4.5" "<alt>=5"

# plotting preferential service network with <alt> = 1, <dep> from 1 to 5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d4_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d6_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d8_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d10_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d4_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d6_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d8_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d10_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=1.5" "<dep>=2" "<dep>=2.5" "<dep>=3" "<dep>=3.5" "<dep>=4" "<dep>=4.5" "<dep>=5"

# plotting non-preferential service network with <dep> = 1 <alt> = no alt, 1-5
python scratch/plot.py -li simdata/rsvcsim_10k_10k_d3_a1_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a5_i10.json simdata/rsvcsim_10k_10k_d3_a7_i10.json simdata/rsvcsim_10k_10k_d3_a9_i10.json simdata/rsvcsim_10k_10k_d3_a11_i10.json -l "No alt" "<alt>=1" "<alt>=2" "<alt>=3" "<alt>=4" "<alt>=5"
python scratch/plot.py -f simdata/rsvcsim_10k_10k_d3_a1_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a5_i10.json simdata/rsvcsim_10k_10k_d3_a7_i10.json simdata/rsvcsim_10k_10k_d3_a9_i10.json simdata/rsvcsim_10k_10k_d3_a11_i10.json -l "No alt" "<alt>=1" "<alt>=2" "<alt>=3" "<alt>=4" "<alt>=5"

# plotting non-preferential service network with <alt> = 1, <dep> from 1 to 5
python scratch/plot.py -li simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d5_a3_i10.json simdata/rsvcsim_10k_10k_d7_a3_i10.json simdata/rsvcsim_10k_10k_d9_a3_i10.json simdata/rsvcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=2" "<dep>=3" "<dep>=4" "<dep>=5"
python scratch/plot.py -f simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d5_a3_i10.json simdata/rsvcsim_10k_10k_d7_a3_i10.json simdata/rsvcsim_10k_10k_d9_a3_i10.json simdata/rsvcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=2" "<dep>=3" "<dep>=4" "<dep>=5"

# plotting preferential vs non-preferential service network with <dep> = 1, <alt> = no alt, 1-5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a1_i10.json simdata/rsvcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/rsvcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/rsvcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/rsvcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a11_i10.json simdata/rsvcsim_10k_10k_d3_a11_i10.json -l "No alt" "No alt" "<alt>=1" "<alt>=1" "<alt>=2" "<alt>=2" "<alt>=3" "<alt>=3" "<alt>=4" "<alt>=4" "<alt>=5" "<alt>=5" -m sym
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a1_i10.json simdata/rsvcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/rsvcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/rsvcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/rsvcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a11_i10.json simdata/rsvcsim_10k_10k_d3_a11_i10.json -l "No alt" "No alt" "<alt>=1" "<alt>=1" "<alt>=2" "<alt>=2" "<alt>=3" "<alt>=3" "<alt>=4" "<alt>=4" "<alt>=5" "<alt>=5" -m sym

# plotting preferential vs non-preferential service network with <alt> = 1, <dep> from 1 to 5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/rsvcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/rsvcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/rsvcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10.json simdata/rsvcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=1" "<dep>=2" "<dep>=2" "<dep>=3" "<dep>=3" "<dep>=4" "<dep>=4" "<dep>=5" "<dep>=5" -m sym
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a3_i10.json simdata/rsvcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/rsvcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/rsvcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/rsvcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10.json simdata/rsvcsim_10k_10k_d11_a3_i10.json -l "<dep>=1" "<dep>=1" "<dep>=2" "<dep>=2" "<dep>=3" "<dep>=3" "<dep>=4" "<dep>=4" "<dep>=5" "<dep>=5" -m sym

# plotting preferential vs scale-free service network with <dep> = 1, <alt> from no alt, 1 to 5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a1_i10_4.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a3_i10_4.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a5_i10_4.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a7_i10_4.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a9_i10_4.json simdata/svcsim_10k_10k_d3_a11_i10.json simdata/svcsim_10k_10k_d3_a11_i10_4.json -l "<alt>=No alt" "<alt>=No alt" "<alt>=1" "<alt>=1" "<alt>=2" "<alt>=2" "<alt>=3" "<alt>=3" "<alt>=4" "<alt>=4" "<alt>=5" "<alt>=5" -m sym
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a1_i10.json simdata/svcsim_10k_10k_d3_a1_i10_4.json simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a3_i10_4.json simdata/svcsim_10k_10k_d3_a5_i10.json simdata/svcsim_10k_10k_d3_a5_i10_4.json simdata/svcsim_10k_10k_d3_a7_i10.json simdata/svcsim_10k_10k_d3_a7_i10_4.json simdata/svcsim_10k_10k_d3_a9_i10.json simdata/svcsim_10k_10k_d3_a9_i10_4.json simdata/svcsim_10k_10k_d3_a11_i10.json simdata/svcsim_10k_10k_d3_a11_i10_4.json -l "<alt>=No alt" "<alt>=No alt" "<alt>=1" "<alt>=1" "<alt>=2" "<alt>=2" "<alt>=3" "<alt>=3" "<alt>=4" "<alt>=4" "<alt>=5" "<alt>=5" -m sym

# plotting preferential vs scale-free service network with <alt> = 1, <dep> from 1 to 5
python scratch/plot.py -li simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a3_i10_4.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10_4.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10_4.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10_4.json simdata/svcsim_10k_10k_d11_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10_4.json -l "<dep>=1" "<dep>=1" "<dep>=2" "<dep>=2" "<dep>=3" "<dep>=3" "<dep>=4" "<dep>=4" "<dep>=5" "<dep>=5" -m sym
python scratch/plot.py -f simdata/svcsim_10k_10k_d3_a3_i10.json simdata/svcsim_10k_10k_d3_a3_i10_4.json simdata/svcsim_10k_10k_d5_a3_i10.json simdata/svcsim_10k_10k_d5_a3_i10_4.json simdata/svcsim_10k_10k_d7_a3_i10.json simdata/svcsim_10k_10k_d7_a3_i10_4.json simdata/svcsim_10k_10k_d9_a3_i10.json simdata/svcsim_10k_10k_d9_a3_i10_4.json simdata/svcsim_10k_10k_d11_a3_i10.json simdata/svcsim_10k_10k_d11_a3_i10_4.json -l "<dep>=1" "<dep>=1" "<dep>=2" "<dep>=2" "<dep>=3" "<dep>=3" "<dep>=4" "<dep>=4" "<dep>=5" "<dep>=5" -m sym

