#include <iostream>     // terminal output
#include <fstream>     // read from files
#include <string>       // string operations

int main(int argc, char* argv[]){
        int total=0;
        int valid=0;

        char* inFileName = argv[1];         
        std::cout << inFileName << '\n';

        std::ifstream inFile(inFileName);
        
        if(inFile.is_open()){
                
                std::string line;
                std::string preamble;

                int i1, i2, pos;
                char key;
                char delim = ':';

                while(getline(inFile,line)){
                        pos = line.find(delim);
                        preamble = line.substr(0,pos+2);
                        line.erase(0,pos+4);
                        //std::cout << preamble << '\n';
                        //std::cout << line << '\n';
                        
                        delim = '-';
                        pos = preamble.find(delim);
                        i1 = std::stoi( preamble.substr(0,pos) );
                        preamble.erase(0,pos+1);
                        std::cout << i1 << '-';

                        delim = ' ';
                        pos = preamble.find(delim);
                        i2 = std::stoi( preamble.substr(0,pos) );
                        preamble.erase(0,pos+1);
                        std::cout << i2 << ' ';

                        key = preamble[0];
                        std::cout << key << '\n';

                        std::cout << line;
                        
                        if( (line[i1-1] == key) || (line[i2-1] == key) ){
                                if( (line[i1-1] != key) || (line[i2-1] != key) ){
                                        std::cout << " valid\n";
                                        ++valid;
                                }else{
                                        std::cout << " not valid\n";
                                }
                        }else{
                                std::cout << " not valid\n";
                        }

                        ++total; 
                }
                inFile.close();

                std::cout << "Total: " << total << '\n';
                std::cout << "Valid: " << valid << '\n';

        }else{
                std::cout << "unable to open file";
        }
        return 0;
}
