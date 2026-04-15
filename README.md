# JSON to XML Converter (Python)

## 📌 Overview

This project is a Python-based command-line tool that converts JSON data into XML format based on a predefined specification.

The conversion follows strict rules where:

* XML tags represent the **type** of JSON values
* JSON keys are stored as **name attributes** in XML elements

---

## ⚙️ Features

* Supports all JSON types:

  * Object
  * Array
  * String
  * Number
  * Boolean
  * Null
* Recursive parsing for nested structures
* Pretty-printed XML output (indented)
* Command Line Interface (CLI)
* Error handling for:

  * Invalid JSON
  * Missing files
  * Incorrect arguments

---

## 🚀 How to Run

### Step 1: Prepare input file

Create a JSON file (example: `input.json`)

Example:

```json
{
  "name": "John",
  "age": 25,
  "skills": ["python", "sql"]
}
```

---

### Step 2: Run the program

```bash
python script.py input.json output.xml
```

---

### Step 3: Check output

The XML output will be written to:

```
output.xml
```

---

## 📁 Project Structure

```
json-to-xml-converter/
│
├── script.py        # Main Python script
├── input.json       # Sample input file
├── output.xml       # Generated output file
└── README           # Project documentation
```

---

## 🧠 Design Approach

* Used **recursion** to handle nested JSON structures
* Type detection using `isinstance`
* Separate handlers for:

  * Objects
  * Arrays
* Indentation handled via recursion depth

---

## ⚠️ Constraints

* Top-level JSON must be:

  * Object OR Array
* Arrays do not include `name` attributes for elements

---

## 🛠 Dependencies

* Python 3.x
* No external libraries required

---

## ✅ Example Output

Input:

```json
{
  "age": 25
}
```

Output:

```xml
<object>
    <number name="age">25</number>
</object>
```

---

## 👤 Author

Nowfal
