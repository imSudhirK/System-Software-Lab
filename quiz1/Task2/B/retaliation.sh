#! /bin/bash 

read cipher   

case "$1" in 
     A) 
        echo $cipher
         ;;
     Z) 
        echo $cipher | tr "[A-Z]" "[ZA-Y]"
         ;;
     Y)
        echo $cipher | tr "[A-Z]" "[Y-ZA-Y]"
         ;;
     X)
        echo $cipher | tr "[A-Z]" "[X-ZA-X]"
         ;;
     W)
        echo $cipher | tr "[A-Z]" "[W-ZA-W]"
         ;;
     U)
        echo $cipher | tr "[A-Z]" "[V-ZA-V]"
         ;;
     U)
        echo $cipher | tr "[A-Z]" "[U-ZA-U]"
         ;;
     T) 
        echo $cipher | tr "[A-Z]" "[T-ZA-T]"
         ;;
     S)
        echo $cipher | tr "[A-Z]" "[S-ZA-S]"
         ;;
     R)
        echo $cipher | tr "[A-Z]" "[R-ZA-R]"
         ;;
     Q)
        echo $cipher | tr "[A-Z]" "[Q-ZA-Q]"
         ;;
     P)
        echo $cipher | tr "[A-Z]" "[P-ZA-P]"
         ;;
     O)
        echo $cipher | tr "[A-Z]" "[O-ZA-O]"
         ;;
     N)
        echo $cipher | tr "[A-Z]" "[N-ZA-N]"
         ;;
     M)
        echo $cipher | tr "[A-Z]" "[M-ZA-M]"
         ;;
     L)
        echo $cipher | tr "[A-Z]" "[L-ZA-L]"
         ;;
     K)
        echo $cipher | tr "[A-Z]" "[K-ZA-K]"
         ;;
     J)
        echo $cipher | tr "[A-Z]" "[J-ZA-J]"
          ;;
     I)
        echo $cipher | tr "[A-Z]" "[I-ZA-I]"
          ;;
     H)
        echo $cipher | tr "[A-Z]" "[H-ZA-H]"
          ;;
     G)
        echo $cipher | tr "[A-Z]" "[G-ZA-G]"
          ;;
     F)
        echo $cipher | tr "[A-Z]" "[F-ZA-F]"
          ;;
     E)
        echo $cipher | tr "[A-Z]" "[E-ZA-E]"
          ;;
     D)
        echo $cipher | tr "[A-Z]" "[D-ZA-D]"
          ;;
     C)
        echo $cipher | tr "[A-Z]" "[C-ZA-C]"
          ;;
     B)
        echo $cipher | tr "[A-Z]" "[B-ZA]"
          ;;
esac

