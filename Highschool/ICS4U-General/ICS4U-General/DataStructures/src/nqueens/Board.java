package nqueens;

public class Board {

	private Stack stack;
	private int n;

	Board(int n) {
		this.n = n;
		stack = new Stack(n);
	}

	// driving method with the main while loop. Checks if the attempted solutions
	// are within boundaries of n and -1.
	void solve() {
		while (stack.getNumberElements() < n && stack.getNumberElements() > -1) {
			if (!placeNewQueen()) {

				try {
					while (!replaceQueen())
						stack.pop();
				} catch (Exception ex) {
					break;
				}
			}
		}
		if (stack.getNumberElements() <= 0)
			displayFailure();
		else
			displaySuccess();
	}

	// replaces queen at the top of the stack with a queen adjacent to the one being
	// replaced. Returns false if it cannot be done
	private boolean replaceQueen() {
		Queen current = new Queen(stack.peek().getRow() + 1, stack.pop().getCol());

		boolean isPlaced = false;
		while (!isPlaced && current.getRow() < n) {
			if (!isConflicting(current)) {
				stack.push(current);
				return true;
			}
			current = new Queen(current.getRow() + 1, stack.getNumberElements());
		}
		return false;
	}

	// called to display board layout when a solution is found.
	private void displaySuccess() {
		for (int countRow = 0; countRow < n; countRow++) {
			for (int countCol = 0; countCol < n; countCol++) {
				if (checkPosition(countRow, countCol))
					System.out.print(" Q ");
				else
					System.out.print(" x ");

			}
			System.out.println();

		}

	}

	// checks if a queen has been assigned to the position being checked.
	private boolean checkPosition(int countRow, int countCol) {
		Stack temp = new Stack(n);

		boolean hasQueen = false;
		while (stack.getNumberElements() > 0) {
			temp.push(stack.pop());
			if (temp.peek().getCol() == countCol && temp.peek().getRow() == countRow) {
				hasQueen = true;
				break;
			}
		}
		while (temp.getNumberElements() > 0)
			stack.push(temp.pop());
		return hasQueen;
	}

	// displays that the 'n' does not have a solution.
	private void displayFailure() {
		System.out.println("There is no nQueens solution for n = " + n);

	}

	// tries to place a new queen on the board, checking every position available in
	// one column. returns false if there is no space in the column where the queen
	// is not being attacked
	private boolean placeNewQueen() {

		Queen current = new Queen(0, stack.getNumberElements());

		boolean isPlaced = false;
		while (!isPlaced && current.getRow() < n) {
			if (!isConflicting(current)) {
				stack.push(current);
				return true;
			}
			current = new Queen(current.getRow() + 1, stack.getNumberElements());
		}
		return false;
	}

	// checks if a the queen being placed is being attacked by any existing queens.
	private boolean isConflicting(Queen current) {
		if (stack.getNumberElements() == 0)
			return false;

		Stack temp = new Stack(n);

		int numberConflicts = 0;
		while (stack.getNumberElements() > 0) {
			temp.push(stack.pop());
			if (temp.peek().getCol() == current.getCol() || temp.peek().getRow() == current.getRow())
				numberConflicts++;
			else if (isDiagonal(current, temp.peek()))
				numberConflicts++;
		}
		while (temp.getNumberElements() > 0) {
			stack.push(temp.pop());
		}

		return numberConflicts > 0;
	}

	// checks if the queen being placed is diagonal to any placed queens
	private boolean isDiagonal(Queen current, Queen setQueen) {
		for (int i = 0; i > -1 && i < n; i++) {
			if ((setQueen.getCol() + i == current.getCol() && setQueen.getRow() + i == current.getRow())
					|| (setQueen.getCol() + i == current.getCol() && setQueen.getRow() - i == current.getRow()))
				return true;
		}
		return false;
	}

}
