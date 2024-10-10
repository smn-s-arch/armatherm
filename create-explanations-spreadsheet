Table of Contents

	1.	Overview
	2.	Step 1: Set Up the Spreadsheet Structure
	3.	Step 2: Define Headers and Their Purposes
	4.	Step 3: Implement Data Validation
	5.	Step 4: Create Helper Sheets for Operators and Variables
	6.	Step 5: Develop Formulas for JSON Generation
	7.	Step 6: Populate Sample Data
	8.	Step 7: Exporting the Spreadsheet to CSV
	9.	Step 8: Best Practices and Maintenance
	10.	Additional Tips
	11.	Conclusion

Overview

The goal is to create a user-friendly spreadsheet that allows you to:

	•	Define options and their explanations for different categories and parts.
	•	Specify dependencies in a structured format without manually writing JSON.
	•	Automate the generation of JSON strings required for the dependencyExpression and action fields.
	•	Ensure data integrity through validation and error checking.
	•	Easily export the data into the required explanations.csv format.

By following this guide, you’ll build a robust system that simplifies dependency management and minimizes the risk of errors.

Step 1: Set Up the Spreadsheet Structure

1.1 Choose Your Spreadsheet Software

You can use either Microsoft Excel or Google Sheets. Both offer robust features, but Google Sheets provides easier collaboration and cloud storage.

1.2 Create a New Spreadsheet

	•	Name: Dependency_Management
	•	Tabs/Sheets: You’ll primarily work within one sheet, but helper sheets will be created later.

Step 2: Define Headers and Their Purposes

2.1 Main Sheet Structure

In the first sheet (e.g., Dependencies), set up the following headers in Row 1, starting from Column A:

	1.	A1: Category
	2.	B1: PartIndex
	3.	C1: OptionValue
	4.	D1: Explanation
	5.	E1: DependencyExpression
	6.	F1: Action

2.2 Header Descriptions

	•	Category: The product or item category (e.g., Rohrfedermanometer).
	•	PartIndex: The zero-based index indicating the part of the matchcode.
	•	OptionValue: The specific value for the option (e.g., R10).
	•	Explanation: A description or explanation of the option.
	•	DependencyExpression: JSON-formatted string defining dependencies.
	•	Action: JSON-formatted string defining any actions upon selection.

Step 3: Implement Data Validation

Data validation ensures that entries adhere to expected formats and values, reducing errors.

3.1 PartIndex Validation

	•	Purpose: Ensure PartIndex is an integer (e.g., 0, 1, 2, 3).
	•	How-To:
	1.	Select Column B (excluding the header).
	2.	Go to Data > Data Validation.
	3.	Criteria: Whole number between 0 and the maximum number of parts you have.
	4.	On invalid data: Show a warning or reject the input.
	5.	Save.

3.2 Operator Validation for DependencyExpression

To simplify dependency creation, create a helper sheet listing supported operators.

3.2.1 Create a Helper Sheet

	1.	Add a new sheet: Name it Operators.
	2.	List Supported Operators:
	•	A1: Operator
	•	A2: ==
	•	A3: !=
	•	A4: IN
	•	A5: NOT IN

3.2.2 Apply Dropdown in DependencyExpression

Since dependencies are JSON arrays, direct operator selection isn’t straightforward. Instead, we’ll guide the user through structured inputs later.

For simplicity, skip this step as JSON will be generated through helper forms or formulas.

3.3 Category Selection Validation

If you have predefined categories:

	1.	List Categories:
	•	Create a new helper sheet: Name it Categories.
	•	A1: Category
	•	A2+: List all categories (e.g., Rohrfedermanometer, etc.).
	2.	Apply Dropdown:
	1.	Go back to the Dependencies sheet.
	2.	Select Column A (excluding header).
	3.	Go to Data > Data Validation.
	4.	Criteria: List from a range.
	5.	Range: Categories!A2:A (assuming categories start from A2).
	6.	Show dropdown list in cell.
	7.	Save.

If categories are dynamic, skip or adjust accordingly.

Step 4: Create Helper Sheets for Operators and Variables

To facilitate easier dependency creation, set up helper sheets that list variables and operators.

4.1 Variables Helper Sheet

	1.	Add a new sheet: Name it Variables.
	2.	List Variables:
	•	A1: Variable
	•	A2+: List all variables used in dependencies (e.g., part0, part1, etc.).

4.2 Operators Helper Sheet

Already created in Step 3.2.1 as Operators.

Step 5: Develop Formulas for JSON Generation

Manually writing JSON strings can be error-prone. Instead, use helper columns and formulas to auto-generate these strings based on user inputs.

5.1 Design the Workflow

	1.	User Inputs:
	•	Define dependencies using separate columns (e.g., Variable, Operator, Value).
	2.	Formulas:
	•	Combine these inputs into properly formatted JSON strings.
	3.	Output:
	•	Populate the DependencyExpression and Action columns automatically.

5.2 Implementing Dependency Conditions

5.2.1 Add Helper Columns

In the Dependencies sheet, add the following helper columns:

	•	G1: Condition1_Variable
	•	H1: Condition1_Operator
	•	I1: Condition1_Value
	•	J1: Condition2_Variable
	•	K1: Condition2_Operator
	•	L1: Condition2_Value
	•	(Add more conditions as needed.)

5.2.2 Apply Data Validation to Helper Columns

	1.	Variable Columns (G & J):
	•	Select Columns G and J (excluding headers).
	•	Go to Data > Data Validation.
	•	Criteria: List from range Variables!A2:A.
	•	Save.
	2.	Operator Columns (H & K):
	•	Select Columns H and K (excluding headers).
	•	Go to Data > Data Validation.
	•	Criteria: List from range Operators!A2:A5.
	•	Save.
	3.	Value Columns (I & L):
	•	No specific validation; allow free text or numbers.

5.2.3 Create a Formula to Generate JSON

In the DependencyExpression column (E2), use a formula to concatenate the conditions into a JSON array.

Example Formula for Single Condition:

=IF(G2<>"", 
  "[{\"variable\":\"" & G2 & "\",\"operator\":\"" & H2 & "\",\"value\":\"" & I2 & "\"}]", 
  "")

Example Formula for Two Conditions:

=IF(G2<>"", 
  "[{\"variable\":\"" & G2 & "\",\"operator\":\"" & H2 & "\",\"value\":\"" & I2 & "\"}" &
  IF(J2<>"", ", {\"variable\":\"" & J2 & "\",\"operator\":\"" & K2 & "\",\"value\":\"" & L2 & "\"}", "") & "]",
  "")

Adjust the formula based on the number of conditions you plan to support.

5.3 Implementing Actions

If actions are needed, use additional helper columns to define them.

5.3.1 Add Action Helper Columns

	•	M1: Action_SetPartIndex
	•	N1: Action_Value
	•	O1: Action_Hint

5.3.2 Populate Action Columns

Users can input the desired action details directly into these columns.

5.3.3 Create a Formula to Generate Action JSON

In the Action column (F2), use a formula to concatenate the action details into a JSON object.

Example Formula:

=IF(AND(M2<>"", N2<>""), 
  "{\"setPartIndex\":" & M2 & ",\"value\":\"" & N2 & "\",\"hint\":\"" & O2 & "\"}", 
  "")

If no action is needed, leave the fields empty.

Step 6: Populate Sample Data

With the structure in place, start entering data to ensure that the system works as intended.

6.1 Enter Sample Rows

Example Row Without Dependencies and Actions:

Category	PartIndex	OptionValue	Explanation	DependencyExpression	Action	Condition1_Variable	Condition1_Operator	Condition1_Value	Condition2_Variable	Condition2_Operator	Condition2_Value	Action_SetPartIndex	Action_Value	Action_Hint
Rohrfedermanometer	0	R10	trocken, Anschluss: Messing											

Example Row With Dependencies and Actions:

Category	PartIndex	OptionValue	Explanation	DependencyExpression	Action	Condition1_Variable	Condition1_Operator	Condition1_Value	Condition2_Variable	Condition2_Operator	Condition2_Value	Action_SetPartIndex	Action_Value	Action_Hint
Rohrfedermanometer	3	N96xN96		[{“variable”:“part1”,“operator”:”!=”,“value”:“HZ”}]	{“setPartIndex”:2,“value”:“4”,“hint”:“part2 has been set to ‘4’ because it’s the only valid option when part3 is ‘N96xN96’”}	part1	!=	HZ				2	4	part2 has been set to ‘4’ because it’s the only valid option when part3 is ‘N96xN96’

6.2 Verify JSON Generation

Ensure that the DependencyExpression and Action columns are correctly populated based on the helper columns.

Step 7: Exporting the Spreadsheet to CSV

Once your data is correctly entered and JSON strings are generated, export the spreadsheet to explanations.csv.

7.1 Prepare for Export

	1.	Hide Helper Columns:
	•	To avoid clutter, hide the helper columns (G to O).
	•	How-To: Right-click on the column headers and select Hide column.
	2.	Review Data:
	•	Double-check that all necessary fields are filled and that JSON strings are correctly formatted.
	•	Ensure no unintended data exists in the hidden columns.

7.2 Export Process

In Microsoft Excel:

	1.	Go to File > Save As.
	2.	Choose the location where you want to save the file.
	3.	Select CSV (Comma delimited) (*.csv) as the file format.
	•	Note: Since your data uses semicolons (;) as delimiters, you’ll need to adjust the delimiter settings.
	4.	Change the delimiter to semicolon:
	•	Windows Users:
	•	Go to Control Panel > Region > Additional settings.
	•	Change the List separator from comma to semicolon.
	•	Click OK.
	•	Save the CSV from Excel.
	•	Revert the list separator back to comma after saving.
	•	Mac Users:
	•	Similar settings can be adjusted via System Preferences > Language & Region > Advanced.
	5.	Click Save.

In Google Sheets:

	1.	Go to File > Download > Comma-separated values (.csv, current sheet).
	2.	Rename the file to explanations.csv.
	3.	Open the CSV in a text editor and replace all commas with semicolons (;).
	•	Alternatively: Use a script or tool to change the delimiter.

Google Sheets does not natively support exporting with semicolon delimiters, so manual adjustment or scripting is necessary.

7.3 Verify the CSV File

	•	Open the CSV in a text editor to ensure that:
	•	Semicolons (;) are used as delimiters.
	•	JSON strings in DependencyExpression and Action are correctly formatted and enclosed in quotes if necessary.

Step 8: Best Practices and Maintenance

8.1 Regular Backups

	•	Frequency: Back up your spreadsheet regularly, especially before making significant changes.
	•	Method: Use cloud storage with version history (e.g., Google Drive) or manual backups on external drives.

8.2 Data Validation

	•	Consistency Checks: Periodically review data entries to ensure consistency and correctness.
	•	Error Logs: Maintain a log of any errors encountered during JSON generation or CSV export for troubleshooting.

8.3 Documentation

	•	Internal Guide: Maintain a separate sheet within the spreadsheet (Guide or Instructions) detailing how to use the system.
	•	Change Log: Keep track of changes made to the spreadsheet structure or formulas.

8.4 Training

	•	Familiarize Yourself: Ensure you understand how each part of the spreadsheet works, especially the formulas generating JSON.
	•	Experiment: Create test rows to understand how dependencies and actions affect the JSON outputs.

Additional Tips

	1.	Use Conditional Formatting:
	•	Highlight rows with missing mandatory fields to prompt completion.
	•	For example, apply a red fill to rows where Category, PartIndex, or OptionValue are empty.
	2.	Leverage Templates:
	•	Duplicate existing rows to maintain consistency when adding similar options.
	•	This helps preserve the structure of dependencies and actions.
	3.	Automate with Macros (Advanced):
	•	If using Excel, consider recording macros to automate repetitive tasks like JSON generation.
	•	Note: Macros can add complexity and may not be necessary for a single-person system.
	4.	Utilize Search and Filter:
	•	Use the spreadsheet’s filter feature to quickly find specific categories, parts, or options.
	5.	Stay Organized:
	•	Keep related options grouped together for easier navigation and management.
	•	Use color-coding or borders to separate different sections or categories.

Conclusion

By following this guide, you’ve established a structured and efficient spreadsheet-based system for managing dependencies within your explanations.csv file. This system leverages the inherent strengths of spreadsheet software—such as data validation, formula automation, and ease of use—to simplify complex dependency management tasks.

Key Takeaways:

	•	Structured Approach: Organizing data systematically reduces errors and enhances clarity.
	•	Automation: Utilizing formulas to generate JSON strings minimizes manual input and potential mistakes.
	•	Validation: Implementing data validation ensures that entries conform to expected formats and values.
	•	Maintenance: Regular backups and documentation are essential for sustaining the system’s integrity over time.

Next Steps:

	1.	Start Small: Begin by entering a few rows of data to test the system and ensure that JSON generation works correctly.
	2.	Iterate and Improve: As you become more comfortable, expand the system to accommodate more complex dependencies and actions.
	3.	Seek Feedback: Even as the sole manager, periodically review the system’s efficiency and adjust processes as needed.

Feel free to reach out if you encounter any challenges or need further assistance in refining your dependency management system!
