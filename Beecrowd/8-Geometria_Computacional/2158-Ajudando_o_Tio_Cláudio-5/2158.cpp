#include <iostream>
using namespace std;

int main(){
    long long fp, fh;
    long long vertex, edge;
    int i =1;
    while(cin>>fp>>fh){

            
            edge = (fp*5+fh*6)/2;
            vertex = 2-(fp+fh)+edge;
            cout<<"Molecula #"<<i<<".:."<<endl;
            cout<<"Possui "<<vertex<<" atomos e "<<edge<<" ligacoes"<<endl<<endl;
            i++;

    }

    return 0;
}