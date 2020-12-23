#! /bin/bash

# downloading file from Internet
wget -O temp.txt http://reqres.in/api/users?page=1

#extracting first names and last names
first_names=($(grep -Po 'first_name":"\K.*?(?=")' temp.txt))
last_names=($(grep -Po 'last_name":"\K.*?(?=")' temp.txt))

# output to file and on the screen
for ((i=0; i<${#first_names[@]}; i++)); do echo "${first_names[$i]} ${last_names[$i]}" ; done | shuf | tee ~/output.txt
