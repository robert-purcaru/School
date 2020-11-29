package Queue;

public class IntNode {
	private Integer data;
	private IntNode link;

	public IntNode(Integer data, IntNode link) {
		this.data = data;
		this.link = link;
	}
	
	public Integer getData() {
		return data;
	}

	public void setData(Integer data) {
		this.data = data;
	}

	public IntNode getLink() {
		return link;
	}

	public void setLink(IntNode link) {
		this.link = link;
	}
}
