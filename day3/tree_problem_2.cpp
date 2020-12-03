#include <iostream>
#include <fstream>
#include <string>

int main( int argc, char* argv[] ){

        char* inFileName = argv[1];
        std::ifstream inFile(inFileName);
        
        int n = (argc-2)/2; 
        int dx[n], dy[n];
        for(int i=0;i<n;++i){
                dx[i] = std::stoi( argv[(2*i)+2] );
                dy[i] = std::stoi( argv[(2*i)+3] );
        }
        
        if( inFile.is_open() ){
                
                int x[n] = {0}; 
                int y[n] = {0};
                int y_cur = 0;
                int trees[n] = {0};
                std::string line;
                
                while( std::getline(inFile,line) ){
                        
                        for(int i=0;i<n;++i){ 
                                if(y[i] == y_cur){
                                       if(line[ x[i] % line.size() ] == '#') ++trees[i];
                                        x[i] += dx[i];
                                        y[i] += dy[i];
                                }
                        }
                        ++y_cur;
                }
                inFile.close();

                long product = 1;
                for(int i=0;i<n;++i){
                        std::cout << "( " << x[i] << ", " << y[i] << " ) Trees = " << trees[i] << '\n';
                        product *= trees[i]; 
                }
                std::cout << "Product = " << product << '\n';

        }else{
                std::cout << "unable to open file\n";
        }

        return 0;
}
