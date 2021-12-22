# set the working dir, where all compiled verilog goes
vlib work

# compile all verilog modules in mux.v to working dir
# could also have multiple verilog files
vlog part2_alex.v

#load simulation using mux as the top level simulation module
vsim part2

#log all signals and add some signals to waveform window
log {/*}
# add wave {/*} would add all items in top level simulation module
add wave {/*}

# first test case
#set input values using the force command, signal names need to be in {} brackets

force Clock 0 0ns, 1 1ns -r 2ns

force Resetn 0
run 2ns
force Resetn 1
run 2ns 

force DataIn 2#00000001
force Go 0
run 2ns
force Go 1
run 2ns

force DataIn 2#00000010
force Go 0
run 2ns
force Go 1
run 2ns

force DataIn 2#00000011
force Go 0
run 2ns
force Go 1
run 2ns

force DataIn 2#00000100
force Go 0
run 2ns
force Go 1
run 2ns

force Go 0
run 2ns
force Go 1
run 2ns

run 30ns

