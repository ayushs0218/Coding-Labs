package project;

import java.util.ArrayList;
import java.util.Scanner;

public class CreditCardMultithreading extends Thread
{	
	
//	Step 1: Check if the length of the Credit Card is: 13-19 digits
	public static boolean cardLengthValidator(ArrayList<Integer> cardList)
	{
		if (cardList.size() >= 13 && cardList.size() <= 19)
		{
			return true;
		} 
		else
		{
			return false;
		}
	}

//	Step 2: Find the Manufacturer of the Credit Card
	public static String industryFinder(ArrayList<Integer> cardList)
	{
		if (cardList.get(0) == 3)
		{
			return "American Express";
		} 
		else if (cardList.get(0) == 6)
		{
			return "Discover Card";
		} 
		else if (cardList.get(0) == 5)
		{
			return "Master Card";
		} 
		else if (cardList.get(0) == 4)
		{
			return "Visa Card";
		} 
		else
		{
			return "Invalid Card";
		}
	}

//	Step 3: Double every even value in the Credit Card number from reverse and use the rules of Luhn's Algorithm
	public static int evenDigitCalculator(ArrayList<Integer> cardList)
	{
		int secondDigitSum = 0;
		for (int i = cardList.size() - 2; i >= 0; i = i - 2)
		{
			if ((cardList.get(i) * 2) < 10)
			{
				secondDigitSum = secondDigitSum + (cardList.get(i) * 2);
			} else
			{
				int tens = (cardList.get(i) * 2) / 10;
				int ones = (cardList.get(i) * 2) % 10;
				secondDigitSum = secondDigitSum + (tens + ones);
			}
		}
		return secondDigitSum;
	}

//	Step 4: Find the sum of all odd values in the Credit Card number from reverse.
	public static int oddDigitCalculator(ArrayList<Integer> cardList)
	{
		int firstDigitSum = 0;
		for (int i = cardList.size() - 1; i >= 0; i = i - 2)
		{
			firstDigitSum += cardList.get(i);
		}
		return firstDigitSum;

	}
	
//	Step 5: Find the sums of Part 3 and 4 and check if the sum is divisible by 10
	public static String divisibiltyChecker(int evenValues, int oddValues)
	{
		if((evenValues + oddValues) % 10 == 0)
		{
			return "This card is valid";
		}
		else
		{
			return "This card is invalid";
		}
	}
	
	
	public static void main(String[] args) throws InterruptedException
	{
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter A Card Number: ");
		String card = scan.next();

		ArrayList<Integer> cardList = new ArrayList<Integer>();
		for (int i = 0; i < card.length(); i++)
		{
			cardList.add(Integer.parseInt(card.substring(i, i + 1)));
		}
		
//		Create a thread for Step 1
		Thread step1 = new Thread(new Runnable() 
		{
		    @Override
		    public void run() 
		    {
		        cardLengthValidator(cardList);
		    }
		});
		
//		Create a thread for Step 2
		Thread step2 = new Thread(new Runnable() 
		{
		    @Override
		    public void run() 
		    {
		    	industryFinder(cardList);
		    	}
		});
		
//		Create a thread for Step 3
		Thread step3 = new Thread(new Runnable() 
		{
		    @Override
		    public void run() 
		    {
		        evenDigitCalculator(cardList);
		    }
		    });
		
//		Create a thread for Step 4
		Thread step4 = new Thread(new Runnable() 
		{
		    @Override
		    public void run() 
		    {
		        oddDigitCalculator(cardList);
		    }
		});
		
		int evenValues = evenDigitCalculator(cardList);
		int oddValues = oddDigitCalculator(cardList);
		
//		Create a thread for Step 5
		Thread step5 = new Thread(new Runnable() 
		{
		    @Override
		    public void run() 
		    {
		    	System.out.println(divisibiltyChecker(evenValues, oddValues));
		    }
		});
		
//		Run all threads
		step1.start();
		step2.start();
		step3.start();
		step4.start();
		step5.start();
		
//		Join all threads
		step1.join();
		step2.join();
		step3.join();
		step4.join();
		step5.join();
		
	}
}
