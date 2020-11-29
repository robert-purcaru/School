package daytwo.linkedlistcontactlist;

public class ContactList {

	private ContactNode head;
	private int numberOfContacts;

	public ContactList() {
		numberOfContacts = 0;
	}

	public int size() {
		return numberOfContacts;
	}

	public void displayContactList() {
		ContactNode currentNode = head;
		while (currentNode != null) {
			System.out.println(currentNode.getData().toString());
			currentNode = currentNode.link();
		}

	}

	public Contact find(String lastName) {
		if(head == null)
			return null;
		ContactNode currentContactNode = head;
		while(currentContactNode != null) {
			if(currentContactNode.getData().getLastName().equals(lastName))
				return currentContactNode.getData();
			currentContactNode = currentContactNode.link();
		}
		return null;
	}

	public void addContact(Contact c) {
		head = new ContactNode(c, head);
		numberOfContacts++;
	}

	public void displayMenu() {
		System.out.println("You have " + numberOfContacts + " contacts saved.");
		System.out.println("You can: ");
		System.out.println("\tSee all contacts (type \"show\").");
		System.out.println("\tAdd new contact (type \"new\").");
		System.out.println("\tSearch for a contact (type \"search\").");
		System.out.println("\tSearch and remove a contact (type \"destroy\").");
		System.out.println();

	}

	public Contact removeContact(String lastName) {
		if (head == null)
			return null;
		if (head.getData().getLastName().equals(lastName)) {
			Contact c = head.getData();
			head = head.link();
			numberOfContacts--;
			return c;
		}
		Contact selectedContact = null;
		ContactNode previous = head;
		while (previous != null) {
			if (previous.getData().getLastName().equals(lastName)) {
				selectedContact = previous.link().getData();
				numberOfContacts--;
				if (previous.link().link() == null) {
					previous.setLink(null);
				} else {
					previous.setLink(previous.link().link());
				}
			}
			previous = previous.link();
		}
		return selectedContact;
	}

}
