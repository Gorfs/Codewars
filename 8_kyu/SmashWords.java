import java.util.Arrays;

public class SmashWords {

	public static String smash(String... words) {
    String res = "";
    for (int i = 0; i < words.length; i ++){
      if (i == 0){
        res += words[i];
      }else{
        res += " " + words[i];
      }
    }
    return res;
  }
}
