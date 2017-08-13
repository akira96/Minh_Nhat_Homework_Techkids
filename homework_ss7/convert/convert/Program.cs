using System;

namespace convert
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			int n, i, j, bin = 0, dec;
			Console.WriteLine ("Chuyen doi thap phan thanh nhi phan trong C#");
			Console.WriteLine ("--------------------------------------------");
			Console.Write ("Nhap mot so thap phan bat ky: ");
			n = Convert.ToInt32 (Console.ReadLine());
			dec = n;
			i = 1;
			for (j = n; j > 0; j = j / 2)
			{
				bin = bin + (n % 2) * i;
				i = i * 10;
				n = n / 2;
			}
			Console.WriteLine ("So trong he nhi phan tuong duong cua so {0} la {1}", dec, bin);
		}
	}
}
