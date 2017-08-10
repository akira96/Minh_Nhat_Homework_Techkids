using System;

namespace BMI
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.Write ("What's your height?(cm) :  ");
			var h = Convert.ToInt32 (Console.ReadLine());
			h = h / 100;

			Console.Write ("What's your weight?(kg) :  ");
			var w = Convert.ToInt32 (Console.ReadLine());

			var BMI = w / (h * h);
			Console.WriteLine ("Your BMI: " + BMI);

			if (BMI < 16)
			{
				Console.WriteLine("Severely underweight!!!");
			}
			else if (BMI < 18.5)
			{
				Console.WriteLine("Underweight!");
			}
			else if (BMI < 25 )
			{
				Console.WriteLine(" Normal ");
			}
			else if (BMI < 30)
			{
				Console.WriteLine("Overweight!");
			}
			else
			{
				Console.WriteLine("Obese!!!");
			}
		}
	}
}
