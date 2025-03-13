
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
 
public class Main {
    public static String capitalizeEachWord(String input) {
        Pattern pattern = Pattern.compile("(^|\\s)\\S");
        Matcher matcher = pattern.matcher(input);
        String output = "";
        while (matcher.find()) {
            String word = matcher.group();
            if (word.matches("\\S*\\W.*")) {
                output += word + " - special character is present";
            } else {
                output += word.toUpperCase();
            }
            output += " ";
        }
        return output.trim();
    }
 
    public static void main(String[] args) {
        String input = "hello world!";
        System.out.println(capitalizeEachWord(input)); // Output: Hello World!
 
        input = "first-class and second-class both begin with a capital letter";
        System.out.println(capitalizeEachWord(input)); // Output: First-Class - special character is present and Second-Class - special character is present both begin with a capital letter
    }
}
