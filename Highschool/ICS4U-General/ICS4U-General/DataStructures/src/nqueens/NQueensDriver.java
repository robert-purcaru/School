package nqueens;

public class NQueensDriver {

	public static void main(String[] args) {
		
		int n = 28;
		
		Board board = new Board(n);
		board.solve();
		
	}

}
