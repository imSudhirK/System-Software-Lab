#open with default application 
xdg-open Lab.pdf      

#started saving works to filename.script 
script filename.script      
#script is done file is saved 
exit              

#create files 
touch lab1_1.txt lab1_2.doc lab1_3.odt   
#create directories one inside another 
mkdir -p assignment1/lab1      

#navigate forward backward and home commond 
cd  nextDir     
cd ..     
cd       

#copying content
cat iit.txt  >>lab1_1.txt >>lab1_2.doc >>lab1_3.odt     

#list only specific files 
ls *.txt *.doc *.odt        

# displays full path of present working directory 
pwd         

# create new file with editing option 
cat > commands.txt          

#making read write and executable file 
chmod +rwx commands.txt      

#dispalys first 11 lines of file 
head -11 filename     

#displays last 7 lines of file
tail -7 filename      

#copying file to another direcctory 
cp filename  destinationDir     

#moving file to another direcctory
mv filename  destinationDir      

#searching for string match in given file 
grep assignment lab1_1.txt       
#for specific word 
grep -w assignment1 lab1_1.txt   
#finding exact match of line 
grep -x "exact matching line" lab1_1.txt   
#recursive search to all directories and files 
grep -r  -w   wordToSearch *          
#counts the number of occurance 
grep -c word  filename     

# space 
df           

#s,m,h,d terminal timer for wait 
sleep 15s     
#time since system is on 
uptime         

#logged in users and their working time 
w      
#logged in users details 
finger 
#source of commands 
whereis     

#sources 
which  cpp python java    

#data received and sent speed 
ping -c 7  google.com    

# to downlaod from web link 
wget   url     

passwd
whoami
date
cal
id

#removing extra and adding Pre_ prefix to all files with .mp4 extention
rename 's/^extra/Pre_/' *.mp4   
#removing .webm and appending .mp4 suffix to all files with .webm extention
rename 's/.webm/.mp4/' *.webm   

# zip
tar -cvf newname.tar directory
# unzip
tar -xvf file.tar