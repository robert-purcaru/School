package Queue;

public class ArrayQueue {
	
	private int[] data;
	private int numberElements;
	
	public ArrayQueue() {
		data = new int[5];
		numberElements = 0;
	}
	
	public void enqueue(int e) {
		if(data.length == numberElements - 1)
			expandQueueCapacity();
		data[numberElements] = e;
		numberElements++;
	}
	
	public int dequeue() {
		if(numberElements == 0)
			throw new NullPointerException();
		int ret = data[0];
		int index = 0;
		try{
			while(true) {
				data[index] = data[index + 1];
				index++;
			}
		} catch (Exception ex) {
			data[index] = 0;
		}
		numberElements--;
		return ret;
	}
	
	public int peek() {
		if(numberElements == 0)
			throw new NullPointerException();
		return data[0];
	}
	
	public void clear() {
		numberElements = 0;
	}
	
	public boolean isEmpty() {
		return numberElements == 0;
	}
	
	private void expandQueueCapacity() {
		int[] temp = new int[data.length + 5];
		for(int i = 0; i < data.length; i++) {
			temp[i] = data[i];
		}
		data = temp;
	}
}
