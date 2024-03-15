using System;

namespace Prime.Services
{
    public class PrimeService
    {
        public bool IsPrime(int candidate)
        {
            if (candidate < 2)
            {
                return false;
            }

            for (var divisor = 2; divisor <= Math.Sqrt(candidate); divisor++)
            {
                if (candidate % divisor == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }

    // This is a simple console application entry point for demonstration purposes.
    class Program
    {
        static void Main(string[] args)
        {
            var primeService = new PrimeService();
            Console.WriteLine("Enter a number to check if it's prime:");
            if (int.TryParse(Console.ReadLine(), out int number))
            {
                bool isPrime = primeService.IsPrime(number);
                if (isPrime)
                {
                    Console.WriteLine($"{number} is a prime number.");
                }
                else
                {
                    Console.WriteLine($"{number} is not a prime number.");
                }
            }
            else
            {
                Console.WriteLine("That's not a valid number.");
            }
        }
    }
}
