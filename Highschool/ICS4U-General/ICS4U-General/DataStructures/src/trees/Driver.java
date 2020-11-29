package trees;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Driver {


	public static void main(String[] args) throws FileNotFoundException {
		IntBST tree = createTree("dataFiles/treeData.dat");
		tree.inOrderTraversal();
		System.out.println();
		tree.delete(7);
		tree.delete(5);
		tree.delete(14);
		tree.delete(9);
		tree.inOrderTraversal();
		tree.delete(2);
		tree.delete(3);
		tree.inOrderTraversal();
		System.out.println();
		tree.delete(29);

	}

	private static IntBST createTree(String fileName) throws FileNotFoundException {
		Scanner in = new Scanner(new File(fileName));
		IntBST bst = new IntBST();
		while (in.hasNext()) {
			bst.addInt(in.nextInt());
		}
		in.close();
		return bst;
	}
}
