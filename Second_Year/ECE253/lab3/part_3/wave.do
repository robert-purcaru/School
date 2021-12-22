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

# first test case
#set input values using the force command, signal names need to be in {} brackets

force {A} 2#1110
force {B} 2#1111
force {Function} 2#000
run 10ns

force {Function} 2#001
run 10ns

force {Function} 2#010
run 10ns

force {Function} 2#011
run 10ns

force {Function} 2#100
run 10ns

force {Function} 2#101
run 10ns

force {Function} 2#110
run 10ns

force {Function} 2#111
run 10ns

force {A} 2#0000
force {B} 2#0000
force {Function} 2#000
run 10ns

force {Function} 2#001
run 10ns

force {Function} 2#010
run 10ns

force {Function} 2#011
run 10ns

force {Function} 2#100
run 10ns

force {Function} 2#101
run 10ns

force {Function} 2#110
run 10ns

force {Function} 2#111
run 10ns

force {A} 2#0000
force {B} 2#1111
force {Function} 2#000
run 10ns

force {Function} 2#001
run 10ns

force {Function} 2#010
run 10ns

force {Function} 2#011
run 10ns

force {Function} 2#100
run 10ns

force {Function} 2#101
run 10ns

force {Function} 2#110
run 10ns

force {Function} 2#111
run 10ns

force {A} 2#0101
force {B} 2#1010
force {Function} 2#000
run 10ns

force {Function} 2#001
run 10ns

force {Function} 2#010
run 10ns

force {Function} 2#011
run 10ns

force {Function} 2#100
run 10ns

force {Function} 2#101
run 10ns

force {Function} 2#110
run 10ns

force {Function} 2#111
run 10ns

force {A} 2#1111
force {B} 2#1111
force {Function} 2#000
run 10ns

force {Function} 2#001
run 10ns

force {Function} 2#010
run 10ns

force {Function} 2#011
run 10ns

force {Function} 2#100
run 10ns

force {Function} 2#101
run 10ns

force {Function} 2#110
run 10ns

force {Function} 2#111
run 10ns