public class String_Reverser
{
    public static void main(String[] args)
    {
        String reverse = "Noah";
        String finish = "";
        for(int i = reverse.length(); i > 0; i--)
        {
            finish += reverse.substring(i-1, i);
        }
        System.out.println(finish);
    }
}