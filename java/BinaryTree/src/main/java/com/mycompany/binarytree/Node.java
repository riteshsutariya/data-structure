/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.binarytree;

/**
 *
 * @author ritesh
 */
public class Node<T> {
    T item;
    Node left;
    Node right;
    public Node(T item){
        this.item=item;
        this.left=null;
        this.right=null;
    }
}
