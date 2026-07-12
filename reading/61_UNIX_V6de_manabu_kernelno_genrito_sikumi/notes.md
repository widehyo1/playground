https://simh.trailing-edge.com/

```bash
~/gitclone/playground/reading/61_UNIX_V6de_manabu_kernelno_genrito_sikumi/v6/sim $ make all
~/gitclone/playground/reading/61_UNIX_V6de_manabu_kernelno_genrito_sikumi/v6/sim/BIN $ ls
altair  buildtools  eclipse  gri  h316  i1401  i1620  i7094  id16  id32  lgp  nova  pdp1  pdp10  pdp11  pdp15  pdp4  pdp7  pdp8  pdp9  sds  sigma  uc15  vax  vax780
~/gitclone/playground/reading/61_UNIX_V6de_manabu_kernelno_genrito_sikumi/v6/sim/BIN $ ./pdp11

PDP-11 simulator V3.12-5
sim>
```

https://gunkies.org/wiki/Installing_UNIX_v6_(PDP-11)_on_SIMH

https://sourceforge.net/projects/bsd42/files/Install%20tapes/Research%20Unix/Unix-v6-Ken-Wellsch.tap.bz2/download



```bash
~/gitclone/playground/reading/61_UNIX_V6de_manabu_kernelno_genrito_sikumi/v6/sim/BIN $ ./pdp11

PDP-11 simulator V3.12-5
sim> set cpu 11/40
Disabling XQ
sim> set tm0 locked
sim> attach tm0 Unix-v6-Ken-Wellsch.tap
sim> attach rk0 rk0
RK: creating new file
sim> attach rk1 rk1
sim> attach rk2 rk2
sim> d cpu 100000 012700
sim> d cpu 100002 172526
sim> d cpu 100004 010040
sim> d cpu 100006 012740
sim> d cpu 100010 060003
sim> d cpu 100012 000777
sim> g 100000

Simulation stopped, PC: 100012 (BR 100012)
sim> g 0
=tmrk
disk offset
0
tape offset
100
count
1
=tmrk
disk offset
1
tape offset
101
count
3999
=
Simulation stopped, PC: 137274 (TSTB @#177560)
sim> q
Goodbye
```
