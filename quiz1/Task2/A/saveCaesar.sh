#! /bin/bash 

read cipher 

printf A' '; echo $cipher 
printf B' '; echo $cipher | tr "[A-Z]" "[ZA-Y]"
printf C' '; echo $cipher | tr "[A-Z]" "[Y-ZA-Y]"
printf D' '; echo $cipher | tr "[A-Z]" "[X-ZA-X]"
printf E' '; echo $cipher | tr "[A-Z]" "[W-ZA-W]"
printf F' '; echo $cipher | tr "[A-Z]" "[V-ZA-V]"
printf G' '; echo $cipher | tr "[A-Z]" "[U-ZA-U]"
printf H' '; echo $cipher | tr "[A-Z]" "[T-ZA-T]"
printf I' '; echo $cipher | tr "[A-Z]" "[S-ZA-S]"
printf J' '; echo $cipher | tr "[A-Z]" "[R-ZA-R]"
printf K' '; echo $cipher | tr "[A-Z]" "[Q-ZA-Q]"
printf L' '; echo $cipher | tr "[A-Z]" "[P-ZA-P]"
printf M' '; echo $cipher | tr "[A-Z]" "[O-ZA-O]"
printf N' '; echo $cipher | tr "[A-Z]" "[N-ZA-N]"
printf O' '; echo $cipher | tr "[A-Z]" "[M-ZA-M]"
printf P' '; echo $cipher | tr "[A-Z]" "[L-ZA-L]"
printf Q' '; echo $cipher | tr "[A-Z]" "[K-ZA-K]"
printf R' '; echo $cipher | tr "[A-Z]" "[J-ZA-J]"
printf S' '; echo $cipher | tr "[A-Z]" "[I-ZA-I]"
printf T' '; echo $cipher | tr "[A-Z]" "[H-ZA-H]"
printf U' '; echo $cipher | tr "[A-Z]" "[G-ZA-G]"
printf V' '; echo $cipher | tr "[A-Z]" "[F-ZA-F]"
printf W' '; echo $cipher | tr "[A-Z]" "[E-ZA-E]"
printf X' '; echo $cipher | tr "[A-Z]" "[D-ZA-D]"
printf Y' '; echo $cipher | tr "[A-Z]" "[C-ZA-C]"
printf Z' '; echo $cipher | tr "[A-Z]" "[B-ZA]"

