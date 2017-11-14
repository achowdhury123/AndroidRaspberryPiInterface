import java.net.ServerSocket;
import java.net.Socket;
import java.io.*;

public class host {
  public static void main(String[] args)  {
    try {
      ServerSocket serverSocket = new ServerSocket(0);
      System.out.println(serverSocket.getLocalPort());
      while(true) {
        Socket socket = serverSocket.accept();
        System.out.println("Test");
        PrintWriter printWriter = new PrintWriter("accelerometerdata.txt");
        String input;
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        while((input = bufferedReader.readLine()) != null)  {
           System.out.println(input);
           printWriter.println(input);
        }
        printWriter.close();
      }
      // socket.close();
    }
    catch(IOException e) {
      e.printStackTrace();
      System.out.println("Failed");
    }
  }
}
