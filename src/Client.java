package security;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Client extends Thread{
	

	
	private Socket client_socket;
	
	public Client(Socket client_socket){
		
		this.client_socket = client_socket;
		this.start();
		
		
	}
	@Override
	public void run() {
		
		try{
			
			System.out.println("Thread Created");
			System.out.println("Established Connection!!!");
			
			//making a input and output streams
	        DataInputStream in = new DataInputStream(client_socket.getInputStream());
	        DataOutputStream out = new DataOutputStream(client_socket.getOutputStream());
	        
	        
	        Scanner sc = new Scanner(System.in);
	        
	        
	        while (true){
	        	
	        	String jesse = in.readUTF();
	        	
	        	if (jesse.equalsIgnoreCase("q")){break;}
	        	
	        	System.out.println("Jesse: " +jesse);
	        	String response = sc.nextLine();
	        	
	        	out.writeUTF(response);
	        	System.out.println("You: " + response);     
	        	
	        }
		}
		catch(Exception e){
			
			e.printStackTrace();
		}
		
        
        
        System.out.println("Connection Closed");
	
	}//run method ends
}//client method ends
	
	
	
	
	

