#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main(int argc, char* argv[]){

        // key fields to parse
        const int numFields = 7;
        const std::string fields[numFields] = {     
                "byr",  // birth year
                "iyr",  // issue year
                "eyr",  // expiration year
                "hgt",  // height
                "hcl",  // hair color
                "ecl",  // eye color
                "pid"  // passport id
                //"cid"   // country id
        };

        int entries = 0;        // number of total entries in the file
        int valid = 0;          // number of inputs containing all fields w/ valid entries

        // filename is a command line input
        const char* inFileName = argv[1];
        //std::cout << inFileName << '\n';

        std::fstream inFile(inFileName);

        // once file is confirmed to open, start the process
        if(inFile.is_open()){

                // no fields found to start
                std::string line;
                std::vector<std::string> tokens;
                std::vector<std::string> keys;
                std::vector<bool> matched;
                bool found = false;
                bool isValid = true;

                std::size_t pos;
                while(getline(inFile,line)){

                        // while the line is not empty, read into tokens
                        //std::cout << "Line size = " << line.size() << '\n'; 
                        if(line.size()<=0){
                                
                                // on empty line, parse gathered tokens
                                for(int i=0;i<tokens.size();++i){
                                        
                                        // take a single token and parse
                                        pos = tokens[i].find(':');
                                        keys.push_back(tokens[i].substr(0,pos));
                                        std::cout << keys[i] << ' ';
                                        tokens[i].erase(0,pos+1);
                                        
                                        matched.push_back(false);
                                }
                               
                                // once tokens have been parsed,
                                // go through each field to see if a key matches
                                std::cout << '\n' << entries+1 << ": ";
                                for(int i=0;i<numFields;++i){
                                        std::cout << fields[i] << ' ';
                                        found = false;
                                        for(int j=0;j<keys.size();++j){
                                                if(!matched[j]){
                                                        if(keys[j].compare(fields[i]) == 0){
                                        switch( std::stoi(keys[j]) ){
                                                case std::stoi("byr"):
                                                        if( tokens[j].size() != 4
                                                                || std::stoi(tokens[j]) < 1920
                                                                || std::stoi(tokens[j]) > 2002 ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("iyr"):
                                                        if( tokens[j].size() != 4
                                                                || std::stoi(tokens[j]) < 2010
                                                                || std::stoi(tokens[j]) > 2020 ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("eyr"):
                                                        if( tokens[j].size() != 4
                                                                || std::stoi(tokens[j]) < 2020
                                                                || std::stoi(tokens[j]) > 2030 ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("hgt"):
                                                        if(
                                                          ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("hcl"):
                                                        bool badChar = false;
                                                        

                                                        if( tokens[j][0] != '#'
                                                                || tokens[j].size() != 7
                                                                || badChar
                                                          ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("ecl"):
                                                        if(
                                                          ){
                                                                isValid = false;
                                                        }
                                                        break;
                                                case std::stoi("pid"):
                                                        if(
                                                          ){
                                                                isValid = false;
                                                        }
                                                        break;
                                        }
                                                                if(isValid){ 
                                                                        matched[j] = true; 
                                                                        found = true;
                                                                }
                                                                break;
                                                        }
                                                }
                                        }
                                        if(found) continue;
                                        else{ 
                                                std::cout << "\nNot valid!";
                                                isValid = false;
                                                break;
                                        }
                                } 

                                // if a key was found for each field,
                                // increment counter 
                                if(isValid) ++valid;
                                
                                // either way, clear the temp tokens and reset for next entry
                                std::cout << "\nValid so far = " << valid << "\n\n";
                                ++entries;
                                tokens.clear();
                                keys.clear();
                                matched.clear();
                                isValid = true;
                                continue;
                        }

                        // when the line isn't empty, read in raw tokens
                        while(true){
                                
                                pos = line.find(' ');
                                //std::cout << pos << '\n';
                                
                                // if mutiple tokens, pick first
                                if(pos!=std::string::npos){
                                        
                                        // record first token, and erase from line
                                        tokens.push_back( line.substr(0,pos+1) );
                                        line.erase(0,pos+1);
                                }else{
                                        // last token on line
                                        tokens.push_back( line );
                                        break;
                                }
                        }
                }
                // parse the last entry
                for(int i=0;i<tokens.size();++i){
                        
                        // take a single token and parse
                        pos = tokens[i].find(':');
                        keys.push_back(tokens[i].substr(0,pos));
                        std::cout << keys[i] << ' ';
                        tokens[i].erase(0,pos+1);
                        
                        matched.push_back(false);
                }
               
                // once tokens have been parsed,
                // go through each field to see if a key matches
                std::cout << '\n' << entries+1 << ": ";
                for(int i=0;i<numFields;++i){
                        std::cout << fields[i] << ' ';
                        found = false;
                        for(int j=0;j<keys.size();++j){
                                if(!matched[j]){
                                        if(keys[j].compare(fields[i]) == 0){
                                                matched[j] = true; 
                                                found = true;
                                                break;
                                        }
                                }
                        }
                        if(found) continue;
                        else{ 
                                std::cout << "\nNot valid!";
                                isValid = false;
                                break;
                        }
                } 

                // if a key was found for each field,
                // increment counter 
                if(isValid) ++valid;
                
                // either way, clear the temp tokens and reset for next entry
                std::cout << "\nValid so far = " << valid << "\n\n";
                ++entries;
                tokens.clear();
                keys.clear();
                matched.clear();
                isValid = true;

        }else{
                std::cout << "unable to open file\n";
        }

        std::cout << "\nTotal number of entries = " << entries << '\n';
        std::cout << "\nNumber of valid entries = " << valid << '\n';
        return 0;
}
