extern "C" {

double arithmetic(char m, double first, double second)
{
    double result;
    switch(m){
	case '+': result = first+second; break;
	case '-': result = first-second; break;
	case '*': result = first*second; break;
	case '/': result = first/second; break;
    }
    return result;
}

int sum_array(int array[], int size) {
    int sum = 0;
    for(int i=0; i<size; i++){
        sum += array[i];
    }
    return sum;
}
	
struct Param 
{
public:
    int first, second;
}

}
