import java.io.*;
import java.text.*;
import java.util.*;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
        int p=0;
        int n=0;
        int z=0;
        int a=arr.size();
        for(int i=0;i<arr.size();i++){
            if(arr.get(i)<0){
                n+=1;
            }else if(arr.get(i)>0){
                p+=1;
            }else{
                z+=1;
            }
        }
        float pa =(float) p/a;
        float na =(float) n/a;
        float za =(float) z/a;
        DecimalFormat df = new DecimalFormat();
        df.setMaximumFractionDigits(6);
        System.out.println(df.format(pa));
        System.out.println(df.format(na));
        System.out.println(df.format(za));
    }

}

public class PlusMinus {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String[] arrTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrTemp[i]);
            arr.add(arrItem);
        }

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
