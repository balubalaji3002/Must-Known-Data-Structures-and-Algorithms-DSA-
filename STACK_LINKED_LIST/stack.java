import java.lang.*;
public class Main {
    public static void main(String[] args) {
        Main Obj = new Main();
        Obj.insert(10);
        Obj.insert(20);
        Obj.insert(30);
        Obj.insert(40);
        Obj.insert(50);
        Obj.insert(60);

        System.out.println("Original List");
        Obj.print();
        
    }
    class Node{
        int element;
        Node next;
        Node prev;

        public Node(int element) {
            this.element = element;
        }
    }

    public Node head = null;
    public Node tail = null;
    int size=0;

    public void insert(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        newNode.prev = null;

        if (head != null)
            head.prev = newNode;

        head = newNode;
    }

    public void print() {

        Node node = head;
        Node end = null;

        while (node != null) {
            System.out.print(node.element + " ");
            end = node;
            node = node.next;
        }
        System.out.println();
    }
}
