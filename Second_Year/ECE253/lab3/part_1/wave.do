# set the working dir, where all compiled verilog goes
vlib work

# compile all verilog modules in mux.v to working dir
# could also have multiple verilog files
vlog part1.v

#load simulation using mux as the top level simulation module
vsim part1

#log all signals and add some signals to waveform window
log {/*}
# add wave {/*} would add all items in top level simulation module
add wave {/*}

# first test case
#set input values using the force command, signal names need to be in {} brackets
force {Input[0]} 0 0ns, 1 {5ns} -r 10ns
force {Input[1]} 0 0ns, 1 {10ns} -r 20ns
force {Input[2]} 0 0ns, 1 {20ns} -r 40ns
force {Input[3]} 0 0ns, 1 {40ns} -r 80ns
force {Input[4]} 0 0ns, 1 {80ns} -r 160ns
force {Input[5]} 0 0ns, 1 {160ns} -r 320ns
force {Input[6]} 0 0ns, 1 {320ns} -r 640ns

force {MuxSelect[0]} 0 0ns, 1 {5ns} -r 10ns
force {MuxSelect[1]} 0 0ns, 1 {10ns} -r 20ns
force {MuxSelect[2]} 0 0ns, 1 {20ns} -r 40ns

#run simulation for a few ns
run 800ns


