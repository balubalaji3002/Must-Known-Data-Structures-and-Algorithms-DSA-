import java.lang.*;

class DoublyLinkedList {
    Node head;

    // Node Class
    class Node {
        int data;
        Node next, prev;

        Node(int x) // parameterized constructor
        {
            data = x;
            next = null;
            prev = null;
        }
    }

    // inserts at first position
    public void insertNode(int data) {
        // Creating newNode memory & assigning data value
        Node newNode = new Node(data);

        newNode.next = head;
        newNode.prev = null;

        // if DLL had already >=1 nodes
        if (head != null)
            head.prev = newNode;

        // changing head to this
        head = newNode;
        System.out.println(newNode.data + " inserted");
    }

    public void display() {
        Node node = head;
        Node end = null;
        //as linked list will end when Node reaches Null

        System.out.print("\nIn forward: ");
        while (node != null) {
            System.out.print(node.data + " ");
            end = node;
            node = node.next;
        }
        System.out.print("\nIn backward: ");

        while (end != null) {
            System.out.print(end.data + " ");
            end = end.prev;
        }
        System.out.println("\n");
    }

}
class Main{
    public static void main(String args[])
    {
        DoublyLinkedList dll = new DoublyLinkedList();

        dll.insertNode(26);
        dll.insertNode(25);
        dll.insertNode(24);

        dll.display();

        dll.insertNode(23);
        dll.insertNode(22);
        dll.insertNode(21);
        dll.insertNode(20);

        dll.display();
    }
}
