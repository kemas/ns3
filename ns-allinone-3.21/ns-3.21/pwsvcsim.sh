#!/bin/bash

./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_3.json'"
./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_4.json'"
./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_5.json'"
./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_6.json'"
./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_7.json'"
./waf --pyrun "scratch/svcsim.py --timefail=20000 --fjson='simdata/mashupsall_dictapis.json' --filename='simdata/pwsvcsim_8.json'"


