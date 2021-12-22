To run the GUI, simply double-click the "run.bat" file in desim_win32/.
	
Troubleshooting:

 - Try shift+right-clicking in the desim_win32 folder and clicking
   "Open Command window here". Then, in that command window, type 
		run.bat
   This will let you see any error messages

 - If you get "invalid option --add-module" it's because your java 
   version is too old. At this point you have two options:
   
     1) Uninstall your old version of Java then install a new one
     
     2) Install a newer version of Java somewhere. Then, edit run.bat to
        have this as its first line (in other words, add this line to the
        start of run.bat):
        
			PATH C:\PATH\TO\NEWER\JAVA\INSTALLATION\bin;%PATH%
	    
	    (notice the "\bin" at the end of the Java path)






To run the demo, simpe double-click the "demo.bat" file in demo/.
	
Troubleshooting:

 - Try shift+right-clicking in the demo folder and clicking
   "Open Command window here". Then, in that command window, type 
		demo.bat
   This will let you see any error messages

 - If you get "could not open fakefpga.vpi" it's because your version of
   Modelsim is not compatible with the one I used to compile the demo.
   For reference, I compiled with Modelsim Intel FPGA Starter Edition
   10.5b 32-bit
 
 - If you get "Command not found: vlog" it's because you need to add 
   Modelsim to your path. Add the following line to the start of
   demo.bat:
   
		PATH  C:\PATH\TO\MODELSIM\INSTALLATION\win32_aloem:%PATH%
   
   (note: your folder may not say "win32_aloem" at the end, but it will
   definitely start with "win32")
 
 - Of course, make sure you've followed all the steps to get your 
   Modelsim license connected (if necessary)
