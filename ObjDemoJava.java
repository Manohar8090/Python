class Student
{
	int sno;
	String sname;
	float marks;
	String cname;
}//Student--Class
class ObjDemoJava 
{
	public static void main(String[] args) 
	{
		Student s=new Student(); //  here s is called object
		s.sno=10;
		s.sname="JG";
		s.marks=34.56f;
		System.out.println(s.sno+" "+s.sname+" "+s.marks);
		s.cname="JNTU";
		System.out.println(s.sno+" "+s.sname+" "+s.marks+" "+s.cname);
		s.city="HYD";
	}
}
