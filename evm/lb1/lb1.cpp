#include <iostream>

template<typename T>
unsigned long long printBinaryNum(T num)
{
	unsigned long long bits = *reinterpret_cast<unsigned long long*>(&num);
	int byte = 8;

    for (int i = sizeof(long) * byte - 1; i >= 0; i--) {
        std::cout << ((bits >> i) & 1);
    }

    std::cout << '\n';
	return bits;
}

void read_values(int& start, int& amount, int& times, int& direction)
{
	std::cout << "Enter from which bit to move"<< '\n';
	std::cin >> start;
	std::cout << "Enter until which bit to move"<< '\n';
	std::cin >> amount;
	std::cout << "Enter in which direction to move, 1 for right and -1 for left"<< '\n';
	std::cin >> direction;
	std::cout << "Enter how many times to move"<< '\n';
	std::cin >> times;

	times = times % amount;
}

unsigned long long cycle_move(unsigned long long bits)
{
	int start, finish, times, direction;
	read_values(start, finish, times, direction);

	if(times == finish +1)
		return bits;

	int changed_bits[64] = {};
	int j;
	//filling arras
	for(int i = 64; i>=0; i--)
	{
		j = 63 - i;
		changed_bits[j] = (bits>>i)&1;
		
	}
	
	int last,first;
	for(int i = 0; i<times; i++)
	{
		if (direction == 1) 
		{
		    last = changed_bits[finish];
			
			for(int j = finish; j>start ; j--)
			{
			changed_bits[j] = changed_bits[j-1];
			}
		}

		if (direction == -1)
		{
			first = changed_bits[start];
			for(int j = start; j<finish ; j++)
			{
				changed_bits[j] = changed_bits[j+1];
			}
		}

		changed_bits[finish] = first;
	}
	
	for(int i = 0; i<64; i++)
	{
		std::cout << changed_bits[i];
	}
	std::cout << '\n';

	return  bits;
}

int main() {
    double d = 15.375;
    long l = 123465789;
	unsigned long long d_result;
	unsigned long long l_result;

	std::cout <<"Enter double " << '\n';
	std::cin >> d;

	std::cout << "Enter long "<< '\n';
	std::cin >> l;

    std::cout << "Binary representation of double: ";
    d_result = printBinaryNum(d);
	std::cout << '\n';

    std::cout << "Binary representation of long: ";
    l_result = printBinaryNum(l);
	std::cout << '\n';


	cycle_move(d_result);
		
	cycle_move(l_result);

    return 0;
}
