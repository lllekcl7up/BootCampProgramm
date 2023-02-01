// Пользователь вводит массив через консоль 
// int n = 5;
// int [] array = new int [n];
// for (int i = 0; i < 5; i++) 
//     array[i] = Convert.ToInt32(Console.ReadLine()); 
// Console.WriteLine("[" + string.Join(", ", array)+ "]");
// Console.WriteLine(array[3]);
// // Сложность алгоритма 
// int summa = 0;
// for (int i = 0; i < n; i++)
// {
//     summa += array[i];
// }
// Console.WriteLine(summa);

int n = Convert.ToInt32(Console.ReadLine());
int [,] matrix = new int [n,n];
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n ; j++)
    {
        matrix [i,j] = (i + 1 ) * (j + 1 );
        matrix [j,i] = (i + 1 ) * (j + 1 );
    }
    Console.WriteLine();
}
for (int i = 0; i < n; i++)
{
    for (int j = 0; j < n; j++)
    {
        Console.Write(matrix[i,j]);
        Console.Write(" ");
    }
    Console.WriteLine();
}