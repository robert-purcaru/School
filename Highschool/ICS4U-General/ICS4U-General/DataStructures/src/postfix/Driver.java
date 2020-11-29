package postfix;

public class Driver {
	
	private static String expression;
	
	public static void main(String[] args) {
		expression = "10 2 8 * + 3 -";
		PostfixEvaluator pE = new PostfixEvaluator(expression);
		pE.evaluate();

	}

}
