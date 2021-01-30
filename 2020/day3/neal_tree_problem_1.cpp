#include <iostream>
#include <fstream>
#include <string>

int main( int argc, char* argv[] ){
        
        char* inFileName = argv[1];
        std::ifstream inFile(inFileName);

        int dx = std::stoi( argv[2] );
        
        if( inFile.is_open() ){
                
                int x = 0; 
                int y = 0;
                int trees = 0;
                std::string line;
                
                while( std::getline(inFile,line) ){
                        
                        if( line[ x % line.size() ] == '#' ) ++trees;
                        
                        ++y;
                        x += dx;
                }
                inFile.close();

                std::cout << "( " << x << ", " << y << " ) Trees = " << trees << '\n';

        }else{
                std::cout << "unable to open file\n";
        }

        return 0;
}
