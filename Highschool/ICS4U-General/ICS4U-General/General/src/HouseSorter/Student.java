package HouseSorter;

public class Student {
	private String firstName;
	private String lastName;
	private String house;
	private int grade;
	
	public Student() {
		firstName = null;
		lastName = null;
		house = null;
		grade = -1;
	}
	
	public Student(String firstName, String lastName, String house, int grade) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.house = house;
		this.grade = grade;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getHouse() {
		return house;
	}

	public void setHouse(String house) {
		this.house = house;
	}

	public int getGrade() {
		return grade;
	}

	public void setGrade(int grade) {
		this.grade = grade;
	}

	
	
}
