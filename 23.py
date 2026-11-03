import xml.etree.ElementTree as ET

def modify_student_xml(input_file, output_file):
    # Parse the existing XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # 1. Modify an existing record: Update CGPA for student ID 101
    for student in root.findall('student'):
        if student.get('id') == '101':
            cgpa_element = student.find('cgpa')
            if cgpa_element is not None:
                cgpa_element.text = '8.5' # Updated CGPA
            
    # 2. Add a new student record
    new_student = ET.Element('student', id='111')
    
    name = ET.SubElement(new_student, 'name')
    name.text = 'Kavya Singh'
    
    department = ET.SubElement(new_student, 'department')
    department.text = 'IT'
    
    year = ET.SubElement(new_student, 'year')
    year.text = '1'
    
    email = ET.SubElement(new_student, 'email')
    email.text = 'kavya.singh@example.com'
    
    cgpa = ET.SubElement(new_student, 'cgpa')
    cgpa.text = '9.0'
    
    root.append(new_student)

    # Generate the modified XML document
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"XML successfully modified and saved to {output_file}")

# Usage
modify_student_xml('students.xml', 'modified_students.xml')
