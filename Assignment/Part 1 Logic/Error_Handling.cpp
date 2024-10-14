#include <bits/stdc++.h>

std::string toBinary(int number)
{
    std::string binary;
    if (number == 0)
    {
        return "00000";
    }
    else
    {
        while (number)
        {
            if (number & 1)
                binary += '1';
            else
                binary += '0';
            number >>= 1;
        }
        return binary;
    }
}

std::string reverse(std::string binary)
{
    int n = binary.length();

    for (int i = 0; i < n / 2; ++i)
    {
        std::swap(binary[i], binary[n - i - 1]);
    }

    return binary;
}

void errorMessages(std::string binary)
{
    if (binary == "00000")
        std::cout << "No error\n";
    if (binary[0] == '1')
        std::cout << "Container descent rate failure\n";
    if (binary[1] == '1')
        std::cout << "Science Payload descent rate failure\n";
    if (binary[2] == '1')
        std::cout << "Container position failure\n";
    if (binary[3] == '1')
        std::cout << "Science Payload position failure\n";
    if (binary[4] == '1')
        std::cout << "Release failure\n";
}

int main()
{
    int num;
    std::cin >> num;
    errorMessages(reverse(toBinary(num)));

    return 0;
}

// Sources:
// https://www.geeksforgeeks.org/reverse-a-string-in-c-cpp-different-methods/#1-using-a-loop
// https://www.geeksforgeeks.org/program-decimal-binary-conversion/
