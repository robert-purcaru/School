package stacks;

public class IntListStack implements Stack {
	private IntegerNode head;
	
	public Integer peek() {
		return head.getData();
	}

	public Integer pop() {
		Integer temp = head.data;
		head = head.link();
		return temp;
	}

	public boolean isEmpty() {
		return head == null;
		
	}

	public void push(Integer x) {
		head = new IntegerNode(x, head);	
	}

	class IntegerNode {

		private Integer data;
		private IntegerNode link;

		public IntegerNode(Integer data, IntegerNode link) {
			this.data = data;
			this.link = link;
		}

		public Integer getData() {
			return data;
		}

		public void setData(Integer data) {
			this.data = data;
		}

		public IntegerNode link() {
			return link;
		}

		public void setLink(IntegerNode link) {
			this.link = link;

		}

	}
}
