



Console.WriteLine("Ingrese una cadena de caracteres que represente una estampida de hormigas.");
Console.WriteLine("Ejemplo: ant...ant..ant.ant.an.ant.t.ant.ant");
string input = Console.ReadLine();


int survivors = CountOccurrences(input, "ant");





Console.WriteLine($"Number of ants alive: {survivors}");
Console.WriteLine($"Number of dead ants");


static int CountOccurrences(string str, string substr) 
{ 
 int count = 0;
 int i = 0;


    while ((i = str.IndexOf(substr, i)) != -1)
    { 
        i = i + substr.Length;
        count++;
    }
    return count;
}