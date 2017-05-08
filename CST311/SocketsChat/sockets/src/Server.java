import java.io.IOException;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server {
  /**
   * Run the server socket, receive messages from the server socket, and send
   * messages to the client socket.
   *
   * @param args no arguments necessary to begin server
   * @throws IOException server socket cannot be created
   */
  public static void main(String[] args) throws IOException {
    String connectionMessage;
    // Create the server socket. Clients should connect to this server on the
    // same port as defined here (8080).
    ServerSocket serverSocket = new ServerSocket(8080);
    // Accept connections to the server socket and set up communication
    // streams.
    Socket client1 = serverSocket.accept();
    Socket client2 = serverSocket.accept();
    Scanner clientScanner1 = new Scanner(client1.getInputStream());
    Scanner clientScanner2 = new Scanner(client2.getInputStream());
    PrintStream clientStream1 =
        new PrintStream(client1.getOutputStream(), true);
    PrintStream clientStream2 =
        new PrintStream(client2.getOutputStream(), true);
    // Each connection should initially send a message containing the client's
    // name and the the user's name.
    String client1Message = clientScanner1.nextLine();
    String client2Message = clientScanner2.nextLine();
    // Split messages on colons and spaces to obtain the server client and user
    // name. Messages come in the form "Client {client name}: {user name}".
    String[] splitClient1Msg = client1Message.split(" ");
    String[] splitClient2Msg = client2Message.split(" ");
    String clientName1 = splitClient1Msg[1]
        .substring(0, splitClient1Msg[1].length() - 1);
    String clientName2 = splitClient2Msg[1]
        .substring(0, splitClient1Msg[1].length() - 1);
    String userName1 = splitClient1Msg[2];
    String userName2 = splitClient2Msg[2];

    // Log the messages that came from the clients.
    System.out.println("Message from Client 1: \"" + client1Message + "\"");
    System.out.println("Message from Client 2: \"" + client2Message + "\"");
    // Tell the clients which connection came first.
    connectionMessage = clientName1 + ": " + userName1 + " received before "
        + clientName2 + ": " + userName2;
    clientStream1.println(connectionMessage);
    clientStream2.println(connectionMessage);
    System.out.println("Sent acknowledgment to both " + clientName1 + " and "
        + clientName2 + ".");

    // Create a simple "chat" for the two clients. When either client says
    // "Bye", close the connections.
    boolean isClient2Response = true;
    clientStream1.println("** You connected first. "
        + "Say something to begin chat. **");
    while(!client1.isClosed() && !client2.isClosed()) {
      if (isClient2Response) {
        // Send message from client 1 to client 2 if there is a message from
        // client 1.
        client1Message = clientScanner1.nextLine();
        clientStream2.println(userName1 + ": " + client1Message);
        isClient2Response = false;
      } else {
        // Send message from client 2 to client 1 if there is a message from
        // client 2.
        client2Message = clientScanner2.nextLine();
        clientStream1.println(userName2 + ": " + client2Message);
        isClient2Response = true;
      }
      // Close both connections if either client has stated "bye".
      if (client1Message.toLowerCase().contains("bye")
          || client2Message.toLowerCase().contains("bye")) {
        client1.close();
        client2.close();
      }
    }
  }
}
