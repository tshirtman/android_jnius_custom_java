package org.test;
import java.lang.String;

public class TestClass {
	private String _name;

	public TestClass(String name) {
		_name = name;
	}

	public String get_result() {
		return "Hello " + _name;
	}
}
