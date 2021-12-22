# set the working dir, where all compiled verilog goes
vlib work

# compile all verilog modules in mux.v to working dir
# could also have multiple verilog files
vlog part2.v

#load simulation using mux as the top level simulation module
vsim part2

#log all signals and add some signals to waveform window
log {/*}
# add wave {/*} would add all items in top level simulation module
add wave {/*}

# first test case
#set input values using the force command, signal names need to be in {} brackets


force {Clock} 0 
force {Reset_b} 0
run 20ns
force {Clock} 1
run 20ns

force Clock 0
force {Reset_b} 1
run 20ns

force {Data} 2#0001
force {Function} 2#000
force Clock 1
run 20ns

force Clock 0
run 20ns

force {Data} 2#1110
force {Function} 2#000
force Clock 1
run 20ns


force Clock 0
force {Data} 2#1111
force {Function} 2#000
run 20ns

force Clock 1
run 20ns
