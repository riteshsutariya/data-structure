/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.binarytree;

/**
 *
 * @author ritesh
 */
public class BinaryTree {

    public static void main(String[] args) {
        Node<Character> node = new Node<>('A');
        node.left = new Node('B');
        node.right = new Node('W');
        node.left.left = new Node('X');
        node.left.right = new Node('S');
        node.left.left.left = new Node('E');
        node.left.left.right = new Node('M');

        node.right.left = new Node('T');
        node.right.right = new Node('C');
        node.right.left.left =  new Node('P');
        node.right.left.right = new Node('N');
        node.right.right.left = new Node('H');
        
        System.out.println("inorder traversal: ");
        inorder(node);
        System.out.println("");
        System.out.println("preorder traversal: ");
        preorder(node);
        System.out.println("");
        System.out.println("postorder traversal: ");
        postorder(node);
    }

    public static void inorder(Node root) {
        if (root != null) {
//            traverse left
            inorder(root.left);
//            process root node
            System.out.print(root.item + "->");
//            traverse right
            inorder(root.right);
        }
    }

    public static void preorder(Node root) {
        if (root != null) {
//            process root
            System.out.print(root.item + "->");
//            traverse left
            preorder(root.left);
//            traverse right
            preorder(root.right);
        }
    }

    public static void postorder(Node root) {
        if (root != null) {
//            traverse left
            postorder(root.left);
//            traverse right
            postorder(root.right);
//            process root
            System.out.print(root.item + "->");
        }
    }
}
