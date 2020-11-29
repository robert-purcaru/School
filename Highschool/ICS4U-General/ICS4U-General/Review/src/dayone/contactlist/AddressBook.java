package dayone.contactlist;

public class AddressBook {

	int numberOfContacts;
	Contact[] contactList;

	public AddressBook() {
	    contactList = new Contact[20]; //not my problem if it runs out of space.
		numberOfContacts = 0;
	}

	public int getListSize() {
		return numberOfContacts;
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

	public void displayContactList() {
		for (int i = 0; i < numberOfContacts; i++) {
			System.out.println(contactList[i].toString());
		}
	}
	
	public void addContact(Contact contact) {
		contactList[numberOfContacts] = contact;
		numberOfContacts++;
	}
	
	public void destroy(String lastName) {
		for(int i = 0; i < numberOfContacts; i++) {
			if(lastName.equals(contactList[i].getLastName())) {
				contactList[i].erase();
				if(i != numberOfContacts) 
					contactList[i] = contactList[numberOfContacts - 1];
				numberOfContacts--;
				System.out.println(lastName + " who?");
				return;
			}
				
		}
		System.out.println("You never had a contact named " + lastName);
		
		
	}

	public String find(String lastName) {
		for(int i = 0; i < numberOfContacts; i++) {
			if(lastName.equals(contactList[i].getLastName()))
				return contactList[i].toString();
		}
		return "You don't have any contacts with last name " + lastName;
		
	}
}
