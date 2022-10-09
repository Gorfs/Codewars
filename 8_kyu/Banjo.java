public class Banjo {
  public static String areYouPlayingBanjo(String name) {
    if (name.charAt(0) == 'r' || name.charAt(0) == 'R'){
      return name + " plays banjo";
    }else{
      return name + " does not play banjo";
    }
  }
}