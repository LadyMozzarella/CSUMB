import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Client {
  /**
   * Run the client socket, receive messages from the server socket and send
   * messages to the server socket.
   *
   * @param args client name sent as the first argument
   * @throws IOException client socket cannot be created
   * @throws IllegalArgumentException client name is not the first argument
   */
  public static void main(String[] args) throws IOException {
    if (args == null || args[0] == null || args[0].equals("")) {
      throw new IllegalArgumentException("Client name as argument is missing.");
    }
    String userName, serverMessage, serverResponse;
    String clientName = args[0];
    // Create the socket for this client. It should connect to the same port
    // defined in the Server program.
    Socket socket = new Socket("127.0.0.1", 8080);
    // The first scanner will allow the user to enter text in via the command
    // line. The second scanner allows the Server socket to send information
    // to this socket.
    Scanner clientScanner = new Scanner(System.in);
    Scanner serverScanner = new Scanner(socket.getInputStream());
    PrintStream serverStream = new PrintStream(socket.getOutputStream(), true);

    // User will enter in messages to send to the server. For now, let's just
    // send the client's name.
    System.out.print("Enter your name: ");
    userName = clientScanner.nextLine();
    // Construct and send the first messages containing the client's name and
    // the user's name.
    serverMessage = "Client " + clientName + ": " + userName;
    serverStream.println(serverMessage);
    // Get and print the server's response.
    serverResponse = serverScanner.nextLine();
    System.out.println("Message Sent to Server: \"" + serverMessage + "\"");
    System.out.println("Message Received from Server: \"" + serverResponse +
        "\"");
    System.out.println(serverResponse);

    // While the connection is still open, check for messages and send
    // messages from/to the server.
    try {
      while ((serverResponse = serverScanner.nextLine()) != null) {
        // If there is a new line from the server, display it.
        System.out.println(serverResponse);
        if (!serverResponse.toLowerCase().contains("bye")) {
          // If there is new user input, send it to the server and display it.
          System.out.print("You: ");
          serverMessage = clientScanner.nextLine();
          serverStream.println(serverMessage);
        }
      }
    } catch (NoSuchElementException | IllegalStateException e) {
      System.out.println("** Chat Closed **");
      socket.close();
    }
  }
}
