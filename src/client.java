import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class client {
    public static void main(String[] args){
        try{
            Socket client = new Socket("128.6.13.180", 9999);

            System.out.println("Connected");
            OutputStream output = client.getOutputStream();
            DataOutputStream out = new DataOutputStream(output);

            InputStream input = client.getInputStream();
            DataInputStream in = new DataInputStream(input);
            Scanner sc = new Scanner(System.in);
            while(true){
                String inSC = sc.nextLine();
                out.writeUTF(inSC);
                System.out.println("Server: " + in.readUTF());
            }
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}