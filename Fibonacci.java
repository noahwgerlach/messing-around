public class Fibonacci
{
    public static void main(String[] args)
    {
        Thread pause = new Thread();
        long x = 0;
        long y = 1;
        while(true)
        {
            System.out.println(x + y);
            long z = x + y;
            x = y;
            y = z;
        }
    }
}