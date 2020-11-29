package trees;

public class IntBST {

	private IntBinaryTreeNode root;

	public IntBST(IntBinaryTreeNode root) {
		this.root = root;
	}

	public IntBST() {
		this.root = null;
	}

	public boolean hasInt(Integer x) {
		if (root == null) {
			return false;
		}

		if (root.getData() == x) {
			return true;
		}

		if (x < root.getData()) {
			if (root.hasLeft()) {
				return hasInt(x, root.getLeftChild());
			} else {
				return false;
			}
		} else if (x > root.getData()) {
			if (root.hasRight()) {
				hasInt(x, root.getRightChild());
			} else {
				return false;
			}
		}
		
		return false;
	}

	private boolean hasInt(Integer x, IntBinaryTreeNode root) {
		if (root.getData() == x) {
			return true;
		}

		if (x < root.getData()) {
			if (root.hasLeft()) {
				return hasInt(x, root.getLeftChild());
			} else {
				return false;
			}
		} else if (x > root.getData()) {
			if (root.hasRight()) {
				hasInt(x, root.getRightChild());
			} else {
				return false;
			}
		}
		
		return false;
	}
		

	public void addInt(Integer data) {
		if (root == null) {
			root = new IntBinaryTreeNode(data);
			return;
		}
		if (data <= root.getData()) {
			if (root.hasLeft()) {
				addIntNode(root.getLeftChild(), data);
			} else {
				root.setLeftChild(new IntBinaryTreeNode(data));
			}
		} else if (data > root.getData()) {
			if (root.hasRight()) {
				addIntNode(root.getRightChild(), data);
			} else {
				root.setRightChild(new IntBinaryTreeNode(data));
			}
		}
	}

	public boolean delete(Integer data) {
		if (root == null) {
			throw new NullPointerException();
		}

		if (root.getData() == data) {
			root.setData(removeReplacementValue(root));
		} else
			return delete(data, root);

		if (root.getData() == null)
			root = null;

		return true;
	}

	private boolean delete(Integer data, IntBinaryTreeNode current) {
		if (current.hasLeft() && current.getLeftChild().getData() == data && !current.getLeftChild().hasChildren()) {
			current.setLeftChild(null);
			return true;
		} else if (current.hasRight() && current.getRightChild().getData() == data
				&& !current.getRightChild().hasChildren()) {
			current.setRightChild(null);
			return true;
		}

		if (current.getData() == data) {
			current.setData(removeReplacementValue(current));
			return true;
		} else {
			if (data <= current.getData() && current.hasLeft()) {
				return delete(data, current.getLeftChild());
			} else if (data > current.getData() && current.hasRight()) {
				return delete(data, current.getRightChild());
			}
		}
		return false;

	}

	private Integer removeReplacementValue(IntBinaryTreeNode current) {
		if (current.hasRight()) {
			current = current.getRightChild();
			while (current.hasLeft())
				current = current.getLeftChild();
			Integer ret = current.getData();
			delete(current.getData());
			return ret;

		} else if (current.hasLeft()) {
			current = current.getLeftChild();
			while (current.hasRight())
				current = current.getLeftChild();
			Integer ret = current.getData();
			delete(current.getData());
			return ret;
		}
		return null;

	}

	private void addIntNode(IntBinaryTreeNode root, Integer data) {
		if (data <= root.getData()) {
			if (root.hasLeft()) {
				addIntNode(root.getLeftChild(), data);
			} else {
				root.setLeftChild(new IntBinaryTreeNode(data));
			}
		} else if (root.getData() < data) {
			if (root.hasRight()) {
				addIntNode(root.getRightChild(), data);
			} else {
				root.setRightChild(new IntBinaryTreeNode(data));
			}
		}

	}

	// TODO Halp
	public boolean refactor() {
		if (root == null)
			return false;

		return false;
	}

	public void processNode(IntBinaryTreeNode node) {
		System.out.println(node.getData());
	}

	public void preOrderTraversal() {
		preOrderTraversal(root);
	}

	private void preOrderTraversal(IntBinaryTreeNode node) {
		processNode(node);
		if (node.hasLeft())
			preOrderTraversal(node.getLeftChild());
		if (node.hasRight())
			preOrderTraversal(node.getRightChild());
	}

	public void postOrderTraversal() {
		postOrderTraversal(root);
	}

	private void postOrderTraversal(IntBinaryTreeNode node) {

		if (node.hasLeft())
			postOrderTraversal(node.getLeftChild());
		if (node.hasRight())
			postOrderTraversal(node.getRightChild());

		processNode(node);
	}

	public void inOrderTraversal() {
		inOrderTraversal(root);
	}

	private void inOrderTraversal(IntBinaryTreeNode node) {
		if (node.hasLeft())
			inOrderTraversal(node.getLeftChild());
		processNode(node);
		if (node.hasRight())
			inOrderTraversal(node.getRightChild());
	}
}
