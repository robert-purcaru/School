package nqueens;

public class Stack {

	Queen[] data;
	int numberElements;
	
	public Stack (int n) {
		data = new Queen[n];
		numberElements = 0;
	}
	
	public int getNumberElements(){
		return numberElements;
	}
	
	// returns the queen at the top of the data
	public Queen peek() {
		if (numberElements < 1)
			return null;
		return data[numberElements - 1];
	}

	// removes the element at the top of the stack and assigns that spot in the array
	// as null, returns true if there was an item to remove, false otherwise.
	public Queen pop() {
		Queen temp = data[numberElements - 1];
		data[numberElements - 1] = null;
		numberElements--;
		return temp;
	}

	// adds an elemtns to the top of the stack.
	public void push(Queen x) {
		data[numberElements++] = x;
	}
}

