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

}
