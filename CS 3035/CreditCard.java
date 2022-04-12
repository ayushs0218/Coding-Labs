package project;

import java.util.ArrayList;
import java.util.Scanner;

public class CreditCard
{
	public static String cardFinder(ArrayList<Integer> cardList)
	{
		if(cardList.size() == 15 && cardList.get(0) == 3)
		{
			return "American Express Card";
		}
		else if((cardList.size() >= 16 && cardList.size() <= 19) && cardList.get(0) == 6)
		{
			return "Discover Card";
		}
		else if(cardList.size() == 16 && cardList.get(0) == 5)
		{
			return "Master Card";
		}
		else if((cardList.size() >= 13 && cardList.size() <= 16) && cardList.get(0) == 4)
		{
			return "Visa Card";
		}
		else
		{
			return "Invalid Card";
		}
	}
	
	public static String luhn(ArrayList<Integer> cardList)
	{
		int secondDigitSum = 0;
		int firstDigitSum = 0;
		int totalSum = 0;
		ArrayList<Integer> secondDigitList = new ArrayList<Integer>();
		ArrayList<Integer> firstDigitLigit = new ArrayList<Integer>();
		for(int i = cardList.size() - 2; i >= 0; i = i - 2)
		{
			if((cardList.get(i) * 2) < 10)
			{
				secondDigitSum = secondDigitSum + (cardList.get(i) * 2);
			}
			else
			{
				int tens = (cardList.get(i) * 2) / 10;
				int ones = (cardList.get(i) * 2) % 10;
				secondDigitSum = secondDigitSum + (tens + ones);
			}
			secondDigitList.add(cardList.get(i));
		}
		for(int i = cardList.size() - 1; i >= 0; i = i - 2)
		{
			firstDigitSum += cardList.get(i);
			firstDigitLigit.add(cardList.get(i));
		}
		totalSum = firstDigitSum + secondDigitSum;
		if(totalSum % 10 == 0)
		{
			return "Valid";
		}
		else
		{
			return "Invalid";
		}
	}
	
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter A Card Number: ");
		String card = scan.next();
		System.out.println(card);
		ArrayList<Integer> cardList = new ArrayList<Integer>();
		for(int i = 0; i < card.length(); i++)
		{
			cardList.add(Integer.parseInt(card.substring(i, i + 1)));
		}
		if(cardFinder(cardList).equals("Invalid Card"))
		{
			System.out.println(cardFinder(cardList));	
		}
		else
		{
			System.out.println("This " + cardFinder(cardList) + " is " + luhn(cardList));
		}
		scan.close();
	}

}
