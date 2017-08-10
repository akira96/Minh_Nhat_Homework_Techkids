using System;

namespace star
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.Write ("Colums: ");
			int c = Convert.ToInt32(Console.ReadLine ()); 

			Console.Write ("Rows: ");
			int r = Convert.ToInt32(Console.ReadLine ());

			for (int i = 0; i < r; i++)
			{
				for (int j = 0; j < c; j++) 
				{
					if (i % 2 == 0) 
					{
						Console.Write ("x*");
					} 
					else 
					{
						Console.Write ("*x");
					}
				}
				Console.WriteLine ();
			}
		}
	}
}
