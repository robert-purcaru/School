package HouseSorter;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class StudentHolder {
	private HashMap<String, Student> masterStudentNameMap;
	private HashMap<String, Student> masterStudentGradeMap;
	private HashMap<String, Student> masterStudentNameLastInitMap;
	private int pointsLaurier = 0;
	private int pointsMacdonald = 0;
	private int pointsMackenzie = 0;
	private int pointsTrudeau = 0;
	private ArrayList<String> namesNotFound = new ArrayList<String>();

	void develope() {
		initStudents("data/students.dat");
		countScores("data/in.dat");
		displayScores();
	}

	private void displayScores() {
		System.out.println("Laurier: " + pointsLaurier);
		System.out.println("Macdonald: " + pointsMacdonald);
		System.out.println("Mackenzie: " + pointsMackenzie);
		System.out.println("Trudeau: " + pointsTrudeau);
		System.out.println();
		if (namesNotFound.size() > 0) {
			System.out.println("These students were not found:");
			for (int i = 0; i < namesNotFound.size(); i++)
				System.out.println(namesNotFound.get(i));
		}
	}

	private void countScores(String fileName) {
		Scanner inputScanner;
		try {
			inputScanner = new Scanner(new File(fileName));
			while (inputScanner.hasNext()) {
				String student = inputScanner.nextLine();
				String studentID = student.replace(" ", "").toLowerCase();
				if (masterStudentNameMap.get(studentID) != null) {
					getPointsFromName(studentID);
				} else if (masterStudentGradeMap.get(studentID) != null) {
					getPointsFromGrade(studentID);
				} else if (masterStudentNameLastInitMap.get(studentID) != null) {
					getPointsFromInit(studentID);
				} else if (masterStudentNameMap.get(studentID.substring(0, studentID.length() - 1)) != null) {
					getShirtPointsFromName(studentID.substring(0, studentID.length() - 1));
				} else if (masterStudentGradeMap.get(studentID.substring(0, studentID.length() - 1)) != null) {
					getShirtPointsFromGrade(studentID.substring(0, studentID.length() - 1));
				} else if (masterStudentNameLastInitMap.get(studentID.substring(0, studentID.length() - 1)) != null) {
					getShirtPointsFromInit(studentID.substring(0, studentID.length() - 1));
				} else {
					namesNotFound.add(student);
				}
			}

		} catch (Exception ex) {
			System.out.println("There was a problem with the input document");
		}

	}

	private void getShirtPointsFromInit(String studentID) {
		String house = masterStudentNameLastInitMap.get(studentID).getHouse();
		assignPoints(house);		
		assignPoints(house);
	}

	private void getShirtPointsFromGrade(String studentID) {
		String house = masterStudentGradeMap.get(studentID).getHouse();
		assignPoints(house);		
		assignPoints(house);
	}

	private void getShirtPointsFromName(String studentID) {
		String house = masterStudentNameMap.get(studentID).getHouse();
		assignPoints(house);
		assignPoints(house);
	}

	private void getPointsFromInit(String studentID) {
		String house = masterStudentNameLastInitMap.get(studentID).getHouse();
		assignPoints(house);
	}

	private void getPointsFromGrade(String studentID) {
		String house = masterStudentGradeMap.get(studentID).getHouse();
		assignPoints(house);

	}

	private void getPointsFromName(String studentID) {
		String house = masterStudentNameMap.get(studentID).getHouse();
		assignPoints(house);
		

	}

	private void assignPoints(String house) {
		if (house.equals("Laurier"))
			pointsLaurier++;
		if (house.equals("Macdonald"))
			pointsMacdonald++;
		if (house.equals("Mackenzie"))
			pointsMackenzie++;
		if (house.equals("Trudeau"))
			pointsTrudeau++;
	}

	private void initStudents(String fileName) {
		masterStudentNameMap = new HashMap<String, Student>();
		masterStudentGradeMap = new HashMap<String, Student>();
		masterStudentNameLastInitMap = new HashMap<String, Student>();
		Scanner studentScanner;

		try {
			studentScanner = new Scanner(new File(fileName));
			while (studentScanner.hasNext()) {
				Student s = new Student();

				String studentInfo = studentScanner.nextLine();
				s.setFirstName(studentInfo.split(", ")[0].trim().toLowerCase());
				s.setLastName(studentInfo.split(", ")[1].trim().toLowerCase());
				s.setHouse(studentInfo.split(", ")[2].trim());
				try {
					s.setGrade(Integer.parseInt(studentInfo.split(", ")[3]));
				} catch (Exception ex) {
					System.out.println("The grade for" + studentInfo.split(", ")[0].trim() + " has a syntax error.");
				}

				String fullName = s.getFirstName().toLowerCase() + s.getLastName().toLowerCase();
				String nameAndGrade = s.getFirstName().toLowerCase() + s.getGrade();
				String nameAndInit = s.getFirstName().toLowerCase() + s.getLastName().substring(0, 1).toLowerCase();

				masterStudentNameMap.put(fullName, s);
				masterStudentGradeMap.put(nameAndGrade, s);
				masterStudentNameLastInitMap.put(nameAndInit, s);

			}
		} catch (Exception ex) {
			System.out.println("Problem Making Student Map");
		}
	}

}
