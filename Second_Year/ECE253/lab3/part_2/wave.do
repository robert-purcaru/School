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

force {a} 2#1111
forc {b} 2#1110
force {c_in} 0
run 10ns

force {a} 2#0000
forc {b} 2#0000
force {c_in} 1
run 10ns

force {a} 2#0011
forc {b} 2#0011
force {c_in} 1
run 10ns

force {a} 2#0100
forc {b} 2#0100
force {c_in} 1
run 10ns

force {a} 2#1111
forc {b} 2#1111
force {c_in} 1
run 10ns

force {a} 2#0000
forc {b} 2#0000
force {c_in} 0
run 10ns

