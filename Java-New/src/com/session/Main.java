package com.session;
import IO.Output;

public class Main {

    public static void main(String[] args) {
	// write your code here
        init();
        Output screen = new Output();
        if(args.length == 0){
            screen.println("You loaded in no files");
        }else if(args.length == 1){
            screen.println("You loaded in 1 files");
        }else{
            screen.println("You loaded in too many files");
        }
    }

    public static void init(){
        StartUpMessage();
    }


    public static void StartUpMessage(){
        System.out.println("Welcome to deckor");
    }
}
