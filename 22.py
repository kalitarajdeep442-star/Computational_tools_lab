import xml.etree.ElementTree as ET

def parse_university_xml(file_path):
    try:
        # Parse the XML document
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract and display University information
        uni_name = root.attrib.get('name', 'Unknown University')
        location = root.find('campus/location').text
        established = root.find('campus/established').text
        
        print(f"=== {uni_name.upper()} ===")
        print(f"Location: {location} | Established: {established}\n")
        
        # Iterate through departments
        departments = root.find('departments')
        for dept in departments.findall('department'):
            dept_name = dept.find('name').text
            dept_id = dept.attrib.get('id')
            hod = dept.find('hod').text
            
            print(f"Department: {dept_name} ({dept_id})")
            print(f"Head of Department: {hod}")
            print("-" * 40)
            
            # Iterate through students in the department
            students = dept.find('students')
            for student in students.findall('student'):
                student_id = student.attrib.get('id')
                
                # Extract Personal Details
                personal = student.find('personal_details')
                first_name = personal.find('name/first_name').text
                last_name = personal.find('name/last_name').text
                
                # Extract Academic Details
                academic = student.find('academic_details')
                year = academic.find('year').text
                cgpa = academic.find('cgpa').text
                
                print(f"  * {first_name} {last_name} (ID: {student_id})")
                print(f"    Year: {year} | CGPA: {cgpa}")
            
            print("\n")
            
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ET.ParseError:
        print("Error: The file is not a valid XML document.")

if __name__ == "__main__":
    # Reference the target file verbatim
    parse_university_xml("university_records_2.xml")
