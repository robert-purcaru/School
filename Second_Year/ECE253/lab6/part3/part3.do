# set the working dir, where all compiled verilog goes
vlib work

# compile all verilog modules in mux.v to working dir
# could also have multiple verilog files
vlog part3.v

#load simulation using mux as the top level simulation module
vsim part3

#log all signals and add some signals to waveform window
log {/*}
# add wave {/*} would add all items in top level simulation module
add wave {/*}
add wave {u1/*}
add wave {u2/*}

# first test case
#set input values using the force command, signal names need to be in {} brackets

force Clock 0 0ns, 1 1ns -r 2ns

force Go 0
force Resetn 0
run 2ns
force Resetn 1
run 2ns


force Divisor 2#0111
force Dividend 2#0001
force Go 0
run 2ns
force Go 1
run 2ns
force Go 0
run 100ns