vlib work
vlog hello.v
vlog tb.v
vsim -pli ../fakefpga.vpi -c -do "run -all" tb
