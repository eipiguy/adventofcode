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

                int keynum, min, max, pos;
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
                        min = std::stoi( preamble.substr(0,pos) );
                        preamble.erase(0,pos+1);
                        std::cout << min << '-';

                        delim = ' ';
                        pos = preamble.find(delim);
                        max = std::stoi( preamble.substr(0,pos) );
                        preamble.erase(0,pos+1);
                        std::cout << max << ' ';

                        key = preamble[0];
                        std::cout << key << '\n';

                        std::cout << line;
                        
                        keynum=0;
                        for(int i=0;i<line.size();++i){
                                if(line[i]==key) ++keynum;
                        }
                        if( (keynum >= min) && (keynum <= max) ){
                                std::cout << ' ' << keynum << " valid\n";
                                ++valid;
                        }else{
                                std::cout << ' ' << keynum << " not valid\n";
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
