package daytwo.linkedlistcontactlist;

public class ContactNode {
	private Contact data;
	private ContactNode link;

	public ContactNode(Contact data, ContactNode link) {
		this.data = data;
		this.link = link;
	}

	public Contact getData() {
		return data;
	}

	public void setData(Contact data) {
		this.data = data;
	}

	public ContactNode link() {
		return link;
	}

	public void setLink(ContactNode link) {
		this.link = link;
	}
}