package dayone.contactlist;

import java.util.Scanner;

public class AddressBookDriver {

	static Scanner in = new Scanner(System.in);

	public static void main(String[] args) {
		AddressBook contacts = new AddressBook();

		while (true) {
			contacts.displayMenu();
			processComand(getCommand(in.nextLine()), contacts);

		}

	}

	private static void processComand(int id, AddressBook contacts) {
		if (id == 5) {
			System.out.println("That is an invalid command. Try again");
			System.out.println("----------------------------");
			return;
		} else if (id == 0) {
			if (contacts.getListSize() == 0) {
				System.out.println("There ain't nothin to show");
				System.out.println("----------------------------");
				return;
			} else {
				System.out.println("Your contacts are:");
				contacts.displayContactList();
				System.out.println("----------------------------");
				return;
			}
		} else if (id == 1) {
			Contact contact = new Contact();
			System.out.print("Please enter the first name of the new contact: ");
			contact.setFirstName(in.nextLine());
			System.out.print("Please enter the last name of the new contact: ");
			contact.setLastName(in.nextLine());		
			System.out.print("Please enter the phone number of the new contact: ");
			contact.setPhone(in.nextLine());
			System.out.println(contact.getFirstName() + " " + contact.getLastName() + " has been added.");
			System.out.println("----------------------------");
			contacts.addContact(contact);

			return;
		} else if(id == 2) {
			System.out.println("Enter the last name of the person you're looking for: ");
			System.out.println(contacts.find(in.nextLine()));
			System.out.println("----------------------------");
			return;
		} else if(id == 3) {
			System.out.println("Enter the last name of the contact who has dishonored you: ");
			contacts.destroy(in.nextLine());
			System.out.println("----------------------------");
		}

		return;
	}

	private static int getCommand(String command) {
		command.toLowerCase().replaceAll(" ", "");
		try {
			if (command.equals("show"))
				return 0;
			if (command.equals("new"))
				return 1;
			if (command.equals("search"))
				return 2;
			if (command.equals("destroy"))
				return 3;
		} catch (Exception ex) {
		}
		return 5;
	}

}
