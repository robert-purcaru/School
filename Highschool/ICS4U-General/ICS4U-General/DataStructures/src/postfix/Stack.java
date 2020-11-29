package postfix;

public class Stack {
	
	private int[] data;
	private int numberElements;
	
	@SuppressWarnings("unused")
	public Stack() {
		data = new int[5];
		int numberElements = 0;
	}
	
	public Stack(int[] preload) {
		data = preload;
		for(int i = 0; i < preload.length; i++) {
			if(data[i] != 0) {
				numberElements++;
			} else
				break;
		}
	}
	
	public int peek() {
		return data[numberElements];
	}
	public boolean isEmpty() {
		if(numberElements == 0) {
			return true;
		} return false;
	}
	
	public int pop() {
		return data[--numberElements];
	}
	
	public void push(int value) {
		try{
			data[numberElements++] = value;
		} catch (Exception ex) {
			expandStackCapacity();
			push(value);
		}
	}
	
	private void expandStackCapacity() {
		int[] temp = new int[data.length + 5];
		for(int i = 0; i < data.length; i++) {
			temp[i] = data[i];
		}
		data = temp;
	}
	
	
}
