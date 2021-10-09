package IO;

public class Output {

    /**
     * This class is responsible for housing the methods responsible for outputing to the console
     */

    public Output(){

    };

    /**
     * println
     * Prints a message+"\n" to the screen
     * @param message a string that will be printed to the screen
     */
    public void println(String message){
        System.out.println(message);
    }

    /**
     * print
     * prints a message to the screen
     * @param message a string that will be printed to the screen
     */
    public void print(String message){
        System.out.print(message);
    }

}
