using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
  public static string HighAndLow(string numbers)
  {
    
    string[] inputSplitted = numbers.Split(' ');

    List<int> listaInt = new List<int>();

    foreach (var item in inputSplitted)
    {
      
      listaInt.Add(int.Parse(item));

    }
    
    return listaInt.ToArray().Max().ToString() + " " + listaInt.ToArray().Min().ToString();
  }
}