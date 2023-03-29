#include<stdio.h>
#include<stdlib.h>

struct node
{
  int data;
  struct node *left;
  struct node *right;
};

struct node *create_node (int data)
{
  struct node *new_node = (struct node *) malloc (sizeof (struct node));
  new_node->data = data;
  new_node->left = NULL;
  new_node->right = NULL;
  return new_node;
}

struct node *insert_node (struct node *root, int data)
{
  if (root == NULL)
    {
      return create_node (data);
    }
  if (data < root->data)
    {
      root->left = insert_node (root->left, data);
    }
  else
    {
      root->right = insert_node (root->right, data);
    }
  return root;
}

struct node *search_node (struct node *root, int data)
{
  if (root == NULL || root->data == data)
    {
      return root;
    }
  if (data < root->data)
    {
      return search_node (root->left, data);
    }
  else
    {
      return search_node (root->right, data);
    }
}

void inorder (struct node *root)
{
  if (root != NULL)
    {
      inorder_traversal (root->left);
      printf ("%d ", root->data);
      inorder_traversal (root->right);
    }
}

int main ()
{
  struct node *root = NULL;
  root = insert_node (root, 50);
  insert_node (root, 30);
  insert_node (root, 20);
  insert_node (root, 40);
  insert_node (root, 70);
  insert_node (root, 60);
  insert_node (root, 80);
  inorder (root);
  return 0;
}
