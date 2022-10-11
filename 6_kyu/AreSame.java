import java.util.Arrays;
public class AreSame {
  
  public static boolean comp(int[] a, int[] b) {
    // we will compare each item in B to see if it has a square root in A
    if( b == null || a == null) {
      return false;
    }else if (b.length != a.length){
      return false;
    }else{
      int sum1 = 0;
      int sum2 = 0;
      for (int i =0  ; i< b.length; i++){ // goes through and makes sum 1 and sum2 the sums of a and b
        sum1 += a[i] * a[i];
        sum2 += b[i];
      }
      
      boolean failed = false;
      for(int i = 0; i< a.length; i++){
        if(!Arrays.toString(b).contains(Integer.toString(a[i] * a[i]))){
          failed = true;
        }
      }
      
      if(sum1 == sum2 && failed == false){
        return true;
      }else{
        return false;
      }
  }
}}
