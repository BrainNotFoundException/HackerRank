import java.io.*;

class Result {

    /*
     * Complete the 'dayOfProgrammer' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER year as parameter.
     */

    public static String dayOfProgrammer(int year) {
    // Write your code here
        
        String res=String.valueOf(year);
        if(year%4==0){
            if(year<1918){
                res = "12.09."+res;
            }else{
                if((year%400==0)||(!(year%100==0))){
                    res="12.09."+res;
                }else{
                    res="13.09."+res;
                }
            }
        }else{
            if(year==1918){
                res="26.09."+res;
            }else{
                res = "13.09."+res;   
            }
        }
        
        return res;
    }

}

public class DayOfTheProgrammer {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int year = Integer.parseInt(bufferedReader.readLine().trim());

        String result = Result.dayOfProgrammer(year);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
