package trees;

public class IntBinaryTreeNode {
	private Integer data;
	private IntBinaryTreeNode leftChild;
	private IntBinaryTreeNode rightChild;

	public IntBinaryTreeNode(Integer data) {
		this.data = data;
		this.leftChild = null;
		this.rightChild = null;
	}

	public IntBinaryTreeNode(Integer data, IntBinaryTreeNode leftChild, IntBinaryTreeNode rightChild) {
		this.data = data;
		this.leftChild = leftChild;
		this.rightChild = rightChild;
	}
	
	public boolean hasChildren() {
		return leftChild != null || rightChild !=null; 
	}

	public boolean hasLeft() {
		return leftChild != null;
	}
	
	public boolean hasRight() {
		return rightChild != null;
	}

	public Integer getData() {
		return data;
	}

	public void setData(Integer data) {
		this.data = data;
	}

	public IntBinaryTreeNode getLeftChild() {
		return leftChild;
	}

	public void setLeftChild(IntBinaryTreeNode leftChild) {
		this.leftChild = leftChild;
	}

	public IntBinaryTreeNode getRightChild() {
		return rightChild;
	}

	public void setRightChild(IntBinaryTreeNode rightChild) {
		this.rightChild = rightChild;
	}

}
