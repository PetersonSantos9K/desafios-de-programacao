package logica;

public class Ex30 {

    static void main() {

        IO.println(isPalindromo("A man, a plan, a canal: Panama"));

    }

    private static boolean isPalindromo(String s){

        boolean check = true;
        String formated = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        if(formated.isEmpty()){
            return true;
        }

        if(formated.length() == 1){
            return true;
        }

        char[] character = formated.toCharArray();
        int p1 = 0;
        for(int p2=character.length-1; p2>0; p2--){

            if(character[p1] != character[p2]){
                check = false;
                break;
            }
            p1++;
        }



        return check;
    }


}
