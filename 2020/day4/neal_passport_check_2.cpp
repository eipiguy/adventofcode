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

        const int numEyeColors = 7;
        const std::string eyeColors[numEyeColors] = {
                "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
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
                                                        if( keys[j].compare(fields[i]) == 0 ){
                                                                matched[j] = true;
                                                                found = true;
                                                                std::cout << tokens[j] << ' ';

                                                                switch( i ){
                                                                case 0:         // byr
                                                                        if( tokens[j].size() != 4
                                                                                || std::stoi(tokens[j]) < 1920
                                                                                || std::stoi(tokens[j]) > 2002 ){
                                                                                isValid = false;
                                                                        }
                                                                        break;
                                                                case 1:         // iyr
                                                                        if( tokens[j].size() != 4
                                                                                || std::stoi(tokens[j]) < 2010
                                                                                || std::stoi(tokens[j]) > 2020 ){
                                                                                isValid = false;
                                                                        }
                                                                        break;
                                                                case 2:         // eyr
                                                                        if( tokens[j].size() != 4
                                                                                || std::stoi(tokens[j]) < 2020
                                                                                || std::stoi(tokens[j]) > 2030 ){
                                                                                isValid = false;
                                                                        }
                                                                        break;
                                                                case 3:         // hgt
                                                                        pos = tokens[j].find("cm");
                                                                        if( pos != std::string::npos ){
                                                                                int cmHeight =
                                                                                std::stoi(tokens[j].substr(0,pos)); 
                                                                                if(150<=cmHeight && cmHeight<=193)
                                                                                      break; 
                                                                        }
                                                                        else{
                                                                                pos = tokens[j].find("in");
                                                                                if( pos != std::string::npos ){
                                                                                        int inHeight =
                                                                                std::stoi(tokens[j].substr(0,pos)); 
                                                                                if(59<=inHeight && inHeight<=76)
                                                                                      break; 
                                                                                }
                                                                        }
                                                                        isValid = false;
                                                                        break;
                                                                case 4:         // hcl
                                                                        if( tokens[j][0] != '#'
                                                                                || tokens[j].size() != 7 ){
                                                                                isValid = false;
                                                                                break;
                                                                        }
                                                                        for(int k=1;k<7;++k){
                                                                                if(isxdigit(tokens[j][k]) == 0){
                                                                                        isValid = false;
                                                                                        break;
                                                                                }
                                                                        }
                                                                        break;
                                                                case 5:         // ecl
                                                                        for(int k=0;k<numEyeColors;++k){
                                                                                if(tokens[j].compare(eyeColors[k])
                                                                                        == 0 ) break;
                                                                        }
                                                                        isValid = false;
                                                                        break;
                                                                case 6:         // pid
                                                                        if( tokens[j].size() != 9 ){
                                                                                isValid = false;
                                                                                break;
                                                                        }
                                                                        for(int k=0;k<9;++k){
                                                                                if(isdigit(tokens[j][k]) == 0){
                                                                                        isValid = false;
                                                                                        break;
                                                                                }
                                                                        }
                                                                        break;
                                                                }       // end of switch
                                                                
                                                                // once validity is checked,
                                                                // stop checking keys,
                                                                // and move to next field
                                                                break;
                                                        
                                                        }       // end of match
                                                }
                                                if(found) break;
                                        }       // end of key loop
                                        
                                        // "found" indicates the key was a valid match
                                        // otherwise the match was invalid
                                        if(!found){ 
                                                std::cout << " field missing!";
                                                isValid = false;
                                                break;
                                        }
                                }       // end of fields 

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
                        }       // end of token parsing

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
