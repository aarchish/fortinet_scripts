print("Following script will add existing address objects to an exisitng address group or to a new address group");
existing_address_group = input("Do you want to add address-objects to a new address-group?(input 'true' if yes): ");
address_group_name = input("Enter address-group name: ");

ip = input("Enter input .txt file path: ");
inputFile = open(ip,"r");
op = input("Enter output file name with .txt (eg: output.txt) (new file will be created): ");
outputFile = open(op, "x");
object_comment = input("Comments for Firewall Object: ");
outputFile.writelines("config firewall addrgrp\n");
outputFile.writelines("edit "+address_group_name+"\n");

#member_line = "append member" if existing_address_group else "set member" ;
object_count = 0;

for line in inputFile:
    if(line.startswith('edit')):
        list = line.split(maxsplit=1)
        if(existing_address_group == 'true' and object_count == 0) : 
            outputFile.writelines("set member "+list[1]);
            object_count += 1;
        else : outputFile.writelines("append member "+list[1]);

outputFile.writelines("set comment "+object_comment+'\n');
outputFile.writelines("next\n");
outputFile.writelines("end\n");
outputFile.close();
inputFile.close();