# Nyaya Health Nepal Assignment

**Invitation for Assignment: Interview Candidate Evaluation**

There were a total of four questions  in the assignment as below:

![Assignment Questions](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/questions.png)

The repository structure is similar to the questions structure with each file/folder solving each question. The Q.2 & Q.3 is merged into the same project. The screenshots folder is for storing screenshots for documentation purposes.

# Solutions
## Q1: HTTP Request and Table Population

- File: Q1.html
- Description: This HTML file contains HTML, JavaScript, and Bootstrap code to make an HTTP request to an API endpoint and populate the retrieved data into a modal table dynamically.
- Instructions: 
    - Open Q1.html in a web browser.
    - Click on the `Get Data` button to fetch the data from the API as shown in the screenshot:
      
    ![Get Button](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/fetchbtn.png)

    - If successful, a modal will appear displaying the table with the retrieved data as shown in the screenshot:
      
    ![Fteched Table](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/fetchdata.png)

    - If anything went wrong, an error alert will be generated

## Q2 & Q3: EHR System with Django

- Files: Q2&3/
- Description: This part of the assignment involved creating a Django-based EHR system with database schema design and API development.
- Instructions:
  - Set up and activate a python virtual environment.
  - Install the required packages in a given environment using `pip install -r requirements.txt`.
  - Start the Django development server by running `python manage.py runserver` in the project root directory i.e. directory containing `manage.py` file
  - Access "http://127.0.0.1:8000/" in a web browser to view the list of patients with prescribed medicines as shown below:
    
  ![Patients Detail](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/drf.png)

**Note:**
For now, the only way to add Patient, Doctor, Medicine, and, prescription is from the Django admin panel(http://127.0.0.1:8000/admin/). For that, you can use: 
- Username: "Arbind_Mehta"
- Password: "123".

## Q4: Custom Odoo Module

- Files: Q4/
- Description: This question involved developing a custom module in Odoo (version 10) to fulfill specific requirements related to sales reporting.
- Instructions:
  - Set up Odoo 10 on your system.
  - Place the `custom_sales_report` module in the Odoo extra addons directory.
  - Restart the Odoo server.
  - Goto `Apps` and `Update Apps List` (Developer mode)
  - Search for `custom_sales_report` and install it as shown in the screenshot:
    
  ![Module Detail](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/image%20(1).png)
  
  - This module will add a submenu called `Custom Sales Report` under `Reports` menu of `Sales` which is visible only to `group_sale_manager` group as shown in the screenshot:
    
![Custom Sales Report menu](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/image%20(4).png)

- Upon clicking `Custom Sales Report` menu, it will open a wizard as in the screenshot:
  
![Custom Sales Report Wizard](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/image%20(2).png)

- Fill up details as per requirements and press `Generate Report` button, which will print the pdf report as in the screenshot:

![PDF Report](https://raw.githubusercontent.com/Arbind15/NayaHealthAssignment/main/screenshots/image%20(3).png)








