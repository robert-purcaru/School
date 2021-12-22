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


force ClockIn 0 0ns, 1 10ns -r 20ns

run 20ns
force Reset 1
run 20ns
force Reset 0
run 20ns

force Speed 2#00

run 500ns

force Speed 2#01

run 15000ns


force Speed 2#10

run 100000ns

force Reset 1

run 10000ns