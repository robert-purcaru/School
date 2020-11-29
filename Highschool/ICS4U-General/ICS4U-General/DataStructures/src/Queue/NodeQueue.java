package Queue;

public class NodeQueue {

	private IntNode head;

	public NodeQueue() {
		head = new IntNode(0, null);
	}

	public void enqueue(Integer newData) {
		IntNode current = head;

		while (current.getLink() != null) {
			current = current.getLink();
		}

		current.setLink(new IntNode(newData, null));
	}

	public Integer dequeue() {
		if (head.getLink() == null)
			throw new NullPointerException();
		Integer ret = head.getLink().getData();
		head.setLink(head.getLink().getLink());
		return ret;
	}

	public Integer peek() {
		return head.getLink().getData();
	}

	public void clear() {
		head.setLink(null);
	}

	public boolean isEmpty() {
		return head.getLink() == null;
	}

}
