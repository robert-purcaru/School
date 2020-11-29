package stacks;

public class IntArrayStack implements Stack {
	private Integer[] data;
	private int manyItems;

	public Integer peek() {
		if(manyItems == 0) throw new IllegalStateException("You really goofed this one up");
		return data[manyItems];
	}

	public Integer pop() {
		return data[--manyItems];
	}

	public boolean isEmpty() {
		return manyItems == 0;
	}

	public void push(Integer x) {
		data[manyItems++] = x;

	}
}
